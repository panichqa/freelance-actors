from django.urls import path
from .views import index, ActorDetailView

urlpatterns = [
    path("", index, name="index"),  # Головна сторінка
    path("actor/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),  # Деталі актора
]

app_name = "actors_agency"
