from django.db import models

class Contact(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=100)
    EMAIL = models.CharField(max_length=50)
    PASSWORD = models.CharField(max_length=15)
    def __str__(self):
        return self.NAME

class Debate(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=60)
    YES_TITLE = models.CharField(max_length=100)
    NO_TITLE = models.CharField(max_length=100)
    CONTEXT = models.CharField(max_length=1000)
    PHOTO_PATH = models.CharField(max_length=150)
    YES_SCORE = models.IntegerField()
    NO_SCORE = models.IntegerField()
    CONTACT_ID = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return self.NAME

class Argument(models.Model):
    ID = models.AutoField(primary_key=True)
    TITLE = models.CharField(max_length=200)
    TEXT = models.CharField(max_length=600)
    DEBATE_ID = models.ForeignKey(Debate, on_delete=models.CASCADE)
    SCORE = models.IntegerField()
    CONTACT_ID = models.ForeignKey(Contact, on_delete=models.CASCADE)
    SIDE = models.CharField(max_length=3)
    def __str__(self):
        return self.TEXT

class Counter_argument(models.Model):
    ID = models.AutoField(primary_key=True)
    TITLE = models.CharField(max_length=200)
    TEXT = models.CharField(max_length=600)
    ARGUMENT_ID = models.ForeignKey(Argument, on_delete=models.CASCADE)
    SCORE = models.IntegerField()
    CONTACT_ID = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return self.TEXT

class Debate_vote(models.Model):
    ID = models.AutoField(primary_key=True)
    SIDE = models.CharField(max_length=3)
    DEBATE_ID = models.ForeignKey(Debate, on_delete=models.CASCADE)
    CONTACT_ID = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return self.SIDE

class Argument_vote(models.Model):
    ID = models.AutoField(primary_key=True)
    ARGUMENT_ID = models.ForeignKey(Argument, on_delete=models.CASCADE)
    SCORE = models.IntegerField()
    CONTACT_ID = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return self.SCORE

class Counter_argument_vote(models.Model):
    ID = models.AutoField(primary_key=True)
    COUNTER_ARGUMENT_ID = models.ForeignKey(Counter_argument, on_delete=models.CASCADE)
    SCORE = models.IntegerField()
    CONTACT_ID = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return self.SCORE

class Voting_right(models.Model):
    DEBATE_ID = models.ForeignKey(Debate, on_delete=models.CASCADE)
    CONTACT_ID = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return self.DEBATE_ID, self.CONTACT_ID