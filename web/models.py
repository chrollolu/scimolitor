from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='media/post/%Y/%m/%d/', blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    # Model Manager
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']), ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('web:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])



class Bien(models.Model):

    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to='media/post/%Y/%m/%d/', blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']), ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('web:bien_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


class Employe(models.Model):
    titre = models.CharField(max_length=10)
    nom = models.CharField(max_length=250)
    fonction = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    linkedin = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='media/employe/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'{self.nom} {self.prenoms}'