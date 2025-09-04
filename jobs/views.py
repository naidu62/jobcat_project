from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects.all().order_by('-created_at')[:10]
    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/home.html', context)

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    context = {
        'job': job
    }
    return render(request, 'jobs/job_detail.html', context)

def search_results(request):
    query = request.GET.get('q')
    if query:
        jobs = Job.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        jobs = Job.objects.all().order_by('-created_at')
    context = {
        'jobs': jobs,
        'query': query
    }
    return render(request, 'jobs/home.html', context)
