from app import app
from flask import render_template

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
