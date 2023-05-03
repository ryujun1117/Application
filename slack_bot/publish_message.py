# Publishing your message

import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
# client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
client = WebClient(token="xoxb-2113692898917-5215545494849-tmSAaQz3znfF9cfzxQ6AGrKg")
logger = logging.getLogger(__name__)
# ID of channel you want to post message to
channel_id = "C0256845ALA"

try:
    # Call the conversations.list method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id,
        text="Hello world!"
        # You could also use a blocks[] array to send richer content
    )
    # Print result, which includes information about the message (like TS)
    print(result)

except SlackApiError as e:
    print(f"Error: {e}")