# Quick Start Guide - AI Quiz Generator

This guide will help you get the AI Quiz Generator up and running in minutes!

## 1. Install Python
- Download Python from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"
- Verify installation: Open terminal and type `python --version`

## 2. Get Your API Key
- Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
- Create a new API key
- Copy your API key

## 3. Set Up the Project
```bash
# Create project directory
mkdir quiz-app
cd quiz-app

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install required packages
pip install django python-dotenv google-generativeai
```

## 4. Configure Environment
- Create a file named `.env` in your project folder
- Add your API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## 5. Run the Application
```bash
# Start the development server
python manage.py runserver
```

## 6. Access the Application
- Open your browser
- Go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Quick Reference

### Creating a Quiz
1. Enter a topic (e.g., "Python Programming")
2. Set number of questions (1-20)
3. Set time limit in minutes
4. Click "Generate Quiz"

### Taking a Quiz
1. Select a quiz from the list
2. Read each question
3. Select your answer
4. Use navigation buttons
5. Click "Submit Quiz"

### Viewing Results
1. Check your score
2. Review correct answers
3. Read explanations
4. Create new quiz if desired

## Common Commands
```bash
# Start server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser
```

## Troubleshooting Quick Fixes

### Server Won't Start
- Check if Python is installed: `python --version`
- Verify virtual environment is activated
- Ensure all packages are installed

### API Key Issues
- Check `.env` file exists
- Verify API key is correct
- Ensure key is active in Google AI Studio

### Database Errors
```bash
# Reset database
python manage.py migrate --reset
```

## Need More Help?
- Check the full documentation in `PROJECT_DOCUMENTATION.md`
- Review file details in `FILE_GUIDE.md`
- Contact support if issues persist 