from django.db import models
from django.utils import timezone

from apps.common.models import DefaultModel


def image_path(instance, filename):
    now = timezone.now()
    return f'{instance.user.id}/{now.year}/{now.month}/{now.day}/{filename}'


class ImageFace(DefaultModel):
    image = models.FileField()
