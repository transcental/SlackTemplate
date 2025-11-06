from slack_bolt.async_app import AsyncAck
from slack_bolt.async_app import AsyncRespond
from slack_sdk.web.async_client import AsyncWebClient

from app.views.hello_world import get_hello_world_view


async def hello_world_handler(
    ack: AsyncAck, respond: AsyncRespond, client: AsyncWebClient, body: dict
):
    await ack()
    channel_id = body["channel"]["id"]
    user_id = body["user"]
    trigger_id = body["trigger_id"]
    view = await get_hello_world_view(channel_id)
    await client.views_open(view=view, user=user_id, trigger_id=trigger_id)
