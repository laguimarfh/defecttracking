from django.urls import path
from . import views  # Import the blog views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Set root to home view    
    path('defect-input/', views.DefectFormView.as_view(), name='defect-input'
    ),
]


# path('about/', login_required(views.AboutView.as_view()), name='about'),
#     path('photo/', views.PhotoContestView.as_view(), name='photo'),
#     path('home2/', views.Home2View.as_view(), name='home2'),
#     path('java/', views.JavaView.as_view(), name='java'),
#     path('topic/', views.TopicListView.as_view(), name='topic'),
#     path(
#         'topics/<slug:slug>/',
#         views.TopicDetailView.as_view(),
#         name='topic-detail',
#     ),
#     path('posts/', views.PostListView.as_view(), name='post-list'),
#     path(
#         'posts/<int:year>/<int:month>/<int:day>/<slug:slug>/',
#         views.PostDetailView.as_view(),
#         name='post-detail',
#     ),
#     path(
#         'posts/<int:pk>/',
#         views.PostDetailView.as_view(),
#         name='post-detail',
#     ),
#     # path('form-example/', views.form_example, name='form-example'),
#     path(
#         'contact/',
#         views.ContactFormView.as_view(),
#         name='contact'
#     ),
#     path(
#         'photo-contest/',
#         views.PhotoContestFormView.as_view(),
#         name='photo-contest'
#     ),
