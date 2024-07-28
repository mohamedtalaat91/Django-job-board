from django.db import models

# Create your models here.
JOB_TYPE_CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100,choices=JOB_TYPE_CHOICES)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)