"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from website.views import index
from .sitemaps import WebsiteStaticSitemap
from article.sitemaps import ArticleSitemap
from django.contrib.sitemaps.views import sitemap

app_name = 'website'

sitemaps = {
    'static': WebsiteStaticSitemap,
    'article': ArticleSitemap
    
    
}


urlpatterns = [
    path('',index,name='index'),
    path(
    "sitemap.xml",sitemap,{"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",),
    # path('robots.txt',include('robots.urls')),
]


