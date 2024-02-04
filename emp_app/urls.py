"""Office_Employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from emp_app.views import index, aboutus, all_emp, add_emp,loggedIn, remove_emp, filter_emp, afterlogin, login, logout, signin, register, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index', index),
    path('signin', signin),
    path('login', login),
    path('afterlogin', afterlogin),
    path('loggedIn',loggedIn),
    path('logout', logout),
    path('register', register),
    path('aboutus', aboutus),
    path('contact', contact),
    path('all_emp', all_emp),
    path('add_emp', add_emp),
    path('remove_emp', remove_emp),
    path('remove_emp/<int:emp_id>', remove_emp),
    path('filter_emp', filter_emp),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


