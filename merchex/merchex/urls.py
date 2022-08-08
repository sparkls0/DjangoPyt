
from django.contrib import admin
from django.urls import path
from listing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('about-us', views.about),
    path('listings', views.listings),
    path('contact-us', views.contact)
]



