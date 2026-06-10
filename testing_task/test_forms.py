from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from .forms import ToDo


class ToDoTestCase(TestCase):

    def test_form_valid_data(self):
        """testing form with valid data"""
        tomorrow = timezone.now() + timedelta(days=1)
        form_data = {
            'title': 'clean the house',
            'description': 'second floor included',
            'due_date': tomorrow
        }
        form = ToDo(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        """testing form with invalid data"""
        yesterday = timezone.now() - timedelta(days=1)
        form_data = {
            'title': 'clean the house and walk the dog in the back yard tomorrow!!',
            'description': 'unacceptable to skip',
            'due_date': yesterday
        }
        form = ToDo(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)