from slack_bolt.async_app import AsyncApp

from app.events.message import message_handler


EVENTS = [
    {
        "name": "message",
        "handler": message_handler,
    },
]


def register_events(app: AsyncApp):
    for event in EVENTS:
        app.event(event["name"])(event["handler"])
