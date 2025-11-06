from slack_bolt.async_app import AsyncSay
from slack_sdk.web.async_client import AsyncWebClient


async def message_handler(client: AsyncWebClient, say: AsyncSay, body: dict):
    event = body["event"]
    user = event["user"]
    text = event["text"]
    await say(f'<@{user}> said "{text}"')
