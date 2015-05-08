from django.db.models.signals import pre_save
from django.dispatch import receiver
from idehco3.community.models import MembershipCommunity


@receiver(pre_save, sender=MembershipCommunity)
def my_handler(sender, **kwargs):
    pass
