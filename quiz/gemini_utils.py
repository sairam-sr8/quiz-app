import google.generativeai as genai
import json
from django.conf import settings

# Configure the Gemini API
genai.configure(api_key=settings.GOOGLE_API_KEY)

def generate_quiz_questions(topic, num_questions=5):
    """Generate quiz questions using Gemini API."""
    try:
        # Use the correct model name
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        prompt = f"""
        Generate {num_questions} multiple-choice questions about {topic}.
        For each question, provide:
        1. The question text
        2. Four options (numbered 1-4)
        3. The correct answer (1-4)
        4. A brief explanation

        Return the response in this exact JSON format:
        [
            {{
                "question": "Question text here",
                "options": {{"1": "First option", "2": "Second option", "3": "Third option", "4": "Fourth option"}},
                "answer": "1",
                "explanation": "Explanation here"
            }},
            // ... more questions
        ]
        """

        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        # Try to find JSON in the response
        start_idx = response_text.find('[')
        end_idx = response_text.rfind(']') + 1
        if start_idx != -1 and end_idx != -1:
            json_str = response_text[start_idx:end_idx]
            questions = json.loads(json_str)
            
            # Validate the questions format
            for q in questions:
                required_keys = ['question', 'options', 'answer', 'explanation']
                if not all(key in q for key in required_keys):
                    raise ValueError("Invalid question format")
                if not all(str(i) in q['options'] for i in range(1, 5)):
                    raise ValueError("Missing options")
            
            return questions
        else:
            raise ValueError("No valid JSON found in response")
            
    except Exception as e:
        print(f"Error generating questions: {str(e)}")
        return [] 