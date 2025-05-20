# To-Do List Application Project - Development Plan

## Project Overview
This project involves building a basic command-line interface (CLI) To-Do List application. Users will be able to add, view, mark complete, and delete tasks. All tasks will be saved to and loaded from a file, ensuring persistence between application runs.

**Difficulty:** Easy
**Core Focus:** Python fundamentals, file I/O, user interaction, foundational software engineering practices.

---

## Part 1: Functional Requirements (What it needs to do)

Your application must implement the following features:

### 1. Task Representation
- Each individual to-do task must store:
    - A **description** (string, e.g., "Buy groceries").
    - A **completion status** (boolean, `True` for complete, `False` for incomplete).

### 2. Add Task
- Allow users to add new tasks.
- Prompt the user for the task description.
- New tasks must always be initialized as **incomplete**.

### 3. View Tasks
- Display all tasks currently in the list.
- Each task should be presented with a clear indicator of its status:
    - `[ ]` for incomplete tasks.
    - `[X]` for complete tasks.
- Tasks should be numbered sequentially starting from 1 for easy reference by the user.
    - Example: `1. [ ] Buy groceries`

### 4. Mark Task Complete
- Allow users to change the status of an incomplete task to complete.
- Prompt the user for the number corresponding to the task they wish to mark complete.
- Implement robust input validation:
    - Handle cases where the input is not a number.
    - Handle cases where the task number is out of the valid range.

### 5. Delete Task
- Allow users to remove a task from the list.
- Prompt the user for the number corresponding to the task they wish to delete.
- Implement robust input validation (similar to 'Mark Task Complete').

### 6. Persistent Storage
- **Load Tasks:** When the application starts, it must attempt to load existing tasks from a designated file.
    - If the file does not exist, the application should start with an empty list of tasks.
    - If the file exists, it should correctly parse the data and populate the task list.
- **Save Tasks:** Before the application exits gracefully, it must save all current tasks to the same designated file.
- **File Format:** You decide on a simple file format (e.g., plain text file, one task per line, with a convention to indicate completion status).

### 7. User Interface (CLI)
- The application must run in a command-line environment.
- Present a clear, interactive menu to the user with options for all functionalities (Add, View, Mark Complete, Delete, Exit).
- Accept user input to select menu options and provide necessary details for chosen actions.
- Gracefully handle invalid menu choices.

### 8. Exit Application
- Provide an option for the user to exit the application.
- Ensure all tasks are properly saved to the file before exiting.

---

## Part 2: Best Practices & Professional Habits (How to build it)

These are crucial for leveling up your skills and making your project portfolio-ready.

### 1. Version Control (Git & GitHub)
- **Initialize a Git Repository:** Start every project by running `git init` in your project directory.
- **Meaningful Commits:** Make small, logical commits with clear commit messages.
    - Example: `git commit -m "feat: Implement add_task function"`
- **`.gitignore` File:** Create a `.gitignore` file to prevent unnecessary files (like virtual environment folders, `__pycache__`) from being committed. At minimum, include `.venv/` and `__pycache__/`.
- **Remote Repository (GitHub):** Create a new public repository on GitHub and link your local project to it. Push your changes regularly. This creates your public portfolio.

### 2. Virtual Environments (`venv`)
- **Create a Virtual Environment:** Use `python -m venv .venv` at the start of your project.
- **Activate & Use:** Always activate your virtual environment before installing packages or running your code.
    - Linux/macOS: `source .venv/bin/activate`
    - Windows: `.\.venv\Scripts\activate`
- **`requirements.txt`:** Generate a `requirements.txt` file (`pip freeze > requirements.txt`) to list project dependencies (if any external libraries are used).

### 3. Code Quality & Style
- **PEP 8 Compliance:** Adhere to Python's official style guide (e.g., 4-space indentation, consistent naming conventions, clear spacing). Use a linter (like `flake8` or `Pylint`) in your IDE to check automatically.
- **Type Hinting:** Use type hints for function parameters and return values (e.g., `def add_task(tasks: list[dict], description: str) -> None:`). This improves readability and helps catch errors.
- **Docstrings & Comments:** Write clear docstrings for functions/classes explaining their purpose, arguments, and return values. Use inline comments for complex logic.
- **Modularity:** Organize your code into functions, and potentially separate files if the project grows (e.g., `task_manager.py`, `file_handler.py`).

### 4. Testing (`pytest` recommended)
- **Install `pytest`:** `pip install pytest`
- **Write Unit Tests:** For each core function (e.g., `add_task`, `view_tasks`, `mark_task_complete`, `delete_task`, `load_tasks`, `save_tasks`), write at least one unit test to verify its correct behavior.
- **Test File Naming:** Name your test files starting with `test_` (e.g., `test_todo_app.py`).
- **Run Tests:** Use the `pytest` command in your terminal.

### 5. Project Structure
- Create a clear directory structure. A simple one might be:
    ```
    my_todo_app/
    ├── .venv/
    ├── .git/
    ├── .gitignore
    ├── main.py        # Your main application logic
    ├── tasks.txt      # (or whatever your data file is)
    ├── README.md      # Project description, how to run, etc.
    └── test_todo_app.py # Your test file(s)
    ```

### 6. `README.md` File
- **Compelling Description:** What does your app do? Why is it useful?
- **Features List:** Bullet points for all functionalities.
- **How to Run:** Clear steps for someone to set up the environment and run your app.
- **Technologies Used:** List Python and any libraries (even `os` or `json` if used).
- **Design Decisions (Optional):** Briefly explain any key choices you made (e.g., "I chose a plain text file for simplicity at this stage").
- **Future Enhancements (Optional):** What features could be added later? (e.g., task priorities, searching, GUI).

---

## Part 3: LeetCode Problems for Skill Reinforcement

These problems are chosen to align with the core algorithmic thinking needed for list manipulation, searching, and managing state in your To-Do List. Solve these on LeetCode as you encounter related concepts in your project.

### 1. [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- **Relevance to Project:** While your To-Do list doesn't parse parentheses, this problem is excellent for developing your ability to:
    - Process sequential input.
    - Use a stack-like behavior (e.g., for matching open/close symbols).
    - Implement robust validation logic based on sequence and state. This thinking applies directly to validating user input for task numbers and menu choices.

### 2. [1. Two Sum](https://leetcode.com/problems/two-two-sum/)
- **Relevance to Project:** This classic problem introduces the concept of using hash maps (Python dictionaries) for efficient lookups.
    - **How it applies:** In your To-Do list, if you were to add a feature to search for a task by keyword, or perhaps manage task IDs more explicitly, the efficiency principles from "Two Sum" (avoiding nested loops for lookups) would be very relevant.

### 3. [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- **Relevance to Project:** This problem focuses on efficiently modifying arrays/lists in-place and handling unique elements.
    - **How it applies:** If you ever wanted to ensure unique task descriptions, or if your delete function involved a specific kind of internal list restructuring, the techniques for efficiently manipulating list elements from this problem would be useful.

---

**Your First Step (again, but with the full context):**

1.  **Set up your project directory.**
2.  **Initialize Git and create your `.gitignore` and `README.md` files.**
3.  **Create and activate your virtual environment.**
4.  **Decide on your `Task Representation` (Requirement 1).** How will you structure a single task (e.g., using a `dict` like `{'description': '...', 'completed': False}` or a simple class)?

Once you've decided on the task structure, share it, and we can proceed to implementing the `add_task` function, keeping all these best practices in mind!
