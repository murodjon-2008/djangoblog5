from django.template.context_processors import static
from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='blog-home'),
    path('sidebar/', sidebar, name='sidebar'),
    path('single-post/',single_post, name='single_post'),
    path('404/',error, name='error'),
    path('<slug>/edit/',UpdateVIEW.as_view(),name='Edit_page'),
    path('create/',CreateVIEW.as_view(),name='Create_page'),
    path('sidebar/create/', CreateVIEW.as_view(), name='Create_page'),
    path('single/<slug>/delete/',DeleteVIEW.as_view(),name='Delete_page'),
    # path('accounts/register/', sign_up, name='register'),

]