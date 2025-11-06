from slack_bolt.async_app import AsyncApp

from app.views.hello_world import hello_world_handler


VIEWS = [
    {
        "id": "hello_world",
        "handler": hello_world_handler,
    },
]


def register_views(app: AsyncApp):
    for view in VIEWS:
        app.view(view["id"])(view["handler"])
