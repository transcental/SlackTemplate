from slack_bolt.async_app import AsyncApp

from app.actions.hello_world import hello_world_handler


ACTIONS = [
    {
        "id": "hello_world",
        "handler": hello_world_handler,
    },
]


def register_actions(app: AsyncApp):
    for action in ACTIONS:
        app.action(action["id"])(action["handler"])
