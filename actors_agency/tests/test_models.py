from django.test import TestCase

from actors_agency.models import Actor, Agency, Character, ActorAgency


class ActorModelTestCase(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create_user(
            username="testuser",
            password="testpassword",
            gender="M",
            bio="This is a test bio."
        )

    def test_actor_str(self):
        self.assertEqual(str(self.actor), "testuser")


class AgencyModelTestCase(TestCase):
    def setUp(self):
        self.agency = Agency.objects.create(
            name="Test Agency",
            city="Test City",
            description="This is a test description."
        )

    def test_agency_str(self):
        self.assertEqual(str(self.agency), "Test Agency")


class CharacterModelTestCase(TestCase):
    def setUp(self):
        self.agency = Agency.objects.create(
            name="Test Agency",
            city="Test City",
            description="This is a test description."
        )
        self.character = Character.objects.create(
            name="Test Character",
            gender="M",
            description="This is a test character.",
            agency=self.agency
        )

    def test_character_str(self):
        self.assertEqual(str(self.character), "Test Character")


class ActorAgencyModelTestCase(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create_user(
            username="testuser",
            password="testpassword",
            gender="M",
            bio="This is a test bio."
        )
        self.agency = Agency.objects.create(
            name="Test Agency",
            city="Test City",
            description="This is a test description."
        )
        self.character = Character.objects.create(
            name="Test Character",
            gender="M",
            description="This is a test character.",
            agency=self.agency
        )
        self.actor_agency = ActorAgency.objects.create(
            actor=self.actor,
            agency=self.agency,
            character=self.character,
            is_booked=False
        )

    def test_actor_agency_str(self):
        self.assertEqual(
            str(self.actor_agency),
            f"{self.actor.username} - {self.character.name} ({self.agency.name})"
        )
