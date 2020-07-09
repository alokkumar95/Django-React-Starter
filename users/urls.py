from django.urls import path
from users.views import users, react

urlpatterns = [
    path('user/', users),
    path('react/', react, name='react')

]
