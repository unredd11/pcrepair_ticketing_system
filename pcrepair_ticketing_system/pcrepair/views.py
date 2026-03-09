from django.shortcuts import render

def home(request):
    return render(request, 'main.html')

def create_ticket(request):
    return render(request, 'create_ticket.html')
