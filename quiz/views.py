from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Quiz, Question
from .gemini_utils import generate_quiz_questions
from .utils import parse_quiz_file
import logging

logger = logging.getLogger(__name__)

def home(request):
    # Get recent quizzes
    recent_quizzes = Quiz.objects.all().order_by('-created_at')[:5]
    return render(request, "quiz/home.html", {
        'recent_quizzes': recent_quizzes
    })

def create_quiz_from_file(request):
    if request.method == "POST":
        try:
            quiz_file = request.FILES.get("quiz_file")
            time_limit = int(request.POST.get("time_limit", 10))

            if not quiz_file:
                messages.error(request, "Please upload a quiz file")
                return redirect("home")

            # Create new quiz
            quiz = Quiz.objects.create(
                topic=f"Quiz from {quiz_file.name}",
                num_questions=0,  # Will be updated after parsing
                time_limit=time_limit
            )

            # Parse questions from file
            try:
                questions = parse_quiz_file(quiz_file)
                quiz.num_questions = len(questions)
                quiz.save()
            except Exception as e:
                messages.error(request, f"Error parsing quiz file: {str(e)}")
                quiz.delete()
                return redirect("home")
            
            # Save questions
            for q in questions:
                Question.objects.create(
                    quiz=quiz,
                    question_text=q["question"],
                    option1=q["options"]["1"],
                    option2=q["options"]["2"],
                    option3=q["options"]["3"],
                    option4=q["options"]["4"],
                    correct_answer=int(q["answer"]),
                    explanation=q["explanation"]
                )

            return redirect("take_quiz", quiz_id=quiz.id)

        except Exception as e:
            logger.error(f"Error creating quiz from file: {str(e)}")
            messages.error(request, "An error occurred while creating the quiz")
            return redirect("home")

    return redirect("home")

def create_quiz_with_ai(request):
    if request.method == "POST":
        try:
            topic = request.POST.get("topic", "").strip()
            num_questions = int(request.POST.get("num_questions", 5))
            time_limit = int(request.POST.get("time_limit", 10))

            if not topic:
                messages.error(request, "Please enter a topic")
                return redirect("home")

            if num_questions < 1 or num_questions > 20:
                messages.error(request, "Number of questions must be between 1 and 20")
                return redirect("home")

            # Create new quiz
            quiz = Quiz.objects.create(
                topic=topic,
                num_questions=num_questions,
                time_limit=time_limit
            )

            # Generate questions using AI
            questions = generate_quiz_questions(topic, num_questions)
            
            if not questions:
                messages.error(request, "Failed to generate questions. Please try again.")
                quiz.delete()
                return redirect("home")
            
            # Save questions
            for q in questions:
                Question.objects.create(
                    quiz=quiz,
                    question_text=q["question"],
                    option1=q["options"]["1"],
                    option2=q["options"]["2"],
                    option3=q["options"]["3"],
                    option4=q["options"]["4"],
                    correct_answer=int(q["answer"]),
                    explanation=q["explanation"]
                )

            return redirect("take_quiz", quiz_id=quiz.id)

        except Exception as e:
            logger.error(f"Error creating quiz with AI: {str(e)}")
            messages.error(request, "An error occurred while creating the quiz")
            return redirect("home")

    return redirect("home")

def recent_quizzes(request):
    quizzes = Quiz.objects.all().order_by('-created_at')
    return render(request, 'quiz/recent_quizzes.html', {'quizzes': quizzes})

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    
    if request.method == "POST":
        correct_answers = 0
        total_questions = questions.count()
        user_answers = {}
        
        # Process each question
        for question in questions:
            selected_option = request.POST.get(f'q{question.id}')
            if selected_option:
                user_answer = int(selected_option)
                user_answers[question.id] = user_answer
                if user_answer == question.correct_answer:
                    correct_answers += 1
            else:
                user_answers[question.id] = None
        
        # Calculate score
        score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        quiz.score = score
        quiz.completed = True
        quiz.save()
        
        # Store user answers in session
        request.session[f'quiz_{quiz_id}_answers'] = user_answers
        
        return redirect("quiz_results", quiz_id=quiz.id)
    
    return render(request, "quiz/quiz.html", {
        'quiz': quiz,
        'questions': questions
    })

def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    messages.success(request, "Quiz deleted successfully")
    return redirect("home") 