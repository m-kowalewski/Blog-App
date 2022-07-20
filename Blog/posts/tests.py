""" test file for posts app """
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from freezegun import freeze_time
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestCreatePost(TestCase):

    @freeze_time("2022-07-20 10:11:12")
    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user1',
            password='1234567890'
        )
        test_user.save()
        test_post = Post.objects.create(
            title='Post title',
            body='Post body',
            owner=test_user
        )
        test_post.save()

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        created = f'{post.created}'
        title = f'{post.title}'
        body = f'{post.body}'
        owner = f'{post.owner}'
        self.assertEqual(created, '2022-07-20 10:11:12+00:00')
        self.assertEqual(title, 'Post title')
        self.assertEqual(body, 'Post body')
        self.assertEqual(owner, 'test_user1')


class TestAPI(APITestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user1',
            password='1234567890'
        )
        test_user.save()

    def test_view_posts(self):
        url = reverse('posts:posts_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_creation_api(self):
        data = {
            'title': 'test_title_API',
            'body': 'test_body_API',
        }
        self.client = APIClient()
        self.client.login(username='test_user1', password='1234567890')
        url = reverse('posts:posts_list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
