from django.conf import settings
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Spec.Status.PUBLISHED)
        )


class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


class Spec(models.Model):
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
        verbose_name_plural = 'specification'

    def __str__(self):
        return self.title


class Classification(models.Model):
    spec = models.ForeignKey(
        Spec,
        on_delete=models.CASCADE,
        related_name='spec_classification'
    )
    classification = models.CharField(max_length=200, default='N/A', help_text='Combination of methods, types, and classes. Use only one per process')
    description = models.TextField(blank=True, help_text='description of method, type, or class')
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
        related_name='classification_publish'
    )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['spec']
        indexes = [models.Index(fields=['spec']),]
        verbose_name_plural = 'classification'
        
    def __str__(self):
        return f"{self.spec.title} - ({self.classification})"


class Quality(models.Model):
    class Method(models.TextChoices):
        ACCEPTANCE_TEST = 'LI', 'Lot Inspection'
        PERIODIC_TEST = 'PT', 'Periodic Test'
        PREPRODUCTION_TEST = 'PRE', 'Preproduction Test'

    class Sample(models.TextChoices):
        PART = 'P', 'Part'
        PANEL = 'PL', 'Panel'

    spec = models.ForeignKey(
        Spec,
        on_delete=models.CASCADE,
        related_name='spec_quality'
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    methods = models.CharField(
        max_length=3,
        choices=Method,
    )
    sample = models.CharField(
        max_length=3,
        choices=Sample,
        default=Sample.PANEL
    )
    test_spec = models.CharField(max_length=50)
    description = models.TextField()
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
        related_name='quality_publish'
    )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name_plural = 'quality requirements'
        
    def __str__(self):
        return self.name

    
class ProcessRequired(models.Model):
    class Identity(models.TextChoices):
        CHROME = 'CR', 'Chrome Plate'
        NICKEL = 'NI', 'Nickel Plate'
        CADMIUM = 'CD', 'Cadmium Plate'
        ANODIZE = 'AN', 'Anodize'
        CONVISION = 'CF', 'Chemical Converision'
        PASSIVATION = 'PA', 'Passivation'
        STRIP = 'ST', 'Coating Strip'
        BRUSH = 'BR', 'Brush Plate'
        PREPEN = 'PR', 'Prepen Etch'
        TEMPERETCH = 'TE', 'Temper Etch'

    classification = models.ForeignKey(
        Classification,
        on_delete=models.CASCADE,
        related_name='process_class'
    )
    step = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    process_identity = models.CharField(
        max_length=50,
        choices=Identity,
        default='N/A'
    )
    description = models.TextField()

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
        related_name='process_publish'
    )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['title']
        indexes = [models.Index(fields=['title']),]
        verbose_name_plural = 'Process Method'
        
    def __str__(self):
        return self.title   
    

class Solution(models.Model):
    tank_identification = models.CharField(max_length=50)
    tank_contents = models.CharField(max_length=200, help_text='Chemical Contents')
    temp_range = models.CharField(max_length=100, default='Ambient', help_text="Temperature in F")
    time_min = models.CharField(max_length=50, help_text="Mininum Soak Time (minutes)")
    time_max = models.CharField(max_length=50, help_text="Maximum Soak Time (minutes)")
    tank_requirement = models.TextField()
    is_rectified = models.BooleanField(default=False)

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
        related_name='tank_publish'
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['tank_identification']
        indexes = [models.Index(fields=['tank_identification']),]
        verbose_name_plural = 'Tank Process'
        
    def __str__(self):
        return self.tank_identification


class Manual(models.Model):
    manual_title = models.CharField(max_length=50)
    manual_description = models.TextField(help_text='Small description of task to be performed')

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
        related_name='manual_publish'
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['manual_title']
        indexes = [models.Index(fields=['manual_title']),]
        verbose_name_plural = 'Manual Process'
        
    def __str__(self):
        return self.manual_title