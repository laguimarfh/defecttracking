from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('input/', views.InputView.as_view(), name='input'),  # Set root to home view    
    path('defect-input/', views.DefectFormView.as_view(), name='defect-input'
    ),
    # path('ajax-form/', views.AjaxFormView.as_view(), name='ajax'
    # ),
    path('home2/', views.HomeView2.as_view(), name='home2'),
    path('home2/create_post/', views.create_post, name='create_post'),
    path('ajaximage/', views.ajaximage, name='ajaximage'),
]