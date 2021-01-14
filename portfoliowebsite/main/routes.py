from flask import Blueprint, render_template, request, flash, redirect, url_for
from portfoliowebsite.main.forms import EmailForm
from portfoliowebsite.main.utils import send_reset_email

main = Blueprint('main', __name__)

@main.route("/", methods=['GET','POST'])
@main.route("/home", methods=['GET','POST'])
def home():
	form = EmailForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		message = form.message.data
		send_reset_email(name=name, email=email, message=message)
		flash('Your message has been sent!', 'success')
		return redirect(url_for('main.home', _anchor='contact'))
	return render_template('home.html', form=form)

@main.route("/education")
def education():
	return render_template('education.html', title="Education")

@main.route("/projects")
def projects():
	return render_template('projects.html', title="Projects")

@main.route("/experience")
def experience():
	return render_template('experience.html', title="Experience")

