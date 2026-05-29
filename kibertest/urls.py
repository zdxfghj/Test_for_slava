from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

from kibertest import views as kiber_views

router.register(r"results", kiber_views.PersonViewSet)
router.register(r"cards", kiber_views.CardsViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('auth', views.auth, name='auth'),
    path('search', views.search, name='search'),
    path('api/save-test-result/', views.save_test_result, name='save_test_result'),
    path("api/", include(router.urls)),

]