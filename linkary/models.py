from django.db import models
from django.urls import reverse
# To use User as ForeignKey:
# from django.contrib.auth.models import User
# user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Link(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    url = models.URLField()
    name = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('link_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
