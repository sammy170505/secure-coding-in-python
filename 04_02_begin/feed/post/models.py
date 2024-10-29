from django.db import models

from uuid import uuid4

from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    @property
    def is_writer(self):
        return self.user.groups.filter(name='writer').exists()

