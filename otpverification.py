import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to generate a 6-digit random OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send an email
def send_otp_email(user_email, otp):
    # Email server settings (use your own email provider's SMTP server)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'  # Replace with your email address
    sender_password = 'your_password'      # Replace with your email password

    # Create a MIME message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = user_email
    message['Subject'] = 'Your OTP Verification Code'

    # Add OTP as the email content
    body = f'Your OTP verification code is: {otp}'
    message.attach(MIMEText(body, 'plain'))

    # Connect to the email server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Use TLS
        server.login(sender_email, sender_password)  # Login to the email account
        server.sendmail(sender_email, user_email, message.as_string())  # Send the email

def main():
    # Generate a 6-digit random OTP
    otp = generate_otp()

    # Request the user's email address
    user_email = input('Enter your email address: ')

    # Send the OTP

    # Send the OTP to the user's email
    send_otp_email(user_email, otp)
    print('OTP has been sent to your email address.')

    # Prompt the user to enter the OTP received in their email
    user_otp = input('Enter the OTP you received in your email: ')

    # Verify the OTP
    if user_otp == otp:
        print('OTP verified successfully!')
    else:
        print('Invalid OTP. Verification failed.')

if __name__ == '__main__':
    main()

