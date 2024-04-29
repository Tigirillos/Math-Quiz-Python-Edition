import random

# Function to generate a random math question
def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    question = f"What is {num1} {operator} {num2}?"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer

# Function to display options for multiple-choice
def display_options(answer):
    options = [answer]
    while len(options) < 4:
        option = random.randint(answer - 10, answer + 10)
        if option != answer and option not in options:
            options.append(option)
    random.shuffle(options)
    return options

# Function to take the quiz
def take_quiz():
    score = 0
    questions = []
    print("\n Let's see how good you are at Math! Here we go!\n")
    for i in range(10):
        question, answer = generate_question()
        options = display_options(answer)
        print(f"\nQuestion {i+1}: {question}\n")
        for idx, option in enumerate(options, start=1):
            print(f" {idx}. {option}")
        user_answer = input("\nYour answer (1/2/3/4): ")
        if user_answer in ['1', '2', '3', '4']:
            user_answer_idx = int(user_answer) - 1
            if options[user_answer_idx] == answer:
                score += 10
                print("Correct!")
            else:
                print("Incorrect!")
        else:
            print("Invalid input! Please enter 1, 2, 3, or 4.")
            i -= 1
            continue
        questions.append((question, options, answer))
    return score, questions

# Main function to run the quiz
def main():
    score, questions = take_quiz()
    print("\n--- Quiz Result ---")
    if score >= 70:
        print(f"You passed with a score of {score}!")
    else:
        print(f"You failed with a score of {score}.")

if __name__ == "__main__":
    main()
