from django.shortcuts import render

# Create your views here.
# khuluma/views.py

def chat(request):
    return render(request, 'chat.html')