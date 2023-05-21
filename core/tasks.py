import os

from celery import shared_task
from slack_sdk import WebClient


@shared_task
def send_slack_message():
    # Initialize Slack client with your API token
    slack_token = os.getenv('SLACK_TOKEN')
    client = WebClient(token=slack_token)

    # Specify the channel and message to send
    channel = '#random'
    message = 'Hello World'

    try:
        # Send the message to Slack
        response = client.chat_postMessage(channel=channel, text=message)

        # Check if the message was sent successfully
        if response['ok']:
            return 'Message sent to Slack successfully'
        else:
            return f'Failed to send message to Slack: {response["error"]}'
    except Exception as e:
        return f'Error sending message to Slack: {str(e)}'