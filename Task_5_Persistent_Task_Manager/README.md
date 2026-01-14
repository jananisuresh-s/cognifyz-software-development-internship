# Task 5 – Persistent CRUD Task Manager (File I/O)

## Overview
This project is an enhanced version of the CRUD console application
that supports **persistent storage** using file input/output.
Tasks are saved to and loaded from a text file, ensuring data is
retained even after the program exits.

## Features
- Create tasks with unique IDs
- View all stored tasks
- Update existing tasks
- Delete tasks
- Automatic saving to file after every change
- Automatic loading of tasks on application start
- Menu-driven console interface

## Technical Details
- Language: Python
- Storage: Text file (`tasks.txt`)
- Data Format: `task_id|title|description`
- Design Pattern: Object-Oriented Programming (OOP)

## Concepts Used
- File handling (read/write)
- Exception handling
- Classes and objects
- Lists and iteration
- Conditional statements and loops
- Data persistence

## How It Works
- On startup, the application checks for an existing `tasks.txt` file.
- If found, tasks are loaded into memory automatically.
- Any create, update, or delete operation immediately updates the file.
- Task IDs are managed dynamically to avoid duplication.

## How to Run
1. Ensure Python is installed on your system.
2. Open a terminal in this project folder.
3. Run the application using:

```bash
python task5_persistent_task_manager.py
