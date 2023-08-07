# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from authentication.models import User
# from django.conf import settings 


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     print("create_auth_token")
#     if created:
#         t = Token.objects.create(user=instance)
#         print("token")
#         print(t)