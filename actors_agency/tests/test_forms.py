from django.test import TestCase

from actors_agency.forms import ActorForm, CharacterForm, AgencyForm


class ActorFormTestCase(TestCase):
    def test_valid_actor_form(self):
        form_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "password": "testpassword",
            "gender": "M",  # або "F", залежно від реалізації
            "bio": "This is a test bio."
        }
        form = ActorForm(data=form_data)
        self.assertTrue(form.is_valid())
        actor = form.save()
        self.assertEqual(actor.username, form_data["username"])

    def test_invalid_actor_form_missing_fields(self):
        form_data = {
            "username": "",
            "first_name": "Test",
            "last_name": "User",
            "password": "testpassword",
            "gender": "M",
            "bio": "This is a test bio."
        }
        form = ActorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)


class CharacterFormTestCase(TestCase):
    def setUp(self):
        self.agency = Agency.objects.create(name="Test Agency", city="Test City", description="Test Description")

    def test_valid_character_form(self):
        form_data = {
            "name": "Test Character",
            "gender": "M",  # або "F"
            "description": "This is a test character.",
            "agency": self.agency.id
        }
        form = CharacterForm(data=form_data)
        self.assertTrue(form.is_valid())
        character = form.save()
        self.assertEqual(character.name, form_data["name"])

    def test_invalid_character_form_missing_fields(self):
        form_data = {
            "name": "",
            "gender": "M",
            "description": "This is a test character.",
            "agency": self.agency.id
        }
        form = CharacterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class AgencyFormTestCase(TestCase):
    def test_valid_agency_form(self):
        form_data = {
            "name": "Test Agency",
            "city": "Test City",
            "description": "This is a test description."
        }
        form = AgencyForm(data=form_data)
        self.assertTrue(form.is_valid())
        agency = form.save()
        self.assertEqual(agency.name, form_data["name"])

    def test_invalid_agency_form_missing_fields(self):
        form_data = {
            "name": "",
            "city": "Test City",
            "description": "This is a test description."
        }
        form = AgencyForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
