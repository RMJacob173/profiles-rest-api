from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""
    #function to manipulate or make change to UserProfile
    def create_user(self,email,name,password=None): #default password value is None
        """Creating a new user"""
        if not email:#empty or null
            raise ValueError("User Must Have An Email Address")

        #normalise email Address i.e makes the second half of the email address to lower
        email = self.normalize_email(email)
        user = self.model(email =email, name=name)

        user.set_password(password) #encrots passord
        user.save(using = self._db) #to consider support for multiple databases
        return user

    #to create a super user
    def create_superuser(self,email,name, password):
        user = self.create_user(email,name,passord)
        user.is_superuser = True #Automatically created by PermissionMixin
        user.is_staff = True
        user.save(using = self._db)
        return user




class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database models for the users in the system"""

    email = models.EmailField(max_length=255, unique = True) #unique email id
    name = models.CharField(max_length=255)
    #add files for the permission system
    is_active = models.BooleanField(default = True)#allows to deactivate user
    is_staff = models.BooleanField(default=False)#admin or users

    #to create a custom model manager
    objects = UserProfileManager()

    #to override the default username field
    USERNAME_FIELD ="email"
    REQUIRED_FIELD =["name"]

    def get_full_name(self):
        """Return the fill name"""
        return self.name

    def get_short_name(self):
        """Return short name"""
        return self.name

    def __str__(self):
        return self.email # strng representing the users
