from django.contrib.auth.models import User
from django.db import models

from telegram_registration.settings import MEDIA_ROOT


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_account")
    telegram_id = models.IntegerField(unique=True)
    photo_url = models.FilePathField(path=MEDIA_ROOT, null=True, blank=True)

    def __str__(self):
        return self.user.username

