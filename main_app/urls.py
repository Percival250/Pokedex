from django.urls import path
from .views import poke_list_view, poke_detail_view

urlpatterns = [
    path('poke_list/', poke_list_view),
    path('poke_list/<int:id>/', poke_detail_view),
]