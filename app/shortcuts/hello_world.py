from slack_bolt.async_app import AsyncAck
from slack_bolt.async_app import AsyncRespond
from slack_sdk.web.async_client import AsyncWebClient


async def hello_world_handler(
    ack: AsyncAck, respond: AsyncRespond, shortcut: dict, client: AsyncWebClient
):
    user = shortcut["user"]["id"]
    await client.chat_postMessage(channel=user, text="hiii")
