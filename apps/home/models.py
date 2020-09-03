from django.db import models

class Test(models.Model):
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title