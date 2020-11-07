from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#class Contact(models.Model):
#    USER = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
#    ID = models.AutoField(primary_key=True)
#    CREATED_AT = models.DateTimeField(auto_now_add=True)
#    @receiver(post_save, sender=User)
#    def create_user_profile(sender, instance, created, **kwargs):
#        if created:
#            Contact.objects.create(user=instance)
#    @receiver(post_save, sender=User)
#    def save_user_profile(sender, instance, **kwargs):
#        instance.Contact.save()
#    def __str__(self):
#        return self.ID

class Debate(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=60)
    YES_TITLE = models.CharField(max_length=100)
    NO_TITLE = models.CharField(max_length=100)
    CONTEXT = models.CharField(max_length=1000, blank=True, null=True)
    PHOTO_PATH = models.CharField(max_length=150, blank=True, null=True)
    YES_SCORE = models.IntegerField(blank=True, null=True)
    NO_SCORE = models.IntegerField(blank=True, null=True)
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.NAME

class Argument(models.Model):
    ID = models.AutoField(primary_key=True)
    TITLE = models.CharField(max_length=200)
    TEXT = models.CharField(max_length=600, blank=True, null=True)
    DEBATE_ID = models.ForeignKey(Debate, on_delete=models.CASCADE)
    SCORE = models.IntegerField(blank=True, null=True)
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    SIDE = models.CharField(max_length=3)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.TEXT

class Counter_argument(models.Model):
    ID = models.AutoField(primary_key=True)
    TITLE = models.CharField(max_length=200)
    TEXT = models.CharField(max_length=600, blank=True, null=True)
    ARGUMENT_ID = models.ForeignKey(Argument, on_delete=models.CASCADE)
    SCORE = models.IntegerField(blank=True, null=True)
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.TEXT

class Debate_vote(models.Model):
    ID = models.AutoField(primary_key=True)
    SIDE = models.CharField(max_length=3)
    DEBATE_ID = models.ForeignKey(Debate, on_delete=models.CASCADE)
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.SIDE

class Argument_vote(models.Model):
    ID = models.AutoField(primary_key=True)
    ARGUMENT_ID = models.ForeignKey(Argument, on_delete=models.CASCADE)
    SCORE = models.IntegerField()
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.SCORE

class Counter_argument_vote(models.Model):
    ID = models.AutoField(primary_key=True)
    COUNTER_ARGUMENT_ID = models.ForeignKey(Counter_argument, on_delete=models.CASCADE)
    SCORE = models.IntegerField()
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.SCORE

class Voting_right(models.Model):
    DEBATE_ID = models.ForeignKey(Debate, on_delete=models.CASCADE)
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.DEBATE_ID, self.CONTACT_ID