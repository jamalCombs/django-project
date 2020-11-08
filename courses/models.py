from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=150)
    summary = models.TextField()

    def __str__(self):
        return self.title