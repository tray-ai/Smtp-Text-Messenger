import smtplib, os, time
from dotenv import load_dotenv

# Load env variables into file. 
load_dotenv()

def send_text_message():
   """ This function sends a email/text 
   message via the SMTP protocol."""

   # Create the connection to gmail smtp server. 
   server = smtplib.SMTP('smtp.gmail.com', 587)

   # Create a secure connection / encryption
   server.starttls()

   # Initate variables for login creds for gmail.
   email = os.getenv('EMAIL')
   password = os.getenv('PASSWORD')

   try:
      # Attempt to login to Gmail.
      server.login(email, password)
   except smtplib.SMTPHeloError:
      print('The server did not respond properly.')
   except smtplib.SMTPNotSupportedError:
      print('The AUTH command is not supported by the server.')
   except smtplib.SMTPException:
      print('No suitable authentication method was found.')

   # Compose a message.
   msg = f'Hello World!'

   try:
      # Attempt to send the email/text message.
      server.sendmail(email, os.getenv('RECIPENT_EMAIL'), msg)
   except smtplib.SMTPHeloError:
      print('The server did not respond properly.')
   except smtplib.SMTPRecipientsRefused:
      print('All recipents were refused. Nobody got the mail.')
   except smtplib.SMTPDataError:
      print('The server replied with an unexpected error code.')

   # Send a notification to pushover that the message was sent.
   notification = (f'Message Sent Succesfully! - {time.strftime('%H:%M:%S')}.')
   server.sendmail(email, os.getenv('PUSHOVER_EMAIL'), notification)

   # Close the connection.
   server.quit()

