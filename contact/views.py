from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import asyncio

# Create your views here.


def send_email(email, message, name):
	try:
		send_mail(
			'New Contact',
		     "Message from Contact: " + " Name: "+name +" EMail: " + email +" Message: "+ message,
		    'boxingstudiogames237@gmail.com',
		    ['codeMedia32@gmail.com','seanDp32@gmail.com'],
		    fail_silently=False,
		    )
	except Exception as e:
		print("error")
		print(e)



@csrf_exempt
def handle_contact(request):
	print(request.POST)
	name 		= request.POST.get("ajax_name", "")
	email 		= request.POST.get("ajax_email", "")
	phone 	 	= request.POST.get("ajax_subject", "")
	message  	= request.POST.get("ajax_message", "")
	# print(name)
	# print(email)
	# print(message)
	send_email(email, message, name)
	return  HttpResponse("")