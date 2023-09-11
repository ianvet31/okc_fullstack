"""backend URL Configuration

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
from django.urls import re_path
from app.views import players
from django.contrib import admin
admin.site.enable_nav_sidebar = False  # Optional: To hide the admin sidebar

urlpatterns = [
    re_path(r'^api/v1/playerSummary/(?P<playerID>[0-9]+)$', players.PlayerSummary.as_view(), name='player_summary'),
]
