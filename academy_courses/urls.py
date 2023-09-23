from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name='about'),
    path('courses/', views.course, name='course'),
    path('course/<int:pk>/', views.course_list, name='course_list'),
    path('course/show/<int:pk>/', views.CourseDetailView.as_view(), name='course_page'),
    path('course/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('course/update/<int:pk>/', views.CourseUpdateView.as_view(), name='course_update'),
    path('course/delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('course/video/create/', views.VideoCreateView.as_view(), name='video_create'),
    path('course/video/update/<int:pk>/', views.VideoUpdateView.as_view(), name='video_update'),
    path('course/video/delete/<int:pk>/', views.VideoDeleteView.as_view(), name='video_delete'),
    path('course/comment/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('course/comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('course/checkout/<int:pk>/', views.checkout, name='checkout'),
    path('checkout/complete/', views.checkout_complete, name='checkout.complete'),
    path('checkout/stripe/', views.stripe_transaction, name='checkout.stripe'),
    path('checkout/stripe/config/', views.stripe_config, name='checkout.stripe.config'),
    path('nohasperm/', views.notperm, name='notaccess'),
]