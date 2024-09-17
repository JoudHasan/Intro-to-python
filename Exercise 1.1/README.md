# Exercise 1.1: Getting Started with Python

## Overview

In this exercise, I learned how to install Python, set up a virtual environment, write a basic Python script, and manage packages using a `requirements.txt` file. Additionally, I created a GitHub repository to organize the deliverables for this course.

## Steps

### 1. Install Python 3.8.7

- Installed Python 3.8.7 on my system.
- Verified the installation by running:

  python3 --version
  Python 3.8.7

### 2. Set Up a Virtual Environment

- Created a virtual environment named cf-python-base using virtualenvwrapper:

mkvirtualenv cf-python-base

- Activated the virtual environment:

workon cf-python-base

### 3. Write a Python Script (Hello.py)

print("Hello World!")

### 4. Set Up an IPython Shell

- Installed ipython in the virtual environment:
  pip install ipython
- Launched the IPython shell to take advantage of syntax highlighting, auto-indentation, and other features:

ipython

### 5. Generate a requirements.txt File

- Exported a list of installed packages to a requirements.txt file using the pip freeze command:
  pip freeze > requirements.txt

### 6. Create a New Virtual Environment

Created a new virtual environment called cf-python-copy and installed packages from the previously generated requirements.txt file:

mkvirtualenv cf-python-copy
pip install -r requirements.txt

### 7. Create a GitHub Repository

https://github.com/JoudHasan/Intro-to-python.git
