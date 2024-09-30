from django.db import models
# we need a custom user model that stores the user's account information and collection of chinese characters
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from lookup.models import Word


class User(AbstractUser):
    # we need a field to store the user's collection of chinese characters
    collection = models.ManyToManyField(Word, related_name='users', blank=True)
    class Meta:
        db_table = 'auth_user'

@receiver(post_save, sender=User)
# we need a signal to create a user's collection when a new user is created
def create_user_collection(sender, instance, created, **kwargs):
    if created:
        instance.collection = Word.objects.all()
        instance.save()


@receiver(post_save, sender=User)
# we need a signal to update a user's collection when a user is updated
def update_user_collection(sender, instance, created, **kwargs):
    instance.collection = Word.objects.all()
    instance.save()


@receiver(models.signals.post_delete, sender=User)
# we need a signal to delete a user's collection when a user is deleted
def delete_user_collection(sender, instance, **kwargs):
    instance.collection.clear()


@receiver(post_save, sender=Word)
# we need a signal to update a user's collection when a chinese character is updated
def update_user_collections(sender, instance, created, **kwargs):
    for user in User.objects.all():
        user.collection.add(instance)
        user.save()
