import json
import requests
from time import sleep
from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def test():
    logger.info('Spinning task in celery')
    sleep(5)
    requests.put('http://localhost:8000/api/handle_tasks', data = json.dumps({"message":"hello"}))
