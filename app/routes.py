# app/routes.py
from flask import render_template
from app.__init__ import app, db, api
from app.forms import ContactForm
from app.models import User
from flask_restful import Resource

@app.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Process the form data and add a user to the database
        user = User(username=form.name.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()

    users = User.query.all()
    return render_template('contact.html', form=form, users=users)

@app.route('/api/docs')
def api_docs():
    return render_template('api_docs.html')

class UserAPI(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'username': user.username, 'email': user.email}

api.add_resource(UserAPI, '/api/users/<int:user_id>')
