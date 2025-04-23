from django.db import models
from .mixins import AbstractTrack
from django.contrib.auth.models import AbstractUser
from core.validators import validate_phone_number
from core.managers import UserManager

# Create your models here.
class User(AbstractUser, AbstractTrack):

    phone = models.CharField(max_length=15, unique=True, validators=[validate_phone_number])
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)
    # @cached_property
    # def is_master_admin(self):
    #     return self.in_group(UserGroup.MASTER_ADMIN.value)
    
    # @cached_property
    # def is_group_admin(self):
    #     return self.in_group(UserGroup.GROUP_ADMIN.value)
    
