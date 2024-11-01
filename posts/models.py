from django.core.validators import MinLengthValidator
from django.db import models
from FurryFunnies.author.models import Author


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        error_messages={"unique": "Oops! That title is already taken. How about something fresh and fun?"}
    )

    image_url = models.URLField(
        help_text="Share your funniest furry photo URL!",
    )

    content = models.TextField()
    updated_at = models.DateField(
        auto_now=True
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    class Meta:
        db_table = 'posts_post'

    def __str__(self):
        return self.title
