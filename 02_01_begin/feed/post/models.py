from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def is_writer(self):
        return self.user.groups.filter(name="writer").exists()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    text = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.created}: id {self.pk}"
