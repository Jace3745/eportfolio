from django.shortcuts import render

def aboutme(request):
    return render(request, "core/aboutme.html")

def screenprint(request):
    return render(request, "core/screenprint.html")

def blackbox(request):
    return render(request, "core/blackbox.html")

