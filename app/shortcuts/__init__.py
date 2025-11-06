from slack_bolt.async_app import AsyncApp

from app.shortcuts.hello_world import hello_world_handler


SHORTCUTS = [
    {
        "id": "hello_world",
        "handler": hello_world_handler,
    },
]


def register_shortcuts(app: AsyncApp):
    for shortcut in SHORTCUTS:
        app.shortcut(shortcut["id"])(shortcut["handler"])
