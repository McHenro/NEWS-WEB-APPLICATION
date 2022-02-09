from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime

from celery import Celery
from .views import object_list
from .models import News
from django.db import IntegrityError


@shared_task(name="update_db_with_new_data")
def update_db():
    data = object_list()
    for item in data:
        try:
            News.objects.create(
                author=item.get("by", ""),
                score=item.get("score", 0),
                title=item.get("title", ""),
                url=item.get("url", ""),
                type=item.get("type", ""),
                text=item.get("text", ""),
            )
        except IntegrityError as e:
            if "unique constraint" in str(e.args):
                continue
