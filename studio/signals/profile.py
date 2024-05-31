import logging
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from studio.models import Profile
from reveal_studio.settings import AUTH_USER_MODEL


logger = logging.getLogger(__name__)

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s profile created")

