from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Post
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)


@receiver(post_save, sender=Post)
def audit_log(sender, instance, **kwargs):
    logging.info(f'{sender} {instance} was created')


@receiver(pre_save, sender=Post)
def audit_log(sender, instance, **kwargs):
    logging.info(f'{sender} {instance} ready to be created')

