# File Guide - AI Quiz Generator

This guide explains the purpose and significance of each file in the project.

## Project Configuration Files

### `manage.py`
- **Purpose**: Django's command-line utility for administrative tasks
- **Significance**: 
  - Used to run development server
  - Create database migrations
  - Manage Django applications
- **Key Commands**:
  ```bash
  python manage.py runserver    # Start development server
  python manage.py makemigrations  # Create database migrations
  python manage.py migrate      # Apply migrations
  ```

### `quizgen/settings.py`
- **Purpose**: Main configuration file for the Django project
- **Significance**:
  - Defines installed applications
  - Configures database settings
  - Sets up static files
  - Manages security settings
- **Key Sections**:
  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'quiz',  # Our quiz application
  ]
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
  ```

### `quizgen/urls.py`
- **Purpose**: Main URL configuration for the project
- **Significance**:
  - Defines URL patterns
  - Routes requests to appropriate views
- **Key Code**:
  ```python
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('quiz.urls')),
  ]
  ```

## Application Files

### `quiz/models.py`
- **Purpose**: Defines database models
- **Significance**:
  - Creates database structure
  - Defines relationships between models
  - Handles data storage
- **Key Models**:
  ```python
  class Quiz(models.Model):
      topic = models.CharField(max_length=200)
      num_questions = models.IntegerField()
      time_limit = models.IntegerField()
      created_at = models.DateTimeField(auto_now_add=True)

  class Question(models.Model):
      quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
      question_text = models.TextField()
      option1 = models.CharField(max_length=200)
      option2 = models.CharField(max_length=200)
      option3 = models.CharField(max_length=200)
      option4 = models.CharField(max_length=200)
      correct_answer = models.IntegerField()
      explanation = models.TextField()
  ```

### `quiz/views.py`
- **Purpose**: Contains application logic
- **Significance**:
  - Handles user requests
  - Processes form data
  - Renders templates
- **Key Functions**:
  ```python
  def home(request):
      # Handles quiz creation
      pass

  def take_quiz(request, quiz_id):
      # Manages quiz taking process
      pass

  def quiz_results(request, quiz_id):
      # Processes and displays results
      pass
  ```

### `quiz/urls.py`
- **Purpose**: Defines application-specific URLs
- **Significance**:
  - Routes application requests
  - Defines URL patterns for views
- **Key Patterns**:
  ```python
  urlpatterns = [
      path('', views.home, name='home'),
      path('quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
      path('quiz/<int:quiz_id>/results/', views.quiz_results, name='quiz_results'),
  ]
  ```

### `quiz/gemini_utils.py`
- **Purpose**: Handles AI question generation
- **Significance**:
  - Interfaces with Google Gemini API
  - Generates quiz questions
  - Processes AI responses
- **Key Functions**:
  ```python
  def generate_quiz_questions(topic, num_questions=5):
      # Generates questions using Gemini API
      pass
  ```

## Template Files

### `quiz/templates/quiz/base.html`
- **Purpose**: Base template for all pages
- **Significance**:
  - Defines common layout
  - Includes shared resources
  - Sets up navigation
- **Key Sections**:
  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <title>{% block title %}Quiz App{% endblock %}</title>
      <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  </head>
  <body>
      {% block content %}{% endblock %}
  </body>
  </html>
  ```

### `quiz/templates/quiz/home.html`
- **Purpose**: Home page template
- **Significance**:
  - Displays quiz creation form
  - Shows recent quizzes
  - Provides navigation
- **Key Features**:
  - Quiz creation form
  - Topic input
  - Question count selection
  - Time limit setting

### `quiz/templates/quiz/quiz.html`
- **Purpose**: Quiz taking interface
- **Significance**:
  - Displays questions
  - Shows timer
  - Handles navigation
- **Key Features**:
  - Question display
  - Answer options
  - Progress tracking
  - Timer functionality

### `quiz/templates/quiz/results.html`
- **Purpose**: Results display page
- **Significance**:
  - Shows quiz results
  - Displays correct answers
  - Provides explanations
- **Key Features**:
  - Score display
  - Question review
  - Correct answers
  - Explanations

## Static Files

### `quiz/static/quiz/style.css`
- **Purpose**: Custom styling
- **Significance**:
  - Defines custom styles
  - Enhances user interface
  - Provides animations
- **Key Features**:
  - Glass card effect
  - Gradient backgrounds
  - Hover animations
  - Responsive design

## Environment Files

### `.env`
- **Purpose**: Stores environment variables
- **Significance**:
  - Secures API keys
  - Manages configuration
  - Separates settings
- **Key Variables**:
  ```
  GOOGLE_API_KEY=your_api_key_here
  ```

## Database Files

### `db.sqlite3`
- **Purpose**: SQLite database file
- **Significance**:
  - Stores quiz data
  - Maintains user progress
  - Records results
- **Contents**:
  - Quiz records
  - Question data
  - User responses
  - Results history 