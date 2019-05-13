from django.db import models


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)


class Subject(models.Model):
    name = models.CharField(max_length=30)


class Textbook(models.Model):
    title = models.CharField(max_length=30)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Professor)
