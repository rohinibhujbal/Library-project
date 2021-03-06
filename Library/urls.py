"""Library URL Configuration

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
from django.urls import path
from Book import views           

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage,name='welcome'),
    path('save.book/',views.save_book),
    path('edit.book/<int:id>/',views.edit_book),
    path('delete.book/<int:pk>/',views.delete_book),
    path('show_deleted_book/',views.show_deleted_data),
    path('hard_deleted_book/<int:pk>/',views.hard_delete_book),
    path('restore_book/<int:id>/',views.restore_book),
    path('restore_all_books/',views.restore_all),
    path('delete_all_books/',views.delete_all),
]

# http://127.0.0.1:8000/      -BASE URL ALWYS FIXED
# http://127.0.0.1:8000/admin/     THESE URL HITS ON CHROMEdfsdsdsds