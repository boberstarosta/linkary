from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class TimedModel(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimedModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})

    def latest_links(self):
        result = self.link_set.order_by('-time_modified')[:10]
        return result

    def __str__(self):
        return self.name


class Link(TimedModel):
    url = models.URLField()
    name = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        get_latest_by = ['time_created']
        ordering = ['-time_modified']

    def get_absolute_url(self):
        return reverse('link_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
