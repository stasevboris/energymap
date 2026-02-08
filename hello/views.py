from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Привет, мир!</h1><p>Это тестовая страница EnergyMap в Docker.</p>")