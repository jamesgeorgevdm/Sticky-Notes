
# posts/tests.py 
from django.test import TestCase 
from django.urls import reverse 
from .models import Note, Author 
 
class NoteModelTest(TestCase): 
    def setUp(self): 
        # Create an Author object 
        author = Author.objects.create(name='Test Author') 
        # Create a Post object for testing 
        Note.objects.create(title='Test Post', content='This is a test post.', author=author) 
 
    def test_post_has_title(self): 
        # Test that a Post object has the expected title 
        post = Note.objects.get(id=1) 
        self.assertEqual(post.title, 'Test Post') 
 
    def test_post_has_content(self): 
        # Test that a Post object has the expected content 
        post = Note.objects.get(id=1) 
        self.assertEqual(post.content, 'This is a test post.') 

class PostCreationTest(TestCase):
    def setUp(self):
        """ Set up an author for post creation. """
        self.author = Author.objects.create(name="Test Author")

    def test_post_creation_view(self):
        """ Test that a new post can be created through the form submission. """
        response = self.client.post(reverse("post_create"), {
            "title": "New Test Post",
            "content": "This is a newly created test post.",
            "author": self.author.id
        })
        
        # Retrieve the post from the database
        self.assertEqual(Note.objects.count(), 1)  # Ensure only one post exists
        post = Note.objects.first()
        self.assertEqual(post.title, "New Test Post")
        self.assertEqual(post.content, "This is a newly created test post.")

        # Verify redirection after creation
        self.assertRedirects(response, reverse("post_list"))
 
class PostViewTest(TestCase): 
    def setUp(self): 
        # Create an Author object 
        author = Author.objects.create(name='Test Author') 
        # Create a Post object for testing views 
        Note.objects.create(title='Test Post', content='This is a test post.', author=author) 
 
    def test_post_list_view(self): 
        # Test the post-list view 
        response = self.client.get(reverse('post_list')) 
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'Test Post') 
 
    def test_post_detail_view(self): 
        # Test the post-detail view 
        post = Note.objects.get(id=1) 
        response = self.client.get(reverse('post_detail', args=[str(post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post') 
        self.assertContains(response, 'This is a test post.') 
    
    def test_post_update(self):
        # Test the update function
        post = Note.objects.get(id=1)
        post.title = "Updated Post"
        post.save()
        self.assertEqual(post.title, "Updated Post")

    def test_post_delete(self):
        # Test the delete function
        post = Note.objects.get(id=1)
        post.delete()
        self.assertEqual(Note.objects.count(), 0)

