from django.db import models


class Video(models.Model):

    CATEGORY_CHOICES = [
        ("reels", "Reels & Shorts"),
        ("youtube", "YouTube"),
        ("cinematic", "Cinematic"),
        ("motion", "Motion Graphics"),
    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField(
        blank=True
    )

    video = models.FileField(
        upload_to="videos/"
    )

    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
        null=True
    )

    featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title