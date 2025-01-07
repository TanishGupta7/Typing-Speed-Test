import os
import random
import time
from datetime import datetime
import matplotlib.pyplot as plt

# Sentence pools for different difficulty levels
sentence_pools = {
    "easy": [
        "The cat sat on the mat.",
        "I like ice cream.",
        "This is a typing test.",
        "Dogs are loyal animals.",
        "The sky is blue."
    ],
    "medium": [
        "Python is a great programming language.",
        "The sun sets in the west.",
        "A journey of a thousand miles begins with a single step.",
        "Reading books is a great habit.",
        "Practice makes perfect."
    ],
    "hard": [
        "Artificial intelligence enables machines to learn from experience.",
        "Typing tests improve speed and accuracy.",
        "The quick brown fox jumps over the lazy dog.",
        "She sells seashells by the seashore.",
        "Developers should focus on writing clean and efficient code."
    ]
}
# Log file and leaderboard paths
log_file = "typing_speed_results.csv"
leaderboard_file = "leaderboard.csv"

def calculate_speed_and_accuracy(start_time, end_time, user_input, original_text):
    """Calculate typing speed, accuracy, and errors."""
    time_elapsed = end_time - start_time
    words_per_minute = len(user_input.split()) / (time_elapsed / 60)
    characters_per_minute = len(user_input) / (time_elapsed / 60)
    errors = sum(1 for i, char in enumerate(original_text) if i < len(user_input) and user_input[i] != char)
    errors += abs(len(original_text) - len(user_input))
    accuracy = max(0, 100 - (errors / max(len(original_text), 1) * 100))
    return round(words_per_minute), round(characters_per_minute), round(accuracy, 2), errors

def log_results(log_file, user_name, wpm, cpm, accuracy, errors, text):
    """Log results to a file."""
    with open(log_file, "a") as file:
        file.write(f"{user_name},{wpm},{cpm},{accuracy},{errors},\"{text}\"\n")

def update_leaderboard(leaderboard_file, user_name, wpm):
    """Update leaderboard with top scores."""
    leaderboard = []
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            leaderboard = [line.strip().split(',') for line in file]
    leaderboard.append([user_name, wpm])
    leaderboard = sorted(leaderboard, key=lambda x: float(x[1]), reverse=True)[:10]  # Top 10 scores
    with open(leaderboard_file, "w") as file:
        for entry in leaderboard:
            file.write(f"{entry[0]},{entry[1]}\n")

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_leaderboard():
    """Display the leaderboard."""
    if os.path.exists(leaderboard_file):
        print("\n***** LEADERBOARD *****")
        with open(leaderboard_file, "r") as file:
            for line in file:
                user, wpm = line.strip().split(',')
                print(f"{user}: {wpm} WPM")
    else:
        print("No leaderboard data available.")

def plot_performance(log_file, user_name):
    """Plot user's performance over time."""
    wpm = []
    accuracy = []
    with open(log_file, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == user_name:
                wpm.append(float(data[1]))
                accuracy.append(float(data[3]))
    if wpm:
        plt.plot(wpm, label="WPM")
        plt.plot(accuracy, label="Accuracy (%)")
        plt.xlabel("Test Number")
        plt.ylabel("Performance")
        plt.title(f"Performance Trends for {user_name}")
        plt.legend()
        plt.show()
    else:
        print("No performance data available.")

if __name__ == "__main__":
    print("***** WELCOME TO THE TYPING SPEED TEST *****\n")

    # Ask for the user's name
    user_name = input("Enter your name: ").strip() or "Anonymous"

    while True:
        # Display options
        print("\nOptions:")
        print("1. Start Typing Test")
        print("2. Add Custom Sentence")
        print("3. View Log File")
        print("4. View Leaderboard")
        print("5. View Performance Graph")
        print("6. Exit")
        choice = input("Enter your choice: ").strip().lower()

        if choice in ["1", "start typing test"]:
            # Typing test
            clear_screen()
            print("Choose difficulty level: Easy, Medium, Hard")
            level = input("Enter difficulty level: ").strip().lower()
            if level not in sentence_pools:
                print("Invalid difficulty level. Defaulting to Easy.")
                level = "easy"

            test_sentence = random.choice(sentence_pools[level])
            print("\nGet ready to type the following sentence:\n")
            print(f"\"{test_sentence}\"\n")
            print("You have 5 seconds to read. The timer starts now!")
            time.sleep(5)

            print("\nStart typing now!\n")
            start_time = time.time()
            user_input = input()
            end_time = time.time()

            # Calculate results
            wpm, cpm, accuracy, errors = calculate_speed_and_accuracy(start_time, end_time, user_input, test_sentence)

            # Display results
            print("\n***** TEST RESULTS *****")
            print(f"Words Per Minute (WPM): {wpm}")
            print(f"Characters Per Minute (CPM): {cpm}")
            print(f"Accuracy: {accuracy}%")
            print(f"Errors: {errors}\n")

            # Log results and update leaderboard
            log_results(log_file, user_name, wpm, cpm, accuracy, errors, test_sentence)
            update_leaderboard(leaderboard_file, user_name, wpm)

        elif choice in ["2", "add custom sentence"]:
            # Add custom sentence
            new_sentence = input("Enter a custom sentence: ").strip()
            if new_sentence:
                sentence_pools.setdefault("custom", []).append(new_sentence)
                print("Custom sentence added successfully!")
            else:
                print("Invalid sentence. Please try again.")

        elif choice in ["3", "view log file"]:
            # View log file
            if os.path.exists(log_file):
                print("\n***** LOG FILE *****")
                with open(log_file, "r") as file:
                    print(file.read())
            else:
                print("No log file found. Complete a test to create one.")

        elif choice in ["4", "view leaderboard"]:
            # View leaderboard
            display_leaderboard()

        elif choice in ["5", "view performance graph"]:
            # View performance graph
            plot_performance(log_file, user_name)

        elif choice in ["6", "exit"]:
            # Exit program
            print("Thank you for using the Typing Speed Test. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
