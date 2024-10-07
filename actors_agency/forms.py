from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from actors_agency.models import Actor, Character, Agency


User = get_user_model()

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]


class ActorForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = Actor
        fields = [
            "username",
            "first_name",
            "last_name",
            "gender",
            "bio",
            "password1",
            "password2",
        ]


class CharacterForm(forms.ModelForm):
    agency = forms.ModelChoiceField(
        queryset=Agency.objects.all(),
        widget=forms.Select,
        required=True,
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = Character
        fields = ["name", "gender", "description", "agency"]


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ["name", "city", "description"]


class SearchForm(forms.Form):
    search_query = forms.CharField(
        label="",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
            }
        ),
    )

    def __init__(self, *args, placeholder=None, **kwargs):
        super().__init__(*args, **kwargs)
        if placeholder:
            self.fields['search_query'].widget.attrs['placeholder'] = placeholder


class ActorSearchForm(SearchForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, placeholder="Search by actor", **kwargs)


class AgencySearchForm(SearchForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, placeholder="Search by agency", **kwargs)


class CharacterSearchForm(SearchForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, placeholder="Search by character", **kwargs)
