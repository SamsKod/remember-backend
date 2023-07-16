from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='sam', password='123Test')

    def test_can_list_posts(self):
        sam = User.objects.get(username='sam')
        Post.objects.create(owner=sam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='sam', password='123Test')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_can_not_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
	def setUp(self):
		sam = User.objects.create_user(username='sam', password='123Test')
		erik = User.objects.create_user(username='erik', password='123Test')
		Post.objects.create(
            owner=sam, title='a title', content='sams content'
            )
		Post.objects.create(
            owner=erik, title='another title', content='eriks content'
            )


	def test_logged_in_user_can_retrive_post_valid_id(self):
		response = self.client.get('/posts/1/')
		self.assertEqual(response.data['title'], 'a title')
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_logged_in_user_can_not_retrive_post_valid_id(self):
		response = self.client.get('/posts/999/')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


	def test_user_can_update_own_post(self):
		self.client.login(username='sam', password='123Test')
		response = self.client.put('/posts/1/', {'title': 'a new title'})
		post = Post.objects.filter(pk=1).first()
		self.assertEqual(post.title, 'a new title')
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_user_can_not_update_others_post(self):
		self.client.login(username='erik', password='123Test')
		response = self.client.put('/posts/1/', {'title': 'a new title'})
		post = Post.objects.filter(pk=1).first()
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
