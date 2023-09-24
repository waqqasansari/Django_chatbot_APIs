from django.db import models

from datetime import date
# from django.utils import timezone

class ChatMessage(models.Model):
    user_message = models.TextField()
    chatbot_response = models.TextField()
    timestamp = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.timestamp}: {self.user_message}'