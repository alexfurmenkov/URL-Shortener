"""
Module with router configuration of
"shortener" project
"""
from django.contrib import admin
from django.urls import path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import shortener.views as views

schema_view = get_schema_view(
   openapi.Info(
      title="Shortener API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', views.HomepageHandler.as_view(), name='homepage'),
    path('api/short/', views.UrlShortenHandler.as_view(),
         name='short'),
    path('<slug:short_url>/', views.ResolveShortUrlHandler.as_view(),
         name='resolve_short_url'),
]
