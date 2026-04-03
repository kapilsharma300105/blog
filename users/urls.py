from django.contrib import admin
from django.urls import path, include
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('blog1.urls')),
    path('register/', user_views.register, name='register'),
    
]