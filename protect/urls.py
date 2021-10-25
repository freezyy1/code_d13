from django.urls import path
from .views import ProfileView, replies_by_advert, take_reply, delete_reply


urlpatterns = [
    path('', ProfileView.as_view()),
    path('<int:advert_pk>/', replies_by_advert, name='replies_by_advert'),
    path('<int:advert_pk>/<int:reply_pk>/take/', take_reply, name='take_reply'),
    path('<int:advert_pk>/<int:reply_pk>/delete/', delete_reply, name='delete_reply')

]
