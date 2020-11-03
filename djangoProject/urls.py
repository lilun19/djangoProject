"""djangoProject URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from demo import views
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    #精确匹配
    path('page/<year>/<month>', views.home),
    url(r'^$', view.hello),
    url('^demo/$', views.demo,name='demo_page'),
    url(r'^page/(\d+)$', views.page),
    # 获取urlc参数,用<name>这种格式,?P 参数year
    # [0-9] 匹配0-9的数字
    # {4} 匹配4个数字
    # {1,2} 匹配1-2个数字
    # r 是raw原型，不转义
    # ^ 匹配开始
    # $ 匹配结束
    url(r'^page/(?P<year>[0-9]{4})/(?P<month>[0-9]{1，2}).html$', views.home1),
    url('hom/',views.hom,name='home_page')
]
