from django.conf import settings
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Spec.Status.PUBLISHED)
        )

class Spec(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    revision = models.CharField(max_length=50)
    description = models.TextField()
    publisher = models.CharField(max_length=50)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='spec_publish'
    )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-title']
        indexes = [
            models.Index(fields=['-title']),
        ]

    def __str__(self):
        return self.title
