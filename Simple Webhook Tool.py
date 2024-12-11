import requests
import time


def send_message(webhook_url, message, count, delay):
    # Loop through the number of times the message should be sent
    for i in range(count):
        data = {
            "content": message
        }

        try:
            # Send the request to the Discord webhook
            response = requests.post(webhook_url, json=data)

            # Check if the message was successfully sent
            if response.status_code == 204:
                print(f"Message {i + 1}/{count} sent successfully.")
            else:
                print(f"Failed to send message {i + 1}/{count}. Status Code: {response.status_code}")

        except Exception as e:
            print(f"Error sending message: {e}")

        # Wait for the specified delay before sending the next message
        if i < count - 1:
            time.sleep(delay)


def main():
    print("Welcome to the Discord Webhook Message Sender!")

    # Input: Webhook URL (You can get this from your Discord server settings)
    webhook_url = input("Enter your Discord Webhook URL: ")

    # Input: Message to be sent
    message = input("Enter the message to send: ")

    # Input: Number of times to send the message
    try:
        count = int(input("How many times do you want to send the message? "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Input: Delay in seconds between messages
    try:
        delay = float(input("Enter the delay (in seconds) between each message: "))
    except ValueError:
        print("Invalid input! Please enter a valid number for delay.")
        return

    # Send the messages
    send_message(webhook_url, message, count, delay)


if __name__ == "__main__":
    main()
