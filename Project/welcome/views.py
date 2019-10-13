from django.shortcuts import render
import logging
def home(request):
	#logging.debug("DEBUG")
	return render(request, 'welcome/Boot.html')                                                                                                          

def about(request):
	return render(request, 'welcome/about.html', {'title':'About'})