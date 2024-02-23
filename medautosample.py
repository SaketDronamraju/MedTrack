import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time

def send_email(subject, body, recipients):
    # Email configuration
    sender_email = ''  # Replace with your email
    password = ''  # Replace with your email password that you get after creating your unique key

    # Email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    # Send email to each recipient
    for recipient in recipients:
        message['To'] = recipient
        server.sendmail(sender_email, recipient, message.as_string())
        print(f"Email sent to {recipient}")

    # Close the SMTP connection
    server.quit()

def main():
    # Set the email details
    subject = " Reminder for restocking medicines "
    body = "Hope you are doing well ,this a friendly reminder to make sure you are fully stocked up with all your medications.Have a good day"
    recipients = [
        'recpient@gmail.com',
        'recpient2@gmail.com'
        ]

    # Calculate the time to send the email (every Friday at 7:20 AM)
    now = datetime.datetime.now()
    friday = (now + datetime.timedelta((4 - now.weekday()) % 7)).replace(hour=7, minute=20, second=0)

    # Schedule the email
    while True:
        if datetime.datetime.now() >= friday:
            # Send the email
            send_email(subject, body, recipients)
            break
        else:
            # Wait for a minute and check again
            time.sleep(60)

if __name__ == "__main__":
    main()


