# 5 quick python projects

# Quiz-game

# quiestions = [
#     {
#         "prompt" : "What is capital of France?",
#         "options" : ["A. Paris", "B. London", "C. Berlin", "D.Madrid"],
#         "answer" : "A"
#     },
#     {
#         "prompt" : "What is the smallest number?",
#         "options" : ["A. 2", "B. 1", "C. 3", "D.4"],
#         "answer" : "B"
#     },
#     {
#         "prompt" : "What is capital of Uzbekistan?",
#         "options" : ["A. Paris", "B. London", "C. Tashkent", "D.Madrid"],
#         "answer" : "C"
#     },
#     {
#         "prompt" : "What is capital of USA?",
#         "options" : ["A. Paris", "B. London", "C. Berlin", "D.Vashington"],
#         "answer" : "D"
#     }
# ]
#
# def run_quiz(questions):
#     score = 0
#     for question in questions:
#         print(question["prompt"])
#         for option in question["options"]:
#             print(option)
#         answer = input("Enter your answer(A, B, C or D): ").upper()
#         if answer == question["answer"]:
#             print("Correct, hooray!!!\n")
#             score += 1
#         else:
#             print("Wrong answer !!! The correct answer was", question["answer"], "\n")
#
#     print(f"You got {score} out of {len(questions)} questions correct.")
#
# run_quiz(quiestions)
# -----------------------------------------------------------------------------------------------------------------------
# Hangman

# import random
#
# words = ['python', 'django', 'html', 'css', 'telegram-bot']
#
# #Randomly choose a word from the list
# chosen_word = random.choice(words)
# word_display = ['_' for _ in chosen_word]
# attempts = 12 #Number of allowed attemps
#
# print("Welcome to Hangman!")
#
# while attempts > 0 and '_' in word_display:
#     print("\n" + ' '.join(word_display))
#     guess = input("Guess a letter: ").lower()
#     if guess in chosen_word:
#         for index, letter in enumerate(chosen_word):
#             if letter == guess:
#                 word_display[index] = guess #reveal letter
#     else:
#         print("This letter isn't suitable, idiot!!!.")
#         attempts -= 1
#
# #Game conclusion
# if '_' not in word_display:
#     print("You guessed the word!")
#     print(' '.join(word_display))
#     print("You survived!")
# else:
#     print("You run out of attemps. The word was: " + chosen_word)
#     print("You lost!")

# simple form of hangman
#
# import random
#
# words = ['python', 'django', 'html', 'css', 'telegram-bot']
# chosen_word = random.choice(words)
# attempts = 3
#
# while attempts > 0:
#     score = 0
#     guess = input("Write one word>>> ")
#     if chosen_word == guess:
#         print("You find!")
#         score += 1
#         attempts -= 1
#     else:
#         print("You are loser!")
#         attempts -= 1
# print(f"You found {score} word")
# -----------------------------------------------------------------------------------------------------------------------
# Budget_tracker
# import json
#
# def add_expense(expenses, description, amount):
#     expenses.append({"description": description, "amount": amount})
#     print(f"Added expenses: {description}, Amount: {amount}")
#
# def get_total_expenses(expenses):
#     sum = 0
#     for expense in expenses:
#         sum += expense["amount"]
#         return sum
#
#
# def get_balance(budget, expenses):
#     return budget - get_total_expenses(expenses)
#
#
# def show_budget_details(budget, expenses):
#     print(f"Total Budget: {budget}")
#     print("Expenses:")
#     for expense in expenses:
#         print(f"- {expense['description']}: {expense['amount']}")
#     print(f"Total Spent: {get_total_expenses(expenses)}")
#     print(f"Remaining Budget: {get_balance(budget, expenses)}")
#
#
# def load_budget_data(filepath):
#     try:
#         with open(filepath, "w") as file:
#             data = json.load(file)
#             return data["initial_budget"], data["expenses"]
#     except (FileNotFoundError, json.JSONDecodeError):
#         return 0, []
#
#
# def save_budget_details(filepath, initial_budget, expenses):
#     data = {
#         'initial_budget': initial_budget,
#         'expenses': expenses
#     }
#     with open(filepath, 'w') as file:
#         json.dump(data, file, indent=4)
#
#
# def main():
#     print("Welcome to the Budget App")
#     # initial_budget = float(input("Please enter your initial budget: "))
#     filepath = 'budget_data.json'
#     initial_budget, expenses = load_budget_data(filepath)
#     if initial_budget == 0:
#         initial_budget = float(input("Please enter your initial budget: "))
#     budget = initial_budget
#
#     while True:
#         print("\nWhat would you like to do?")
#         print("1. Add an expense")
#         print("2. Show budget details")
#         print("3. Exit")
#         choice = input("Enter your choice (1/2/3): ")
#
#         if choice == "1":
#             description = input("Enter expense description: ")
#             amount = float(input("Enter expense amount: "))
#             add_expense(expenses, description, amount)
#         elif choice == "2":
#             show_budget_details(budget, expenses)
#         elif choice == "3":
#             save_budget_details(filepath, initial_budget, expenses)
#             print("Exiting Budget App. Goodbye!")
#             break
#         else:
#             print("Invalid choice, please choose again.")
#
#
# if __name__ == "__main__":
#     main()

# Language learning app
# import random
#
# words = [
#     {'uzbek': 'ona', 'english': 'mother'},
#     {'uzbek': 'ota', 'english': 'father'},
#     {'uzbek': 'aka', 'english': 'brother'},
#     {'uzbek': 'singil', 'english': 'sister'},
#     {'uzbek': 'mashina', 'english': 'car'},
#     {'uzbek': 'home', 'english': 'uy'},
#     {'uzbek': 'phone', 'english': 'telefon'},
#     {'uzbek': 'laptop', 'english': 'komputer'},
#     {'uzbek': 'apartement', 'english': 'kvartira'},
#     {'uzbek': 'windows', 'english': 'oyna'}
# ]
#
# def quiz_user(words):
#     random.shuffle(words)
#     score = 0
#
#     for word in words:
#         print(f"What is the English translation of '{word['uzbek']}' ?")
#         user_answer = input("Your answer>>>").strip().lower()
#         correct_answer = word['english'].lower()
#
#
#         if correct_answer == user_answer:
#             print("Coool! Correct!!!\n")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer is {word['english']}.\n")
#
#     print(f"You find {score} answers")
#
# def main():
#     print("Welcome to the English Learning app!")
#     input("Press Enter to star the quiz...")
#     quiz_user(words)
#
#
# if __name__ == "__main__":
#     main()

# Desctop cleaner

import os
import shutil


def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path
    

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            print((os.path.join(folder_path, filename)))
            file_extension = filename.split(' ')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} files"
                subfolder_path =create_subfolder_if_needed(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                new_location = os.path.join(subfolder_path, filename)
                if not os.path.exists(new_location):
                    shutil.move(file_path, subfolder_path)
                    print(f"Moved: {filename}---> {subfolder_name}")
                else:
                    print(f"Scipped: {filename} already exists in {subfolder_name}")



if __name__ == "__main__":
    print("Desctop Cleaner Script")
    folder_path = ''
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning complete>>>")
    else:
        print("Invalid folder path!!!")
