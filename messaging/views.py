from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola desde la aplicación de mensajería")
