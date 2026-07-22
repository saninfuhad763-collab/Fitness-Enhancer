from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Subscription

@receiver(post_save, sender=User)
def create_user_profile_and_subscription(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(
            user=instance,
            defaults={
                'age': 30,
                'height': 170.0,
                'weight': 70.0,
                'goal': 'fitness'
            }
        )
        Subscription.objects.get_or_create(
            user=instance,
            defaults={'plan': 'free'}
        )
