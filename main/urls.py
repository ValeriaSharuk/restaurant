from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('menu', views.DishView.as_view(), name='menu'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('registration', views.RegFormView.as_view(), name='registration'),
    path('logout', views.LogoutFormView.as_view(), name='logout'),
    path('create_about', views.create_about, name='create_about'),
    path('update', views.AboutUpdateView.as_view(), name='about_update'),
    path('create_feedback', views.Index.feedback_create, name='create_feedback'),
]
