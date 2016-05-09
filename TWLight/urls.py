"""
TWLight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from TWLight.users import authorization as auth
from TWLight.users.urls import urlpatterns as users_urls
from TWLight.applications.urls import urlpatterns as applications_urls

from .views import DashboardView


urlpatterns = [
	# Built-in
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', auth_views.login, name='auth_login'),
    url(r'^accounts/logout/',
        auth_views.logout,
        {'next_page': '/'},
        name='auth_logout'),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^oauth/login/$',
        auth.OAuthInitializeView.as_view(),
        name='oauth_login'),
    url(r'^oauth/callback/$',
        auth.OAuthCallbackView.as_view(),
        name='oauth_callback'),

    url(r'^dashboard/$',
        DashboardView.as_view(),
        name='dashboard'
    ),

    # TWLight apps
    url(r'^users/', include(users_urls, namespace="users")),
    url(r'^applications/', include(applications_urls,namespace="applications")),
]
