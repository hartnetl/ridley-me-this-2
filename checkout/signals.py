from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from orders.models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    Handles signals from the post save event
    """
    instance.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.update_total()
