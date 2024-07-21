# Smtp-Text-Messenger
 A Python-based project that securely sends emails using the SMTP protocol, leveraging environment variables managed by the dotenv library for configuration.

.env.example:

This file serves as a template for environment variables needed for the email sending functionality. Users should rename this file to .env and replace the placeholder values with their actual credentials.

email_sms.py:

This script schedules the sending of an email every day at 12 AM CST using the schedule library. It continuously checks for pending tasks and executes them.

email_sms_module.py:

This module contains the functionality to send an email via the SMTP protocol using environment variables for configuration. It loads environment variables, creates a connection to the Gmail SMTP server, logs in, composes a message, and sends it.


