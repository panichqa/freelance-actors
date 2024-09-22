from django import forms
from actors_agency.models import Actor, Character, Agency
from django.contrib.auth import get_user_model


User = get_user_model()


class ActorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Actor
        fields = [
            "username",
            "first_name",
            "last_name",
            "password",
            "gender",
            "bio",
        ]

    def save(self, commit=True):
        actor = super().save(commit=False)
        actor.set_password(self.cleaned_data['password'])  # Хешує пароль
        if commit:
            actor.save()
        return actor



class CharacterForm(forms.ModelForm):
    agency = forms.ModelChoiceField(
        queryset=Agency.objects.all(),
        widget=forms.Select,
        required=True,
    )

    class Meta:
        model = Character
        fields = ['name', 'gender', 'description', 'agency']


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ["name", "city", "description"]


class ActorSearchForm(forms.Form):
    actor = forms.CharField(
        label="",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by actor"
            }
        ),
    )


class AgencySearchForm(forms.Form):
    agency = forms.CharField(
        label="",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by agency"
            }
        ),
    )


class CharacterSearchForm(forms.Form):
    character = forms.CharField(
        label="",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by character"
            }
        ),
    )
