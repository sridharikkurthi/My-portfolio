from flask import Flask, render_template, request, redirect, flash
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load environment variables from .env file
load_dotenv()

# Admin email
ADMIN_EMAIL = os.getenv('sridharikkurthi12@gmail.com')

# Email credentials
EMAIL_ADDRESS = os.getenv('sridharikkurthi12@gmail.com')
EMAIL_PASSWORD = os.getenv('Sridhar@49')

def save_contact_info(name, email, message):
    with open('contact_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, message])

def send_email_notification(name, email, message):
    try:
        # Email content
        subject = "New Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Setup MIME
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ADMIN_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, ADMIN_EMAIL, text)
        server.quit()
    except Exception as e:
        print(f"Failed to send email notification: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Save contact info
        save_contact_info(name, email, message)
        
        # Send email notification to admin
        send_email_notification(name, email, message)
        
        # Flash message to the user
        flash('Thank you for your message! I will get back to you soon.')
        return redirect('/')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
