from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Job, core

def index(request):
    # Filter jobs that are published and whose deadline has not expired
    jobs = Job.objects.filter(status=core.BaseModel.PUBLISHED, deadline__gte=timezone.now())
    
    return render(request, 'job/index.html',
    {
        'jobs': jobs                  
    })
    
def detail(request, slug):
    # Get the jobs with the given slug, ensuring it's published and deadline not expired
    job = get_object_or_404(Job, slug=slug, status=core.BaseModel.PUBLISHED, deadline__gte=timezone.now())
    
    return render(request, 'job/detail.html', {
        'job': job
    })