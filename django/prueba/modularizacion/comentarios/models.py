from django.db import models

class comments(models.Model):

    name = models.CharField(max_length=50, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name

