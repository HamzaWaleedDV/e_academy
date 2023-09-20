from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('courses/', views.course, name='course'),
    path('courses/<int:pk>/', views.course_list, name='course_list'),
    path('courses/show/<int:pk>/', views.CourseDetailView.as_view(), name='course_page'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/update/<int:pk>/', views.CourseUpdateView.as_view(), name='course_update'),
    path('courses/delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('courses/video/create/', views.VideoCreateView.as_view(), name='video_create'),
    path('courses/video/update/<int:pk>/', views.VideoUpdateView.as_view(), name='video_update'),
    path('courses/video/delete/<int:pk>/', views.VideoDeleteView.as_view(), name='video_delete'),
]