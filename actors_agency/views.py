from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Actor, Agency, Character, ActorAgency
from .forms import ActorForm, AgencyForm, CharacterForm, ActorSearchForm, AgencySearchForm, CharacterSearchForm


@login_required
def index(request):
    context = {
        "num_actors": Actor.objects.count(),
        "num_agencies": Agency.objects.count(),
        "num_characters": Character.objects.count(),
        "num_visits": request.session.get("num_visits", 0) + 1,
    }
    request.session["num_visits"] = context["num_visits"]
    return render(request, "actors_agency/index.html", context)


class ActorListView(LoginRequiredMixin, generic.ListView):
    model = Actor
    paginate_by = 4
    context_object_name = "actor_list"
    template_name = "actors_agency/actor_list.html"

    def get_queryset(self):
        queryset = Actor.objects.all()
        name = self.request.GET.get("actor", "")
        if name:
            queryset = queryset.filter(username__icontains=name)
        current_user = self.request.user
        self_me = queryset.filter(username=current_user.username)
        other_actors = queryset.exclude(username=current_user.username)
        return list(self_me) + list(other_actors)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ActorSearchForm(initial={"actor": self.request.GET.get("actor", "")})
        return context


def actors_detail_view(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    current_bookings = ActorAgency.objects.filter(actor=actor, is_booked=True)
    past_bookings = ActorAgency.objects.filter(actor=actor, is_booked=False)

    context = {
        "actor": actor,
        "current_bookings": current_bookings,
        "past_bookings": past_bookings,
    }
    return render(request, "actors_agency/actor_detail.html", context)


class ActorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Actor
    form_class = ActorForm
    template_name = "actors_agency/actor_form.html"
    success_url = reverse_lazy("actors_agency:actor-list")


class ActorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Actor
    form_class = ActorForm
    template_name = "actors_agency/actor_form.html"
    success_url = reverse_lazy("actors_agency:actor-list")

class ActorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Actor
    success_url = reverse_lazy("actors_agency:actor-list")
    template_name = "actors_agency/actor_confirm_delete.html"

class CharacterListView(LoginRequiredMixin, generic.ListView):
    model = Character
    template_name = "actors_agency/characters_list.html"
    context_object_name = "character_list"
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('character')
        if query:
            return Character.objects.filter(name__icontains=query).order_by("name")
        return Character.objects.all().order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = CharacterSearchForm(self.request.GET)
        return context


def character_detail_view(request, pk):
    character = get_object_or_404(Character, pk=pk)
    actor_id = request.user.id
    actor_gender = Actor.objects.get(id=actor_id).gender
    character_gender = character.gender
    actor_is_booked = is_actor_booked(actor_id)
    character_is_booked = is_character_booked(character.id)
    is_different_gender =  actor_gender != character_gender
    return render(request, "actors_agency/character_detail.html", {
        "character": character,
        "agency": character.agency,
        "actor_is_booked": actor_is_booked,
        "character_is_booked": character_is_booked,
        "is_different_gender": is_different_gender,
    })

def is_actor_booked(actor_id: int) -> bool:
    return ActorAgency.objects.filter(actor_id=actor_id, is_booked=True).exists()

def is_character_booked(character_id: int) -> bool:
    return ActorAgency.objects.filter(character_id=character_id, is_booked=True).exists()



def character_create_view(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            agency_id = request.GET.get('agency_id')
            if agency_id:
                agency = get_object_or_404(Agency, pk=agency_id)
                character.agency = agency
            character.save()
            return redirect("actors_agency:characters-list")
    else:
        form = CharacterForm()

    return render(request, "actors_agency/character_form.html", {"form": form})

def character_update_view(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect("actors_agency:character-detail", pk=character.pk)
    else:
        form = CharacterForm(instance=character)

    return render(request, "actors_agency/character_form.html", {"form": form})

class CharacterDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Character
    success_url = reverse_lazy("actors_agency:characters-list")
    template_name = "actors_agency/character_confirm_delete.html"

class AgencyListView(LoginRequiredMixin, generic.ListView):
    model = Agency
    template_name = "actors_agency/agency_list.html"
    context_object_name = "agency_list"
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('agency')
        if query:
            return Agency.objects.filter(name__icontains=query).order_by("name")
        return Agency.objects.all().order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = AgencySearchForm(self.request.GET)
        return context


def agency_detail_view(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    return render(request, 'actors_agency/agency_detail.html', {
        'agency': agency,
        'characters': agency.characters.all(),
    })

def agency_create_view(request):
    if request.method == "POST":
        agency_form = AgencyForm(request.POST)
        if agency_form.is_valid():
            agency_form.save()
            return redirect("actors_agency:agency-list")
    else:
        agency_form = AgencyForm()

    return render(request, "actors_agency/agency_form.html", {'agency_form': agency_form})

def agency_update_view(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    if request.method == "POST":
        form = AgencyForm(request.POST, instance=agency)
        if form.is_valid():
            form.save()
            return redirect('actors_agency:agency-detail', pk=agency.pk)
    else:
        form = AgencyForm(instance=agency)
    return render(request, "actors_agency/agency_form.html", {'agency_form': form})

class AgencyDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Agency
    success_url = reverse_lazy("actors_agency:agency-list")
    template_name = "actors_agency/agency_confirm_delete.html"


def book_actor_agency_view(request, pk):
    character = get_object_or_404(Character, pk=pk)
    actor_id = request.user.id
    actor_gender = Actor.objects.get(id=actor_id).gender
    character_gender = character.gender
    actor_is_booked = is_actor_booked(actor_id)
    character_is_booked = is_character_booked(character.id)
    is_different_gender =  actor_gender != character_gender
    is_booked = False

    if not is_different_gender and not actor_is_booked and not character_is_booked:
        is_booked = True
        ActorAgency.objects.create(
            character=character,
            actor_id=actor_id,
            agency_id=character.agency_id,
            is_booked=True
        )
        return render(request, "actors_agency/actor_agency_booked.html", {
        "user": request.user.username,
        "character": character,
        "agency": character.agency,
        "actor_is_booked": actor_is_booked,
        "character_is_booked": character_is_booked,
        "is_different_gender": is_different_gender,
        "is_booked": is_booked
    })

def delete_booking(request, booking_id):
    booking = get_object_or_404(ActorAgency, id=booking_id)

    if request.method == "POST":
        booking.is_booked = False
        booking.save()
        messages.success(request, f"Booking for {booking.character.name} has been successfully canceled.")
        return redirect('actors_agency:actor-detail', pk=booking.actor.id)

    return render(request, 'actors_agency/delete_booking_confirm.html', {'booking': booking})
