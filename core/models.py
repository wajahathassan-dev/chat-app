from django.db import models
from uuid import uuid4

# User

class User(models.Model):
    id                  =   models.CharField(max_length=36, default=uuid4, primary_key=True)
    first_name          =   models.CharField(max_length=255)
    last_name           =   models.CharField(max_length=255)
    profile_photo       =   models.ImageField(blank=True)
    phone_no            =   models.CharField(max_length=255)
    description         =   models.CharField(max_length=300, blank=True)
    is_active           =   models.BooleanField(default=True)


# Contact

class Contact(models.Model):
    id                   =   models.CharField(max_length=36, default=uuid4, primary_key=True)
    user                 =   models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_set')
    contact              =   models.ForeignKey(User, on_delete=models.CASCADE)


# Message  ( One user to another )
 
class Message(models.Model):
    id                   =   models.CharField(max_length=36, default=uuid4, primary_key=True)
    sender               =   models.ForeignKey(User, on_delete=models.CASCADE, related_name="senderset")
    receiver             =   models.ForeignKey(User, on_delete=models.CASCADE)
    message_text         =   models.TextField()
    sent_at              =   models.DateTimeField(auto_now_add=True)


# Group

class Group(models.Model):
    id                   =   models.CharField(max_length=36, default=uuid4, primary_key=True)
    name                 =   models.CharField(max_length=255)
    description          =   models.CharField(max_length=300)
    created_at           =   models.DateTimeField(auto_now_add=True)


# UserGroup

ROLE_CHOICES = [
    ('R', 'REGULAR'),
    ('A', 'ADMIN'),
]

DEFAULT_ROLE = ROLE_CHOICES[0][0]

class UserGroup(models.Model):
    id                   =   models.CharField(max_length=36, default=uuid4, primary_key=True)
    user                 =   models.ForeignKey(User, on_delete=models.CASCADE)
    group                =   models.ForeignKey(Group, on_delete=models.CASCADE)
    role                 =   models.CharField(max_length=255, choices=ROLE_CHOICES, default=DEFAULT_ROLE)
    added_at             =   models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'group')


# GroupMessage

class GroupMessage(models.Model):
    id                   =   models.CharField(max_length=36, default=uuid4, primary_key=True)
    sender               =   models.ForeignKey(User, on_delete=models.CASCADE)
    group                =   models.ForeignKey(Group, on_delete=models.CASCADE)
    message_text         =   models.TextField()
    sent_at              =   models.DateTimeField(auto_now_add=True)