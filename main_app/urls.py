from django.urls import path

from .views import AdvertListView, AdvertCreateView, AdvertDetailView, AdvertUpdateView, AdvertDeleteView


app_name = 'adverts'

urlpatterns = [
    path('', AdvertListView.as_view(), name='adverts'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='advert'),
    path('create/', AdvertCreateView.as_view(), name='advert_create'),
    path('<int:pk>/update/', AdvertUpdateView.as_view(), name='advert_update'),
    path('<int:pk>/delete/', AdvertDeleteView.as_view(), name='advert_delete'),
]
