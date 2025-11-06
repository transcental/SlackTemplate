from blockkit import Input
from blockkit import Modal
from blockkit import PlainTextInput
from blockkit import Section
from slack_bolt.async_app import AsyncAck
from slack_sdk.web.async_client import AsyncWebClient


async def get_hello_world_view(channel_id: str):
    modal = (
        Modal()
        .callback_id("hello_world")
        .title("Hewwo Wowld")
        .add_block(Section("wrrf ^-^"))
        .add_block(
            Input("Say something ig")
            .block_id("input")
            .element(PlainTextInput().placeholder("bark bark").action_id("input"))
        )
        .private_metadata(channel_id)
        .submit("Submit")
        .build()
    )
    return modal


async def hello_world_handler(ack: AsyncAck, client: AsyncWebClient, body: dict):
    await ack()
    user = body["user"]["id"]
    view = body["view"]
    input = view["state"]["values"]["input"]["input"]["value"]
    channel = view["private_metadata"]

    await client.chat_postMessage(channel=channel, text=f"<@{user}> said {input}!")
