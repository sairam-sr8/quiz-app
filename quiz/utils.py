import pandas as pd
import logging

logger = logging.getLogger(__name__)

def parse_quiz_file(file):
    """
    Parse a CSV or Excel file containing quiz questions.
    Expected format:
    - CSV/Excel should have columns: question, option1, option2, option3, option4, correct_answer, explanation
    - correct_answer should be a number (1-4) indicating the correct option
    """
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        
        # Validate required columns
        required_columns = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_answer', 'explanation']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("File must contain all required columns: question, option1, option2, option3, option4, correct_answer, explanation")
        
        # Convert to list of dictionaries
        questions = []
        for _, row in df.iterrows():
            try:
                correct_answer = int(row['correct_answer'])
                if not 1 <= correct_answer <= 4:
                    raise ValueError(f"Correct answer must be between 1 and 4, got {correct_answer}")
                
                questions.append({
                    'question': str(row['question']),
                    'options': {
                        '1': str(row['option1']),
                        '2': str(row['option2']),
                        '3': str(row['option3']),
                        '4': str(row['option4'])
                    },
                    'answer': str(correct_answer),
                    'explanation': str(row['explanation'])
                })
            except (ValueError, TypeError) as e:
                logger.error(f"Error parsing row: {str(e)}")
                continue
        
        if not questions:
            raise ValueError("No valid questions found in the file")
        
        return questions
    
    except Exception as e:
        logger.error(f"Error parsing quiz file: {str(e)}")
        raise 