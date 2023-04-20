"""
URL configuration for crudpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from crudapp import views
# from django.urls.resolvers import URLPattern
app_name = 'crudapp'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",views.CompanyListView.as_view(),name='company_list'),
    path("company<int:pk>/home/",views.CompanyDetailview.as_view(),name='company_detail'),
    path("create/",views.CompanyCreateview.as_view()),
    # path("update/",views.CompanyUpdateView.as_view()),
    path('update/<int:pk>/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('delete/<int:pk>/',views.CompanyDeleteView.as_view())
]


