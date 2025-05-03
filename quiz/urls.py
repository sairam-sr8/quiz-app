from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-from-file/', views.create_quiz_from_file, name='create_quiz_from_file'),
    path('create-with-ai/', views.create_quiz_with_ai, name='create_quiz_with_ai'),
    path('recent-quizzes/', views.recent_quizzes, name='recent_quizzes'),
    path('quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('quiz/<int:quiz_id>/delete/', views.delete_quiz, name='delete_quiz'),
] 