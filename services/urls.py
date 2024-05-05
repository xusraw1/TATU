from django.urls import path
from .views import *

urlpatterns = [
    path('create/blog/', CreateBlogView.as_view(), name='create_blog'),
    path('blogs/', Blogs.as_view(), name='blogs'),
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blog'),
    path('blog/<int:id>/update/', BlogUpdateView.as_view(), name='update_blog'),

    path('passwords/', PasswordView.as_view(), name='passwords'),

    path('password/list/<slug:slug>/', PasswordViewProfile.as_view(), name='password_list'),
    path('password/delete/<int:id>/', delete_password, name='password_delete'),

    path('weather/', Weather.as_view(), name='weather'),

    path('', services, name='services'),
]
