from django.shortcuts import render, HttpResponse
import os

def home(request):
    database_name = os.getenv('MYSQL_DATABASE')
    return HttpResponse(database_name)

def	test(request):
	return HttpResponse("I hate this garbage project")