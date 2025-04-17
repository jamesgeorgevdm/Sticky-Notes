from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import PostForm

# Views for handling post-related actions in the Django app.

def post_list(request):
    """
    View to display a list of all posts.

    :param request: HTTP request object.
    :return: Rendered template with a list of posts.
    """
    posts = Note.objects.all()

    # Context dictionary to pass data to the template
    context = {
        "posts": posts,
        "page_title": "List of Posts"
    }

    return render(request, "notes_app/post_list.html", context)


def post_detail(request, pk):
    """
    View to display details of a specific post.

    :param request: HTTP request object.
    :param pk: Primary key of the post to retrieve.
    :return: Rendered template with post details.
    """
    post = get_object_or_404(Note, pk=pk)
    return render(request, "notes_app/post_detail.html", {"post": post})


def post_create(request):
    """
    View to create a new post.

    :param request: HTTP request object.
    :return: Rendered form template for post creation, or redirects to post list on success.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Save form data without committing immediately
            post.save()
            return redirect("post_list")  # Redirect to list of posts after successful creation
    else:
        form = PostForm()  # Display empty form for new post creation
    
    return render(request, "notes_app/post_form.html", {"form": form})


def post_update(request, pk):
    """
    View to update an existing post.

    :param request: HTTP request object.
    :param pk: Primary key of the post to be updated.
    :return: Rendered form template for editing a post, or redirects to post list on success.
    """
    post = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)  # Apply updates before saving
            post.save()
            return redirect("post_list")  # Redirect after successful update
    else:
        form = PostForm(instance=post)  # Pre-fill form with existing post data

    return render(request, "notes_app/post_form.html", {"form": form})


def post_delete(request, pk): 
    """
    View to delete an existing post.

    :param request: HTTP request object.
    :param pk: Primary key of the post to be deleted.
    :return: Redirect to the post list after deletion.
    """
    post = get_object_or_404(Note, pk=pk)
    post.delete()  # Remove post from the database
    return redirect("post_list")  # Redirect back to post list
