from django.db import models
from django.utils import timezone
from core.models import BaseModel
from job.models import Job


class Applicant(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)