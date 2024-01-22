#Branch Messaging APP#

##Dependencies##
Create and activate a virtual environment to isolate your project dependencies
python -m venv venv
source venv/bin/activate  # On macOS/Linux
.\venv\Scripts\activate   # On Windows

Install Flask within your virtual environment.
pip install flask

Install SQLAlchemy and Flask
pip install Flask Flask-SQLAlchemy

Install Flask-RESTful
pip install Flask-RESTful


##Files##
app/routes.py - defines the app's routes and views.
app/forms.py - defines form actions
app/models.py - defines the app's data and database
run.py - execution file

To run the app:
python run.py

Visit http://127.0.0.1:5000/ in your web browser to see your Flask app.

#Authors#
[Emmaculate Sintoya](https://github.com/lsintoya)
