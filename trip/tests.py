from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Destinations

class TripTest(TestCase):
  def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='pass'
        )

        self.destination = Destinations.objects.create(
            author=self.user,
            place='island',
            location='in the sea',
            summary='is a magical place',
        )