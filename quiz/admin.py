from django.contrib import admin
from .models import Quiz, Question

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('topic', 'time_limit', 'created_at', 'score', 'completed')
    list_filter = ('completed', 'created_at')
    search_fields = ('topic',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz', 'correct_answer')
    list_filter = ('quiz',)
    search_fields = ('question_text',) 