from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
	return render(request,'generator/home.html')

def about(request):
	return render(request,'generator/about.html')

def password(request):

	characters = list('abcdefghijklmnopqrstuvwxyz')

	length = int(request.GET.get('length', 12))

	if request.GET.get('Uppercase'):
		characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

	if request.GET.get('Numbers'):
		characters.extend(list("0123456789"))

	if request.GET.get('Special characters'):
		characters.extend(list("!@#$%^&*()"))


	thepassword = ''
	for x in range(length):
		thepassword +=random.choice(characters)

	return render(request,'generator/password.html', {'password': thepassword})#HttpResponse('Get what you want')