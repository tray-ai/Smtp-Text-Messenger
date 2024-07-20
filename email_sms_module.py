import smtplib, os
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


   # Login to Gmail
   server.login(email, password)


   # Compose a message.
   msg = f'Hello World!'

   # Send the email/text message.
   server.sendmail(email, os.getenv('RECIPENT_EMAIL'), msg)

   # Close the connection.
   server.quit()


   print('Message Sent Succesfully!')
