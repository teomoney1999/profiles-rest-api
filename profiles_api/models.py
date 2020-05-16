from django.db import models

# Standard base classes use when overriding or customizing 
# the default django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager): 
    """Manager for user profile"""

    def create_user(self, email, name, password=None): 
        """Create a new user profile"""
        if not email: 
            raise ValueError('User must have email address')
        email = self.normalize_email(email) 
        user = self.model(email=email, name=name)

        user.set_password(password)                 # password is encrypted
        user.save(using=self._db)                   # support multiple database

        return user

    def create_superuser(self, email, name, password): 
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True                    # auto create allow by PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)

        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin): 
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom model manager for user model
    objects = UserProfileManager()

    # Work with Django admin and Django authentication system
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self): 
        """Retrive full name of user"""
        return self.name
    
    def get_short_name(self): 
        """Retrive short name of user"""
        return self.name
    
    def __str__(self): 
        """Return string representation of our user"""
        return self.email

