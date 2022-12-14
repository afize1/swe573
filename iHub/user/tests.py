from django.test import TestCase
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import users,shares



class createUserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test",first_name="testname", last_name="testlastname", email="test@test.com",password="1234Test")
        self.user = users.objects.create(username="test", answer="test12", security_question="1" )
        self.user= shares.objects.create( username="test",subject= "django",label = "development",private = "1",type = "1", content="text", description = "nice test")
        self.user.save()

    def test_loginTest(self):
        user = authenticate(username='test', password='1234Test')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_loginWrongName(self):
        user = authenticate(username='test12', password='1234Test')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_LoginWrongPassword(self):
        user = authenticate(username='test', password='1234Test1234')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_forgotPassword(self):
        user = users.objects.filter(username="test")
        self.assertEqual(user[0].security_question, "1")
        self.assertEqual(user[0].answer, "test12")

    def test_createPost(self):
        user = users.objects.filter(username="test")
        self.assertEqual(user[0].subject, "django")
        self.assertEqual(user[0].label, "development")
        self.assertEqual(user[0].private, "1")
        self.assertEqual(user[0].type, "1")
        self.assertEqual(user[0].content, "text")
        self.assertEqual(user[0].description, "nice test")





