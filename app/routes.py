from flask import render_template, flash, redirect, url_for, request
from flask_cors import CORS
from app import app
from os import environ, getcwd
import getpass

# getUser = lambda: environ["USERNAME"] if "C:" in getcwd() else environ["USER"]
# username = getUser()
username = getpass.getuser()


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Abhishek'}
    posts = [
        {
            'author': {'username': 'CESBot'},
            'body': 'I am here to help!'
        }
    ]
    return render_template('index.html', title='Home', user=username, posts=posts)


@app.route('/chatbot')
def chatbot():
    user = {'username': 'Abhishek'}
    return render_template('chatbot.html', title='Chatbot', user=username)
