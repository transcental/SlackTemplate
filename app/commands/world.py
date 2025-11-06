from blockkit import Button
from blockkit import Confirm
from blockkit import Message
from blockkit import Section
from slack_bolt.async_app import AsyncAck
from slack_bolt.async_app import AsyncRespond
from slack_sdk.web.async_client import AsyncWebClient


async def world_handler(
    ack: AsyncAck,
    client: AsyncWebClient,
    respond: AsyncRespond,
    performer: str,
    channel: str,
    text="nothing",
):
    msg = (
        Message()
        .add_block(
            Section(f"<@{performer}> said {text}").accessory(
                Button("do something")
                .action_id("hello_world")
                .style(Button.PRIMARY)
                .confirm(
                    Confirm()
                    .title("you sure?")
                    .text("you can't undo something ya know")
                    .confirm("yep!")
                    .deny("on second thoughts...")
                )
            )
        )
        .build()
    )
    await client.chat_postMessage(channel=channel, **msg)
