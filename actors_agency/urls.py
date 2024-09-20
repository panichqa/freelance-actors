from django.urls import path
from .views import (
    index,
    actors_detail_view,
    ActorsListView,
    CharactersListView,
    AgencyListView, agency_detail_view, character_detail_view
)

urlpatterns = [
    path('', index, name='index'),
    path('actors/', ActorsListView.as_view(), name='actors-list'),
    path('actors/<int:pk>/',actors_detail_view, name='actor-detail'),
    path('agencies/',AgencyListView.as_view(), name='agency-list'),
    path('agencies/<int:pk>/',agency_detail_view, name='agency-detail'),
    path('characters/',CharactersListView.as_view(), name='characters-list'),
    path('characters/<int:pk>/', character_detail_view, name='character-detail'),
]

app_name = "actors_agency"
