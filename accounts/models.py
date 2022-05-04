from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE,  related_name="profile")
    profile_image = models.ImageField(
        upload_to='static/images/', default='./images/user.png', null=True, blank=True)
    dob = models.DateField(default=date.today)
    phone = models.IntegerField(default=0)
    email = models.EmailField(default='')
    ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.user.username


User.accounts = property(
    lambda u: Profile.objects.get_or_create(user=u)[0])


#   from django.contrib.auth.models import User
#   from accounts.models import Profile
#   from django.contrib.auth import get_user_model
#   User = get_user_model()
#   users = User.objects.filter(profile=None)
#   for user in users:
#       Profile.objects.create(user=user)
