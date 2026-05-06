from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('auth', views.auth, name='auth'),
    path('search', views.search, name='search'),
    path('api/save-test-result/', views.save_test_result, name='save_test_result'),
]