from django.db import models
from slugify import slugify
from core.models import BaseModel

class Job(BaseModel):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    deadline = models.DateField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    status = models.CharField(
        max_length=10, 
        choices=BaseModel.STATUS_CHOICES, 
        default=BaseModel.DEFAULT_STATUS
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.company_name} {self.title}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name + ' / ' + self.title
    
    class Meta:
        ordering = ('created_on',)