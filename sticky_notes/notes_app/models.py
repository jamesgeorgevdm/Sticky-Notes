from django.db import models

class Note(models.Model):
    """
    Model representing a note.
    
    Attributes:
        title (CharField): The title of the note, limited to 255 characters.
        content (TextField): The main content of the note.
        created_at (DateTimeField): Timestamp indicating when the note was created.
        author (ForeignKey): A reference to the Author model, allowing optional ownership.
    """
    title = models.CharField(max_length=255)  # Note title with character limit
    content = models.TextField()  # Main body of the note
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-filled timestamp when created
    
    # ForeignKey for author relationship (optional, allows NULL values)
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        """
        Returns a string representation of the note (its title).
        """
        return self.title


class Author(models.Model):
    """
    Model representing an author.
    
    Attributes:
        name (CharField): The name of the author, limited to 255 characters.
    
    Note: 
        Placeholder class for potential future authentication integration.
    """
    name = models.CharField(max_length=255)  # Author's name field

    def __str__(self):
        """
        Returns a string representation of the author (their name).
        """
        return self.name
