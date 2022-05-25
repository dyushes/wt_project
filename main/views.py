from .models import JobVacancy
from django.shortcuts import render
from .forms import RegisterUserForm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, '../static/../templates/main/index.html')


def registration(request):
    return render(request, '../static/../templates/main/registr.html')


def login(request):
    return render(request, '../static/../templates/main/login.html')


def jobvacancy(request):
    job_vacancy = JobVacancy.objects.all()
    return render(request, '../static/../templates/main/jobvacancy.html', {'job_vacancy': job_vacancy})


# Функция регистрации
def registr(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = RegisterUserForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'main/login.html', data)
    else: # Иначе
        # Создаём форму
        form = RegisterUserForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'main/registr.html', data)

