from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('post/', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('jurnal/', views.jurnal_list, name='jurnal_list'),
	path('jurnal/new/', views.jurnal_new, name='jurnal_new'),
	path('jurnal/<int:pk>/edit/', views.jurnal_edit, name='jurnal_edit'),
]