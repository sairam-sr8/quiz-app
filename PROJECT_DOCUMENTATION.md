# AI-Powered Quiz Generator - Project Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Technology Stack](#technology-stack)
4. [Setup Guide](#setup-guide)
5. [Project Structure](#project-structure)
6. [Features](#features)
7. [How It Works](#how-it-works)
8. [User Guide](#user-guide)
9. [Troubleshooting](#troubleshooting)
10. [Future Enhancements](#future-enhancements)

## Introduction

Welcome to the AI-Powered Quiz Generator! This application allows you to create, take, and manage quizzes on any topic using artificial intelligence. Whether you're a teacher, student, or just someone who loves learning, this tool makes quiz creation and taking simple and fun.

## Project Overview

The AI Quiz Generator is a web application that:
- Uses AI to generate quiz questions on any topic
- Provides a modern, user-friendly interface
- Tracks quiz progress and results
- Allows users to create and manage multiple quizzes

## Technology Stack

The project uses the following technologies:

1. **Python**: The main programming language
2. **Django**: A web framework that makes building websites easier
3. **Google Gemini API**: An AI service that generates quiz questions
4. **HTML/CSS**: For creating the website's look and feel
5. **Tailwind CSS**: A design framework for making the website look modern
6. **SQLite**: A database to store quizzes and results

## Setup Guide

### Prerequisites
- Python 3.8 or higher
- A Google Gemini API key
- A code editor (like Visual Studio Code)

### Installation Steps

1. **Install Python**
   - Download Python from python.org
   - During installation, check "Add Python to PATH"

2. **Set Up the Project**
   ```bash
   # Create a new folder for your project
   mkdir quiz-app
   cd quiz-app

   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate

   # Install required packages
   pip install django python-dotenv google-generativeai
   ```

3. **Get Your API Key**
   - Go to Google AI Studio (https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Create a file named `.env` in your project folder
   - Add your API key: `GOOGLE_API_KEY=your_api_key_here`

4. **Create the Django Project**
   ```bash
   django-admin startproject quizgen
   cd quizgen
   python manage.py startapp quiz
   ```

5. **Configure Settings**
   - Open `quizgen/settings.py`
   - Add 'quiz' to INSTALLED_APPS
   - Configure the database settings
   - Add your static files configuration

6. **Create Models**
   - Create models for Quiz and Question in `quiz/models.py`
   - Run migrations: `python manage.py makemigrations`
   - Apply migrations: `python manage.py migrate`

7. **Create Views and Templates**
   - Create views in `quiz/views.py`
   - Create templates in `quiz/templates/quiz/`
   - Set up URLs in `quiz/urls.py`

8. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   - Open your browser and go to http://127.0.0.1:8000/

## Project Structure

```
quiz-app/
├── quizgen/                 # Main project folder
│   ├── settings.py          # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # Web server configuration
├── quiz/                    # Quiz application folder
│   ├── models.py           # Database models
│   ├── views.py            # Application logic
│   ├── urls.py             # Application URLs
│   ├── templates/          # HTML templates
│   │   └── quiz/
│   │       ├── base.html   # Base template
│   │       ├── home.html   # Home page
│   │       ├── quiz.html   # Quiz page
│   │       └── results.html # Results page
│   └── static/             # CSS and JavaScript files
├── .env                    # Environment variables
└── manage.py              # Django management script
```

## Features

### 1. Quiz Creation
- Enter any topic
- Set number of questions (1-20)
- Set time limit
- AI generates questions automatically

### 2. Quiz Taking
- Modern, user-friendly interface
- Timer display
- Progress tracking
- Question navigation
- Immediate feedback

### 3. Results
- Score calculation
- Detailed feedback
- Correct answers and explanations
- Time taken analysis

### 4. Quiz Management
- View all quizzes
- Delete quizzes
- Track quiz history
- View previous results

## How It Works

### 1. AI Question Generation
- User enters a topic
- Application sends request to Google Gemini API
- AI generates questions and answers
- Questions are stored in the database

### 2. Quiz Taking Process
- User selects a quiz
- Questions are displayed one at a time
- Timer tracks remaining time
- User selects answers
- Results are calculated and stored

### 3. Results Processing
- Correct answers are checked
- Score is calculated
- Time taken is recorded
- Detailed feedback is generated

## User Guide

### Creating a Quiz
1. Go to the home page
2. Enter a topic (e.g., "Python Programming")
3. Set number of questions (1-20)
4. Set time limit in minutes
5. Click "Generate Quiz"

### Taking a Quiz
1. Select a quiz from the list
2. Read each question carefully
3. Select your answer
4. Use navigation buttons to move between questions
5. Click "Submit Quiz" when finished

### Viewing Results
1. After submitting, you'll see your score
2. Review correct answers
3. Read explanations for each question
4. Option to create a new quiz

## Troubleshooting

### Common Issues

1. **API Key Not Working**
   - Check if the API key is correctly set in .env file
   - Ensure the key is active in Google AI Studio
   - Verify the key has proper permissions

2. **Questions Not Generating**
   - Check your internet connection
   - Verify the topic is clear and specific
   - Try a different topic

3. **Server Not Starting**
   - Ensure Python is installed correctly
   - Check if all required packages are installed
   - Verify the virtual environment is activated

### Error Messages

1. **"Invalid API Key"**
   - Solution: Update the API key in .env file

2. **"Database Error"**
   - Solution: Run migrations again
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **"Page Not Found"**
   - Solution: Check if the server is running
   - Verify the URL is correct

## Future Enhancements

1. **User Accounts**
   - Personal quiz history
   - Progress tracking
   - Custom quiz settings

2. **Advanced Features**
   - Multiple choice types
   - Image-based questions
   - Audio questions
   - Custom difficulty levels

3. **Social Features**
   - Share quizzes
   - Compete with friends
   - Leaderboards
   - Comments and feedback

4. **Learning Analytics**
   - Performance tracking
   - Topic mastery levels
   - Personalized recommendations
   - Learning paths

## Conclusion

The AI Quiz Generator is a powerful tool that makes learning fun and interactive. By combining artificial intelligence with a user-friendly interface, it provides an engaging way to test knowledge on any topic. Whether you're a teacher creating quizzes for students or a learner testing your own knowledge, this application makes the process simple and effective.

Remember to:
- Keep your API key secure
- Regularly backup your database
- Update the application as new features are added
- Provide feedback for improvements

Happy quizzing! 