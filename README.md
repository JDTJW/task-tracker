# Task Tracker (CLI)

A simple command-line task tracker built in Python. Add, view, remove, and mark tasks as done — all saved to a local file so your data persists between runs.

## Features

- **Add tasks** — create new tasks by name
- **View tasks** — see all tasks and their completion status
- **Remove tasks** — delete a task by name
- **Mark tasks done** — update a task's status
- **Persistent storage** — tasks are saved to `tasks.json` and automatically reloaded the next time the program runs

## How it works

Tasks are stored in memory as a list of dictionaries, e.g.:

```python
{"name": "Buy groceries", "done": False}
```

On startup, the program tries to load existing tasks from `tasks.json`. If the file doesn't exist yet (first run), it starts with an empty list instead of crashing.

On exit, the current task list is written back to `tasks.json` using Python's built-in `json` module, so nothing is lost between sessions.

## Running it

```bash
python tracker.py
```

You'll see a menu:

```
1. Add task
2. Show task
3. Remove task
4. Mark task done
5. Exit
```

Enter a number to choose an action, and follow the prompts.

## What I learned building this

This was my first real project after being stuck watching Python tutorials without retaining much. Building it from scratch (rather than following a tutorial) forced me to actually understand and debug:

- Lists and dictionaries as combined data structures
- Writing functions with parameters and return values, and using return values for success/failure feedback
- Loop + mutation bugs (modifying a list while iterating over it, and why `break`/`return` prevent that)
- Variable scope issues (e.g. referencing an undefined variable outside a function)
- File I/O and JSON serialization, plus handling the "file doesn't exist yet" edge case with `try`/`except`

## Possible future improvements

- Due dates and priority levels
- Sorting/filtering tasks (e.g. show only pending tasks)
- A web-based version (planned as a separate future project, once I've learned frontend/backend basics)
