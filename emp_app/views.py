from django.shortcuts import render, HttpResponse, redirect
from emp_app.models import Employee, Role, Department, Contact
from datetime import datetime
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request,'index.html')

def aboutus(request):
	return render(request,'aboutus.html')

def login(request):
	return render(request, 'login.html')
def loggedIn(request):
	return render(request, 'afterlogin.html')
def afterlogin(request):
	if request.method == "POST":
		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']
		print(loginpassword)
		print(loginusername)

		user = authenticate(request,username = loginusername, password = loginpassword)
		print("user-------",user)
		if user is not None:
			login(user)
			messages.success(request, "Successfully Logged In")
			return redirect('/loggedIn')		
		else:
			messages.error(request, "Invalid Credentials, Please Try Again.")
			return redirect('/login')


def logout(request):
	return HttpResponse('logout.html')

def signin(request):
	return render(request,'signin.html')

def register(request):
	return render(request, 'register.html')



def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']		
		content = request.POST['content']
		print(name, email, phone, content)
		
		if len(name)<2 or len(email)<8 or len(phone)<10 or len(content)<20:
			messages.error(request, "Please fill the form correctly!!!")
		else:
			contact = Contact(name=name, email=email, phone=phone, content=content )
			contact.save()
			messages.success(request, "Your message has been sucessfully sent")
	return render(request, 'contact.html')  


def all_emp(request):
	emps = Employee.objects.all()
	context = {
		'emps':emps
			}
	print(context)
	return render(request,'all_emp.html',context)

def add_emp(request):
	if request.method == 'POST':
		emp_id = request.POST['emp_id']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		sal = int(request.POST['sal'])
		age = int(request.POST['age'])
		bonus = int(request.POST['bonus'])
		phone = int(request.POST['phone'])
		email = request.POST['email']
		dept = request.POST['dept']
		role = request.POST['role']
		username = request.POST['username']
		password = request.POST['password']
		new_emp = Employee(emp_id = emp_id, first_name= first_name, password = password, username = username, last_name= last_name, age = age , sal = sal, bonus = bonus, phone = phone, email = email, dept_id = dept, role_id = role, hire_date = datetime.now())
		new_emp.save()
		return HttpResponse("Employee added Successfully.")

	elif request.method == 'GET':
		return render(request, 'add_emp.html')
	else:
		return HttpResponse("An Exception Occoured!!!")

def remove_emp(request, emp_id = 0):
	if emp_id:
		try:
			emp_to_be_removed = Employee.objects.get(id = emp_id)
			emp_to_be_removed.delete()
			return HttpResponse("Employee Removed Sucessfully")
		except:
			return HttpResponse("Please enter a valid Employee Id.")
	emps = Employee.objects.all()
	context = {
		'emps':emps
			}

	return render(request,'remove_emp.html', context)

def filter_emp(request):
	if request.method == "POST":
		name = request.POST['name']
		dept = request.POST['dept']
		role = request.POST['role']
		emps = Employee.objects.all()
		if name:
			emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
		if dept:
			emps = emps.filter(dept__name__icontains = dept)
		if role:
			emps = emps.filter(role__name__icontains = role)
		
		context = {
			'emps' : emps
}
		return render(request, 'all_emp.html', context)


	elif request.method == 'GET':
		return render(request,'filter_emp.html')
	else:
		return render('An Exception Occurred')
