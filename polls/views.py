# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. 960ece0c is the polls index.")
