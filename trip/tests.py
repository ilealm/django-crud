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

    def test_string_representation(self):
        destination = Destinations(place='Seattle')
        self.assertEqual(str(destination), destination.place)
    
    def test_trip_content(self):
        self.assertEqual(f'{self.destination.place}', 'island')
        self.assertEqual(f'{self.destination.location}', 'in the sea')
        self.assertEqual(f'{self.destination.summary}', 'is a magical place')

    def test_trip_list_view(self):
        response = self.client.get(reverse('destination_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'island')
        self.assertTemplateUsed(response, 'destination_list.html')

    def test_trip_detail_view(self):
        response = self.client.get(reverse('destination_detail', args='1')) #'/snacks/1/')
        no_response = self.client.get('/destination/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'magical')
        self.assertTemplateUsed(response, 'destination_detail.html')

    def test_trip_create_view(self):
        response = self.client.post(reverse('destination_create'), {
            'author' : self.user,
            'place' : 'lake',
            'location':'samamish',
            'summary' :'amazing animals',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'lake')
        self.assertContains(response, 'samamish')
        self.assertTemplateUsed(response, 'destination_create.html')

    #here must update all the fields
    def test_trip_update_view(self):
        response = self.client.post(reverse('destination_update',args='1'), {
            'place': 'Updated place',
            'location':'Updated location',
            'summary': 'Updated summary',
        })
        self.assertEqual(response.status_code, 302)


    def test_trip_update_view_redirect(self):
        response = self.client.post(reverse('destination_update',args='1'), {
            'place': 'Updated place',
            'location':'Updated location',
            'summary': 'Updated summary',
        }, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Updated place')

        self.assertTemplateUsed('destination_detail.html')

    def test_trip_delete_view(self):
        response = self.client.get(reverse('destination_delete',args='1'))
        self.assertEqual(response.status_code, 200)