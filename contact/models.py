from unittest.mock import Base
from django.db import models
from helpers.models import BaseModel
# Create your models here.


class Cantact(BaseModel):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)

    description = models.TextField()