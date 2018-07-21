"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from MyBlog import settings
from articles import views

urlpatterns = [
                  path('articles/<int:article_pk>/',
                       views.ArticleView.as_view(),
                       name='article_page'),
                  path('admin/', admin.site.urls),
                  path('', views.HomeView.as_view(),
                       name='home'),
                  path('logout/', auth_views.LogoutView.as_view(),
                       name='logout'),
                  path('new/',
                       views.write_article,
                       name='new_article'),
                  path('new/complete/',
                       views.write_article_complete,
                       name='new_article_complete'),
                  path('delete_success/<int:article_pk>/',
                       views.DeleteSuccessView.as_view(),
                       name='delete_success'),
                  path('login/',
                       auth_views.LoginView.as_view(template_name='login.html'),
                       name='login'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
