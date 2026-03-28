"""
URL configuration for rooGUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from basics.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/",index,name='index'),
    path("frames/",frames, name='frames'),
    path("frame_order/",frame_order,name='frame_order'),
    path("mugs/",mugs, name='mugs'),
    path('order/',order,name='order'),

    path("keychains/",keychains, name='keychains'),

    path("about/",about, name='about'),

    path("contact/",contact, name='contact'),

    path("thankyou/",thankyou, name='thankyou'),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
     path("register/",register, name="register"),

]
