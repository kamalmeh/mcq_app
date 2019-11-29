System Requirements
-----------------------------------------
App is developed using Python 3.7.4

You can experiment any python version to check if it's working.

$ pip install django_mysql

$ pip install django-tables2

Setup
-----------------------------------------
1. Clone the repository using git clone
---------------------------------------
	git clone https://github.com/kamalmeh/mcq_app.git

2. Change Directory to mcq_app
---------------------------------------
	cd mcq_app

3. In windows git-bash or linux bash, execute below to activate virtual environment
---------------------------------------
	Windows
	-----------
	virtualenv/Scripts/activate.bat
	
	Git-Bash
	-----------
	source ./virtualenv/Scripts/activate	

	Linux
	-----------
	source ./virtualenv/Scripts/activate

4. Change directory to mcq_app(directory with same name)
---------------------------------------
	cd mcq_app/

5. Run the web app using below server
---------------------------------------
	python manage.py runserver
