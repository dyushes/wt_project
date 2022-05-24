from django.shortcuts import render
from .models import JobVacancy


def index(request):
    return render(request, '../static/../templates/main/index.html')


def registration(request):
    return render(request, '../static/../templates/main/registration.php')


def login(request):
    return render(request, '../static/../templates/main/login.html')


def jobvacancy(request):
    job_vacancy = JobVacancy.objects.all()
    return render(request, '../static/../templates/main/jobvacancy.html', {'job_vacancy': job_vacancy})
