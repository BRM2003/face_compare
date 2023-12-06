from django.contrib import admin
from django.urls import path
from main.views import main_script

urlpatterns = [
    path('admin/', admin.site.urls),
    path('face_compare', main_script)
]
