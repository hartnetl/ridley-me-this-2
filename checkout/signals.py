from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from orders.models import Order


@receiver(post_save, sender=Order)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    Handles signals from the post save event
    """
    instance.get_total()
    instance.update_total()


@receiver(post_delete, sender=Order)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.get_total()
    instance.update_total()
