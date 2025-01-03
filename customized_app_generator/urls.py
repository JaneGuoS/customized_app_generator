"""
URL configuration for customized_app_generator project.

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
from django.urls import path, re_path,include

from blog import views
from blog.views import BlogDetailView, BlogListView, ChannelListView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r"^main/",
        views.blog_list,
        # ChannelListView.as_view(template_name="blog/blog_list.html"),
        # name="blog_list",
    ),
    re_path(
        r"^detail(?P<pk>\d+)/$",
        BlogDetailView.as_view(template_name="blog/blog_detail.html"),
        name="blog_detail",
    )

]
