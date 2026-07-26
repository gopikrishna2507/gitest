# Git Basics & Python Demo Project

Welcome to your Git practice repository! This project serves as a hands-on guide for learning core **Git version control concepts** using simple **Python scripts**.

## 📌 Project Structure

```text
gitdemo/
│── .gitignore          # Tells Git which files/directories to ignore (e.g. __pycache__)
│── README.md           # Project documentation and guide
│── calculator.py       # Math functions module (add, subtract, multiply, divide)
│── main.py             # Entry point script calling calculator functions
└── test_calculator.py  # Unit tests verifying calculator module correctness
```

## 🚀 Git Core Workflow Overview

1. **Working Directory**: The actual files on your computer.
2. **Staging Area (Index)**: The preparation area where files are prepared (`git add`) before committing.
3. **Local Repository**: The `.git` folder on your machine containing commit history (`git commit`).
4. **Remote Repository**: Host repository on GitHub (`git push` / `git pull`).

---

## 🛠 Basic Git Commands Cheatsheet

### 1. Repository Setup & Status
- Check status of tracked/untracked files:
  ```bash
  git status
  ```
- View commit history:
  ```bash
  git log --oneline
  ```

### 2. Staging & Committing
- Stage specific file or all files:
  ```bash
  git add main.py
  git add .
  ```
- Commit staged changes with a message:
  ```bash
  git commit -m "Add main execution script"
  ```

### 3. Branching & Merging
- Create and switch to a new branch:
  ```bash
  git checkout -b feature/advanced-math
  ```
- Switch back to `main` branch:
  ```bash
  git checkout main
  ```
- Merge branch changes into `main`:
  ```bash
  git merge feature/advanced-math
  ```

### 4. GitHub Remote Integration
- Push your local `main` branch to GitHub:
  ```bash
  git push -u origin main
  ```
