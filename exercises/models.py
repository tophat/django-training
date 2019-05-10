from django.db import models


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Textbook(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Professor, on_delete=models.CASCADE)

