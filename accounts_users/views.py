from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import account_user
from .forms import UserUpdateForm

def createaccount (request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']
		
		if password == password2:
			if User.objects.filter(username=username).exists():
				messages.error(request,'Username is already taken')
				return redirect('createaccount')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request, 'Email is already in use')
					return redirect('createaccount')
				else:
					user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
					user.save()
					messages.success(request,'You are now registered')
					return redirect ('login')

		else:
			messages.error(request, 'Passwords do not match')
			return redirect ('createaccount')
	else:
		return render (request, 'accounts_users/createaccount.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect ('reservation')
		else:
			messages.error(request, 'Invalid credentials')
			return redirect ('login')


def editaccount(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)

		if u_form.is_valid():
			u_form.save()
			messages.success(request, 'Your account has been update')
			return redirect('editaccount')

	else:
		u_form = UserUpdateForm(instance=request.user)
  
	context = {
		'u_form': u_form
	}
 
	return render (request, 'accounts_users/editaccount.html', context)
