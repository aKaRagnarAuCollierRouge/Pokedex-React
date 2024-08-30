from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import TypeAccount

@receiver(post_save, sender=User)
def create_default_type_account(sender, instance, created, **kwargs):
    if created:
        default_type_account, created = TypeAccount.objects.get_or_create(name='Gratuit')

        instance.type_account = default_type_account
        instance.save()