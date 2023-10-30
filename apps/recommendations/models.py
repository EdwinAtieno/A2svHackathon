from django.db import models
from django.conf import settings

class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    html_content = models.TextField()

    def __str__(self):
        return f"Recommendation {self.pk}"
