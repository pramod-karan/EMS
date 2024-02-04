from django.db import models

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length=100,null=False)
	location = models.CharField (max_length=100)
	
	def __str__(self):
		return self.name

class Role(models.Model):
	name = models.CharField(max_length=100, null=False)

	def __str__(self):
		return self.name

class Employee(models.Model):
	emp_id = models.IntegerField(null=False)
	first_name = models.CharField(max_length=30, null=False)
	last_name = models.CharField(max_length=30)
	age = models.IntegerField()
	dept = models.ForeignKey(Department, on_delete=models.CASCADE)
	sal = models.IntegerField(default=0)
	bonus = models.IntegerField(default=0)
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	phone = models.IntegerField()
	email = models.EmailField(max_length=50)
	hire_date = models.DateField()
	username = models.CharField(max_length=15, null=False)
	password = models.CharField(max_length=15, default = "Welcome*123")

	def __str__(self):
		return "%s %s %s" %(self.first_name,self.last_name,self.phone)

class Contact(models.Model):
	sno = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	phone = models.CharField(max_length = 15)
	email = models.EmailField(max_length=50)
	content = models.TextField()
	timeStamp = models.DateTimeField(auto_now_add = True, blank = True)
	
	def __str__(self):
		return 'Message from ' + self.name






	