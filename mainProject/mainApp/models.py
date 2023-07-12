from django.db import models


# Create your models here.
class Comment(models.Model):
    comment = models.TextField(null=True)

    def __str__(self):
        return f'{self.comment}'
