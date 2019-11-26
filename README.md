System Requirements
-----------------------------------------
$ python --version
Python 3.7.4

$ pip install django_mysql

Development Environment Setup
-----------------------------------------
1. Create the project Directory
---------------------------------------
	mkdir MCQProject
2. Change to the newly created directory
---------------------------------------
	cd MCQProject
3. Prepare for virtual environment
---------------------------------------
	pip install virtualenv
4. Create Virtual Environment
---------------------------------------
	virtualenv virtualenv
5. Install Django in virtual environment
---------------------------------------
	pip install django
6. Start new project
---------------------------------------
	django-admin.py startproject mcq_app
7. Change to mcq_app Directory
---------------------------------------
	cd mcq_app
8. Make Migrations (For Database. Default SQLite and Can be changed from mcq_app/settings.py)
---------------------------------------
	python manage.py migrate
9. Try running the app to check if setup till now is correct.
---------------------------------------
	python manage.py runserver
