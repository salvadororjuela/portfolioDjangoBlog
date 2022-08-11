"""blog_app_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Necesary to import static files
from django.conf.urls.static import static
from django.conf import settings
# Necessary for redirecting the homepage
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path("users/", include("users.urls")),
    # Redirects the homepage to the url http://127.0.0.1:8000/
    path("", views.index, name="index")
]

urlpatterns += staticfiles_urlpatterns()
# Necesary to read media files from the database
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
