from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
	return render_template('home.html')

@main.route("/education")
def education():
	return render_template('education.html', title="Education")

@main.route("/projects")
def projects():
	return render_template('projects.html', title="Projects")

@main.route("/experience")
def experience():
	return render_template('experience.html', title="Experience")

