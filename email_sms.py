import schedule, time
import email_sms_module as esm

# Schedule to send email every day at 9am CST. 
schedule.every().day.at('24:00').do(esm.send_text_message)


def main():
    """
    Main function that performs the following tasks:
    1. Checks for any pending scheduled tasks and executes them.
    2. Sleep every 60 seconds to optimize CPU usage.
    """
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()
