from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime
from .models import BaseModel, Job
from applicant.forms import ApplicantForm


def index(request):
    # Filter jobs that are published and whose deadline has not expired
    jobs = Job.objects.filter(status=BaseModel.PUBLISHED, deadline__gte=timezone.now())
    
    return render(request, 'job/index.html',
    {
        'jobs': jobs                  
    })
    
    
def detail(request, slug):
    # Get the jobs with the given slug, ensuring it's published and deadline not expired
    job = get_object_or_404(Job, slug=slug, status=BaseModel.PUBLISHED, deadline__gte=timezone.now())
    
    if job.deadline >= datetime.now().date():
        if request.method == 'POST':
            form = ApplicantForm(request.POST, request.FILES)
            if form.is_valid():
                applicant = form.save(commit=False)
                applicant.job = job  # Associate the job with the application
                applicant.save()
                # Return a JSON response for AJAX
                return JsonResponse({'success': True})
            else:
                # Return a JSON response with form errors
                return JsonResponse({'success': False, 'error': form.errors.as_json()})
        else:
            form = ApplicantForm()
    else:
        form = None

    return render(request, 'job/detail.html', {
        'job': job,
        'form': form, 
    })