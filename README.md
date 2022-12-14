# New York City Guide - Django Project

### Decription
This project is designed to be a guide for the five boroughs of New York. Each borough has differnt activites, and each activity has different venues. All of the data shown is nested within one rather large dictionary that is available to view in the boroughs.py file.

## Project Colaborators:

Nikkole Hardy - https://github.com/NikkoleAshleigh
Erik Nava - https://github.com/ErickNavaP

## To start building the project:

Once the user has cloned the repo and dedicate the repo in its respective directory:

### 1. Create a virtual environment

At the root folder of the repository run:
```
python3 -m venv venv
```
Make sure to call your virtual environment "venv"

### 2. Run virtual environment
#### On Windows:
Windows Powershell users:
```
venv\Scripts\activate.bat
```
Bash users:
```
source venv/Scripts/activate
```
#### On Unix or MacOS:
```
source venv/bin/activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run Django
```
python manage.py runserver
```
And go to `http://localhost:8000`

Enjoy the site!
