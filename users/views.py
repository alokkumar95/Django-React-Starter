from django.shortcuts import render
from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer
from django.core.paginator import Paginator


class User_objects(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def users(request):
    queryset = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    # dic = {}
    # dic["users"] = []
    # for item in queryset:
    #     print(item.id)
    #     dic["users"].append(item)

    return render(request, "users/home.html", {'users': users})
# Create your views here.


def react(request):
    return render(request, "users/react.html")
