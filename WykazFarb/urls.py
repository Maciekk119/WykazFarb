"""WykazFarb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from WykazFarb.views import Main, CatalogueBrands, CatalogueTypes, Analog, Logging, Registering, PaintSets, Logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view()),
    path('katalog/brand/<brand>', CatalogueBrands.as_view()),
    path('katalog/type/<type>', CatalogueTypes.as_view()),
    path('odpowiedniki/<id>', Analog.as_view()),
    path('paintsets/', PaintSets),
    path('accounts/login/', Logging.as_view()),
    path('registering/', Registering.as_view()),
    path('logout/', Logout),



]
