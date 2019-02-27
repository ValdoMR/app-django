from django.shortcuts import render, HttpResponse

def home(request):
	return render(request, 'core/pages/home.html')

def about(request):
	return render(request, 'core/pages/about.html')

def portafolio(request):
	return render(request, 'core/pages/portafolio.html')

def contact(request):
	return render(request, 'core/pages/contact.html')
