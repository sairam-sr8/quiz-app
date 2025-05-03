from django.db import models
from django.utils import timezone

class Quiz(models.Model):
    topic = models.CharField(max_length=200)
    num_questions = models.IntegerField(default=5)
    time_limit = models.IntegerField(default=10)  # in minutes
    created_at = models.DateTimeField(default=timezone.now)
    score = models.FloatField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.topic} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])
    explanation = models.TextField()

    def __str__(self):
        return self.question_text[:50] + "..." 