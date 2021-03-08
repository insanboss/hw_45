"""hw_45 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from To_do_list.views import (
    index_view,
    task_view,
    task_create_view,
    task_update_view,
    task_delete_view
)
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index_view, name='index'),
#     path('article/<int:pk>', article_view, name='article_view'),
#     path('articles/add', article_create_view, name='article_add')
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('task/<int:pk>', task_view, name='task_view'),
    path('task/add/', task_create_view, name='task_add'),
    path('task/<int:pk>/update/', task_update_view, name='task_update'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete'),
]
