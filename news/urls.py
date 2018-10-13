"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from posts.api.views import PostViewSet
from comments.api.views import CommentViewSet
from user.api.views import UserViewSet
from profiles.api.views import ProfileViewSet

from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()

router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/login', obtain_jwt_token)
]
