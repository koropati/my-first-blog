from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('post/', views.post_list, name='post_list'),
	path('post/drafts', views.post_draft_list, name='post_draft_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
	path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
	path('jurnal/', views.jurnal_list, name='jurnal_list'),
	path('jurnal/new/', views.jurnal_new, name='jurnal_new'),
	path('jurnal/<int:pk>/edit/', views.jurnal_edit, name='jurnal_edit'),
	path('new/', views.data_test, name='data_test'),
	path('map/', views.data_list, name='data_list'),
	path('map/<int:id>/', views.data_detail, name='data_detail'),
	path('map/<int:id>/remove/', views.data_remove, name='data_remove'),
	# path('res/', views.response, name='response'),
]