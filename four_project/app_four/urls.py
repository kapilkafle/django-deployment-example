from django.conf.urls import url
from app_four import views

app_name = 'app_four'

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.user_login, name='user_login')
]