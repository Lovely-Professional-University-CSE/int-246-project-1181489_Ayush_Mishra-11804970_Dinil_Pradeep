from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request, 'accounts/main.html')

def project(request):
	return render(request,'accounts/int246_project.html')
