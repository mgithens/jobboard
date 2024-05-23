from django.db import models
from core import models as core
from slugify import slugify

class Job(core.BaseModel):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    deadline = models.DateField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    status = models.CharField(
        max_length=10, 
        choices=core.BaseModel.STATUS_CHOICES, 
        default=core.BaseModel.DEFAULT_STATUS
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.company_name} {self.title}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title