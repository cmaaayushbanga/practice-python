import random

# List of questions and their corresponding answers
questions = [
    {
        'question': 'What is a specialised branch of accounting that keeps track of a companys financial transactions?',
        'options': ['A. cost accouting', 'B. management accounting', 'C. financial accouting', 'D. corporate accounting'],
        'answer': 'c'
    },
    {
        'question': 'Financial accounting provides accounting information to the ________ though the information is useful for internal purposes also?',
        'options': ['A. external users', 'B. internal users', 'C. company', 'D. competitors'],
        'answer': 'a'
    },
    {
        'question': 'Financial accounting cover overall performance of the?',
        'options': ['A. external users', 'B. internal users', 'C. company', 'D. competitors'],
        'answer': 'c'
    }
]

def play_game():
    total_amount = 0
    random.shuffle(questions)  # Shuffle the questions to randomize the order
    
    print("Welcome to the KBC game!")
    print("Answer the following questions to win cash prizes.")
    
    for int, question in enumerate(questions, start=1):
        print(f"\nQuestion {int}: {question['question']}")
        for option in question['options']:
            print(option)
        
        Useranswer = input("Enter your answer (A, B, C, or D): ").lower()
        
        if Useranswer == question['answer']:
            print("Congratulations! You got the correct answer.")
            total_amount += 1000  # Add the prize amount for a correct answer
        else:
            print("Oops! That's incorrect.")
            break
    
    print("\nGame over!")
    print(f"You won a total amount of ${total_amount}.")
    
play_game()