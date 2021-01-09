from flask_mail import Message
from portfoliowebsite import mail

def send_reset_email(name, email, message):
	msg = Message('New Portfolio Website Email!', sender='taylor.mcouat2@gmail.com', recipients=['taylor.mcouat@gmail.com'])
	msg.body = f'''Message contents: {message}

Name: {name}
Email: {email}
'''
	mail.send(msg)