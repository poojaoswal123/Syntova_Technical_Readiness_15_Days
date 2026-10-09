# DAY 12: GIT PRACTICE
# Git helps you track these changes. Think of it as a history book for your code.
# Git: Tracks changes to your code on your computer.
# GitHub: Stores your code online so you can share it and collaborate with others.
# mkdir = make directory (create a folder).
# git-day12-practice = the folder's name.
# cd means change directory — it moves your terminal into that folder.
# git init : Start tracking the project in this folder.
# git status : What is happening in my project right now?
# git diff : It shows the differences between your last commit and your current file.
# git switch — change branches.
# -c — create a new branch.
# git branch A branch lets you work on a separate line of development without immediately changing the main branch.

# DAY 12: GIT & PULL REQUEST WORKFLOW
# Goal: Create a branch, commit changes, push to GitHub, and create a Pull Request.
# Run terminal commands in the VS Code terminal, not inside this Python file.

# STEP 1: Check Git and repository status
# git --version
# git status
# git branch

# STEP 2: Create and switch to a feature branch
# Run only if you are currently on main and your working tree is clean:
# git switch -c feature/hello-message

# STEP 3: Update hello.py with this code and save it
print("Hello Git")
print("Learning version control")
print("I am learning Git step by step")
print("Practicing branches and pull requests")

# STEP 4: Run the Python file in the terminal
# python hello.py

# STEP 5: Review, stage, and commit your changes
# git status
# git diff
# git add hello.py
# git commit -m "Add feature branch message"

# STEP 6: Push the feature branch to GitHub
# git push -u origin feature/hello-message

# STEP 7: On GitHub, create a Pull Request
# Base branch: main
# Compare branch: feature/hello-message
# Title: Add feature branch message
# Review the changes and click Merge pull request.

# STEP 8: Update your local main branch after the PR is merged
# git switch main
# git pull origin main

# STEP 9: Verify the final result
# python hello.py
# git log --oneline --graph --all
# git status

# EXPECTED OUTPUT:
# Hello Git
# Learning version control
# I am learning Git step by step
# Practicing branches and pull requests

# IMPORTANT:
# If feature/hello-message already exists, use:
# git switch feature/hello-message
# If Git reports uncommitted changes or a merge conflict, stop and resolve
# that state before proceeding. Do not force-push.

# main = your original, stable assignment.
# feature/hello-message = a separate copy where you add something new.
# commit = saving a named checkpoint of your work.
# push = uploading your branch to GitHub.
# Pull Request = asking to include your changes in the main assignment.
# merge = combining your changes into main.
# pull = downloading the latest changes from GitHub to your computer.