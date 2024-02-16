from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('upload/', views.upload_file, name='upload'),
    path('upload-success/', views.upload_success, name='upload_success'),
    path('', views.upload_file, name='upload'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]


# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', index, name='index'),
#     path('login/', login_view, name='login'),
#     path('register/', register_view, name='register'),
#     path('upload/', upload_view, name='upload'),
#     path('upload/success/', upload_success, name='upload_success'),
# ]