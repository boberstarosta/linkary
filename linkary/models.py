from django.db import models
# To use User as ForeignKey:
# from django.contrib.auth.models import User
# user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Link(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=500)
