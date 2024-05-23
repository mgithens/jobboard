from django.db import models

class BaseModel(models.Model):
    """
    Base model for all models
    """
    
    # CHOICES
    DRAFT = "DFT"
    PUBLISHED = "PUB"
    ARCHIVED = "ARC"
    
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (ARCHIVED, 'Archived'),
    ]
    
    DEFAULT_STATUS = DRAFT
    
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        