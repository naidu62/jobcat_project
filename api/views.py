from django.http import HttpResponse

def api_home(request):
    return HttpResponse("API is working ✅")
