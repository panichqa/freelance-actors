from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic
from .models import Actor, Agency, Character

def index(request):
    num_actors = Actor.objects.count()
    num_agencies = Agency.objects.count()
    num_characters = Character.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_actors": num_actors,
        "num_agencies": num_agencies,
        "num_characters": num_characters,
        "num_visits": num_visits + 1,
    }

    return render(request, "actors_agency/index.html", context=context)


class ActorsListView(generic.ListView):
    model = Actor
    template_name = "actors_agency/actors_list.html"
    context_object_name = "actors_list"
    paginate_by = 4

    def get_queryset(self):
        return Actor.objects.all().order_by("username")

def actors_detail_view(request:HttpRequest, pk: int):
    actor = Actor.objects.get(id=pk)
    context = {
        "actor": actor,
    }
    return render(request, "actors_agency/actors_detail.html", context)


class CharactersListView(generic.ListView):
    model = Character
    template_name = "actors_agency/characters_list.html"
    context_object_name = "characters_list"
    paginate_by = 4

    def get_queryset(self):
        return Character.objects.all().order_by("name")


def character_detail_view(request: HttpRequest, pk: int):
    character = Character.objects.get(id=pk)
    context = {
        "character": character,
    }
    return render(request, "actors_agency/character_detail.html", context)


class AgencyListView(generic.ListView):
    model = Agency
    template_name = "actors_agency/agency_list.html"
    context_object_name = "agency_list"
    paginate_by = 4

    def get_queryset(self):
        return Agency.objects.all().order_by("name")

def agency_detail_view(request: HttpRequest, pk: int):
    agency = Agency.objects.get(id=pk)
    context = {
        "agency": agency,
    }
    return render(request, "actors_agency/agency_detail.html", context)
