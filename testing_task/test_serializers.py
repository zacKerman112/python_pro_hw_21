from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from .serializers import ToDoSerializer, UserSerializer


class TestToDoSerializer(TestCase):

    def test_serializer_with_valid_data(self):
        """testing serializer with valid data which fit in the boarderlines of serialiser it self"""
        tomorrow = timezone.now() + timedelta(days=1)
        serializer_data = {
            'title': 'Clean the house',
            'description': 'Second floor included',
            'due_date': tomorrow
        }
        serializer = ToDoSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['title'], 'Clean the house')

    def test_serializer_with_invalid_data(self):
        """testing serializer with invalid data which don`t fit in the boarderlines of serializer itself"""
        tomorrow = timezone.now() + timedelta(days=1)
        serializer_data = {
            'title': 'clean the house and walk the dog in the back yard tomorrow!!',
            'description': 'unacceptable to skip',
            'due_date': tomorrow
        }
        serializer = ToDoSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_serializer_with_missing_data(self):
        """testing serializer with missing data to ensure required fields trigger validation errors"""
        tomorrow = timezone.now() + timedelta(days=1)
        serializer_data = {
            'due_date': tomorrow,
        }
        serializer = ToDoSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)
        self.assertIn('description', serializer.errors)

    def test_serializer_date_in_past_fails(self):
        """testing serializer with past date to ensure custom validation blocks it"""
        yesterday = timezone.now() - timedelta(days=1)
        serializer_data = {
            'title': 'Clean the house',
            'description': 'Second floor included',
            'due_date': yesterday
        }
        serializer = ToDoSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('due_date', serializer.errors)


class TestUserSerializer(TestCase):

    def test_serializer_with_valid_data(self):
        """testing serializer with valid data which fit in the boarderlines of serialiser it self"""
        serializer_data = {
            'id': 1,
            'username': 'zakhar1234',
            'email': 'someemail@gmail.com'
        }
        serializer = UserSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['username'], 'zakhar1234')

    def test_serializer_with_invalid_data(self):
        """testing serializer with invalid data which don`t fit in the boarderlines of serializer itself"""
        serializer_data = {
            'id': -1,
            'username': 'A',
            'email': 'someemail@gmail.com'
        }
        serializer = UserSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('id', serializer.errors)
        self.assertIn('username', serializer.errors)