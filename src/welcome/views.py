from django.shortcuts import render

def home(request):
	return render(request, 'welcome/Boot.html')                                                                                                          

def about(request):
	return render(request, 'welcome/about.html', {'title':'About'})