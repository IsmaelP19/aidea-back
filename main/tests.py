from django.test import TestCase
from .models import CustomUser
import pytest

# Create your tests here.


class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(
            username='testuser',
            password='testpassword',
        )

    def test_user_created(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpassword')
        self.assertEqual(user.age, None)
        self.assertEqual(user.phone, None)

    def test_user_updated(self):
        user = CustomUser.objects.get(username='testuser')
        user.age = 25
        user.phone = '123456789'
        user.save()
        self.assertEqual(user.age, 25)
        self.assertEqual(user.phone, '123456789')

    def test_user_deleted(self):
        user = CustomUser.objects.get(username='testuser')
        user.delete()
        self.assertEqual(CustomUser.objects.filter(
            username='testuser').count(), 0)

    def test_create_custom_user_with_valid_age_and_phone(self):
        user = CustomUser.objects.create(
            username='testuser2', age=25, phone='1234567890')
        assert user.age == 25
        assert user.phone == '1234567890'

    def test_custom_user_str_method(self):
        user = CustomUser(username='testuser')
        assert str(user) == 'testuser'

    def test_create_custom_user_with_null_age_and_phone(self):
        user = CustomUser.objects.create(
            username='testuser2', age=None, phone=None)
        assert user.age is None
        assert user.phone is None

    def test_custom_user_string_representation(self):
        user = CustomUser(username='testuser')
        assert str(user) == 'testuser'

    def test_create_custom_user_with_age_zero(self):
        user = CustomUser.objects.create(
            username='testuser2', age=0, phone='1234567890')
        assert user.age == 0
        assert user.phone == '1234567890'

    def test_create_custom_user_with_non_numeric_age(self):
        invalid_age = 'invalid'
        with pytest.raises(ValueError, match="Field 'age' expected a number but got '{}'".format(invalid_age)):
            CustomUser.objects.create(
                username='testuser2', age=invalid_age, phone='1234567890')

    def test_create_custom_user_with_special_characters_in_phone(self):
        user = CustomUser.objects.create(
            username='testuser2', age=25, phone='!@#$%^&*()')
        assert user.age == 25
        assert user.phone == '!@#$%^&*()'

    def test_create_custom_user_without_age_and_phone(self):
        user = CustomUser.objects.create(username='testuser2')
        assert user.age is None
        assert user.phone is None

    def test_age_field_non_negative(self):
        with pytest.raises(Exception, match='CHECK constraint failed: age'):
            CustomUser.objects.create(
                username='testuser', age=-5, phone='1234567890')
