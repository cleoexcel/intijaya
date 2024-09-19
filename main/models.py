import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    categories = models.CharField(max_length=255)

    def __str__(self):
        return self.name