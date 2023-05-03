import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
# client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
client = WebClient(token="xoxb-xxxxxxxxxxx") # クレデンシャル情報は含めないこと
logger = logging.getLogger(__name__)
channel_name = "d4c-info-plan"
conversation_id = None
try:
    # Call the conversations.list method using the WebClient
    for result in client.conversations_list():
        if conversation_id is not None:
            break
        for channel in result["channels"]:
            if channel["name"] == channel_name:
                conversation_id = channel["id"]
                #Print result
                print(f"Found conversation ID: {conversation_id}")
                break

except SlackApiError as e:
    print(f"Error: {e}")
