from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class TimedModel(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimedModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Link(TimedModel):
    url = models.URLField()
    name = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('link_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
