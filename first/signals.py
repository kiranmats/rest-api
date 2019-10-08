from .models import Author, Score
from django.db.models.signals import post_save
from django.dispatch import receiver


# Sender is Author
@receiver(post_save, sender=Author)
def create_score_user(sender, instance, created, **kwargs):
    if created:
        Score.objects.create(author=instance)
        print("Score card for Author created")
