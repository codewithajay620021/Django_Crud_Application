from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('program/', views.program, name='program'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('contact_submit/', views.contact_submit, name='contact_submit'),
    path('details_submit/', views.details_submit, name='details_submit'),
    path('register_view/', views.register_view, name='register_view'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit_submit/<int:id>', views.edit_submit, name='edit_submit'),
]