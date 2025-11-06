from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.config import config
from app.tasks.task import task


def register_tasks():
    scheduler = AsyncIOScheduler(timezone=config.timezone)
    scheduler.add_job(
        task,
        "interval",
        minutes=1,
        max_instances=1,
        next_run_time=datetime.now(),
    )

    scheduler.start()
