# Typing Speed Test

A Python-based Typing Speed Test application designed to evaluate typing speed, accuracy, and errors. The project includes features like logging results, maintaining a leaderboard, visualizing performance graphs, and allowing custom sentence additions.

---

## Features

- **Typing Speed Test**: Measure your Words Per Minute (WPM), Characters Per Minute (CPM), typing accuracy, and errors.
- **Difficulty Levels**: Choose from *easy*, *medium*, and *hard* sentence pools.
- **Custom Sentences**: Add your personalized sentences to practice.
- **Leaderboard**: Displays the top 10 performers based on WPM.
- **Performance Graphs**: Track your typing progress with WPM and accuracy visualizations.
- **Log Results**: Save detailed test results for review.

---

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.6 or above**
- **Matplotlib library** for graph visualization

Install Matplotlib by running:
```bash
pip install matplotlib
```

---

## Getting Started

Follow these steps to get the application running:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/TanishGupta7/typing-speed-test.git
   ```
2. **Navigate to the Project Directory**
   ```bash
   cd typing-speed-test
   ```

3. **Run the Application**
   ```bash
   python typing_speed_test.py
   ```

4. **Choose an Option from the Menu**
   Use the main menu to start the test, view the leaderboard, or explore other features.

---

## Usage

### Main Menu Options
- **1. Start Typing Test**  
  Select difficulty (*easy*, *medium*, or *hard*), read the sentence, and start typing to evaluate your typing speed and accuracy.

- **2. Add Custom Sentence**  
  Add your custom sentences to the test pool.

- **3. View Log File**  
  View the results of previous tests, including WPM, accuracy, and errors.

- **4. View Leaderboard**  
  See the top 10 performers ranked by WPM.

- **5. View Performance Graph**  
  Visualize your WPM and accuracy trends over multiple tests.

- **6. Exit**  
  Exit the application.

---

## Example Workflow

### Starting a Typing Test:
```text
***** WELCOME TO THE TYPING SPEED TEST *****

Options:
1. Start Typing Test
2. Add Custom Sentence
3. View Log File
4. View Leaderboard
5. View Performance Graph
6. Exit

Enter your choice: 1

Choose difficulty level: Easy, Medium, Hard
Enter difficulty level: easy

Get ready to type the following sentence:
"The cat sat on the mat."

You have 5 seconds to read. The timer starts now!
...

***** TEST RESULTS *****
Words Per Minute (WPM): 45
Characters Per Minute (CPM): 230
Accuracy: 98.5%
Errors: 1
```

### Performance Graph:
Visualize your typing progress over time:
- **WPM**: Words Per Minute over multiple tests.
- **Accuracy**: Percentage of correct characters typed.

---

## File Structure

```plaintext
typing-speed-test/
├── typing_speed_test.py       # Main Python script
├── typing_speed_results.csv   # Log file (generated after first test)
├── leaderboard.csv            # Leaderboard data (generated after first test)
└── README.md                  # Documentation
```

---

## Logging and Leaderboard

### Logging
Test results are saved in `typing_speed_results.csv`:
```csv
User Name, WPM, CPM, Accuracy, Errors, Sentence
John, 45, 230, 98.5, 1, "The cat sat on the mat."
```

### Leaderboard
Displays the top 10 performers ranked by WPM. Data is stored in `leaderboard.csv`:
```csv
User Name, WPM
Alice, 65
Bob, 60
```

---

## Contributing

We welcome contributions! Feel free to fork the repository and submit pull requests to enhance the application. Suggestions and bug reports are also appreciated.

---

## Acknowledgments

- [Matplotlib](https://matplotlib.org/) for enabling performance graph visualizations.
- Inspired by the need to improve typing speed and accuracy.

---

## Contact

For any questions or suggestions, please feel free to reach out via GitHub.
