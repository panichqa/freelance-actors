from django.urls import path

from .views import (
    index,
    actors_detail_view,
    ActorListView,
    CharacterListView,
    AgencyListView,
    agency_detail_view,
    character_detail_view,
    ActorCreateView,
    ActorUpdateView,
    ActorDeleteView,
    character_create_view,
    character_update_view,
    CharacterDeleteView,
    agency_create_view,
    agency_update_view,
    AgencyDeleteView,
    book_actor_agency_view,
    delete_booking
)

app_name = "actors_agency"
urlpatterns = [
    path("", index, name="index"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", actors_detail_view, name="actor-detail"),
    path("actors/create/", ActorCreateView.as_view(), name="actor-create"),
    path("actors/<int:pk>/update/", ActorUpdateView.as_view(), name="actor-update"),
    path("actors/<int:pk>/delete/", ActorDeleteView.as_view(), name="actor-delete"),

    path("agencies/", AgencyListView.as_view(), name="agency-list"),
    path("agencies/<int:pk>/", agency_detail_view, name="agency-detail"),
    path("agencies/create/", agency_create_view, name="agency-create"),
    path("agencies/<int:pk>/update/", agency_update_view, name="agency-update"),
    path("agencies/<int:pk>/delete/", AgencyDeleteView.as_view(), name="agency-delete"),

    path("characters/", CharacterListView.as_view(), name="characters-list"),
    path("characters/<int:pk>/", character_detail_view, name="character-detail"),
    path("characters/create/", character_create_view, name="character-create"),
    path("characters/<int:pk>/update/", character_update_view, name="character-update"),
    path("characters/<int:pk>/delete/", CharacterDeleteView.as_view(), name="character-delete"),

    path("actor-agency/book/character/<int:pk>/", book_actor_agency_view, name="book-character"),
    path("booking/<int:booking_id>/delete/", delete_booking, name="delete-booking"),

]
