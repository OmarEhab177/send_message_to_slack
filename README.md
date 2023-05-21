# Send Message to Slack using Django, Celery, and Redis

This is a Django project that utilizes Celery and Redis to send a message to a channel on Slack every six hours. 

## Prerequisites

Before running this project, make sure you have the following installed:

- Python (version 3.6 or higher)
- Django (version 3.2 or higher)
- Celery (version 5.0 or higher)
- Redis (version 5.0 or higher)

## Setup

1. Clone the project repository from GitHub:

   ```
   git clone https://github.com/OmarEhab177/send_message_to_slack.git
   ```

2. Navigate to the project directory:

   ```
   cd send_message_to_slack
   ```

3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Create a new Slack app and generate an API token. Follow the official Slack documentation for instructions on how to create an app and obtain an API token.

5. Rename the `.env.example` file to `.env` and update the `SLACK_API_TOKEN` variable with your generated API token.

6. Configure Redis:
   
   - If Redis is running on the local machine with default settings, no additional configuration is required.
   - If Redis is running on a remote server or has custom settings, update the `CELERY_BROKER_URL` variable in the `.env` file with the appropriate Redis URL.

7. Run the migrations to create the required database tables:

   ```
   python manage.py migrate
   ```

## Usage

To send messages to a Slack channel every six hours, follow these steps:

- Start the Celery worker and scheduler:

   ```
   celery -A callslack worker --loglevel=info --beat
   ```

Congratulations! You have successfully set up and scheduled messages to be sent to a Slack channel using Django, Celery, and Redis.

Note: Make sure to keep the Celery worker and scheduler running for the messages to be sent at their scheduled times. and i am using the channel #random to send message on it if you want to change it got to core/tasks.py ln 14 and change it 
