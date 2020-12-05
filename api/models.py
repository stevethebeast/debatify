import collections, sys, json
from django.db import models, connection
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

class DebateManager(models.Manager):
    def with_debatevotes(self, user):
        with connection.cursor() as cursor:
            cursor.execute("SELECT ad.\"ID\" DEBATE_ID, ad.\"NAME\", ad.\"YES_TITLE\", ad.\"NO_TITLE\", ad.\"CONTEXT\", ad.\"PHOTO_PATH\", ad.\"CREATOR_ID_id\" CREATOR_ID, CAST(ad.\"CREATED_AT\" AS VARCHAR) CREATED_AT, adv.CONTACT_ID, adv.\"SIDE\", adv.\"ID\"\
                FROM api_debate AS ad LEFT OUTER JOIN \
                (SELECT \"ID\", \"DEBATE_ID_id\" DEBATE_ID, \"CONTACT_ID_id\" CONTACT_ID, \"SIDE\"\
                FROM api_debate_vote\
                WHERE \"CONTACT_ID_id\"=%s) adv ON ad.\"ID\"=adv.DEBATE_ID;", [user])
            objects_list = []
            for row in cursor.fetchall():
                #sys.stderr.write("LINES" + str(row[0]) + str(row[1]) + str(row[2]) + str(row[3]))
                d = collections.OrderedDict()
                d["ID"] = row[0]
                d["NAME"] = row[1]
                d["YES_TITLE"] = row[2]
                d["NO_TITLE"] = row[3]
                d["CONTEXT"] = row[4]
                d["PHOTO_PATH"] = row[5]
                d["CREATOR_ID"] = row[6]
                d["CREATED_AT"] = row[7]
                d["CONTACT_ID"] = row[8]
                d["SIDE"] = row[9]
                d["VOTE_ID"] = row[10]
                objects_list.append(d)
        return objects_list

class Debate(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=60)
    YES_TITLE = models.CharField(max_length=100)
    NO_TITLE = models.CharField(max_length=100)
    CONTEXT = models.CharField(max_length=1000, blank=True, null=True)
    PHOTO_PATH = models.CharField(max_length=150, blank=True, null=True)
    CREATOR_ID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    objects = DebateManager()

class ArgumentManager(models.Manager):
    def with_argumentlikes(self, argument, user):
        with connection.cursor() as cursor:
            cursor.execute("SELECT arg.\"ID\" ARGUMENT_ID, arg.\"TITLE\", arg.\"TEXT\", arg.\"SCORE\", arg.\"SIDE\", arg.\"CREATED_AT\", arg.\"CONTACT_ID_id\" CONTACT_ID, arg.\"DEBATE_ID_id\" DEBATE_ID\
                FROM api_argument AS arg LEFT OUTER JOIN\
                (SELECT \"LIKE\", \"ARGUMENT_ID_id\" ARGUMENT_ID\
                FROM api_argument_vote\
                WHERE \"CONTACT_ID_id\"=%s AND \"ARGUMENT_ID_id\"=%s) av ON arg.\"ID\" = av.ARGUMENT_ID;", [user, argument])
            objects_list = []
            for row in cursor.fetchall():
                #sys.stderr.write("LINES" + str(row[0]) + str(row[1]) + str(row[2]) + str(row[3]))
                d = collections.OrderedDict()
                d["ID"] = row[0]
                d["TITLE"] = row[1]
                d["TEXT"] = row[2]
                d["SCORE"] = row[3]
                d["SIDE"] = row[4]
                d["CREATED_AT"] = row[5]
                d["CONTACT_ID"] = row[6]
                d["DEBATE_ID"] = row[7]
                objects_list.append(d)
        return objects_list
    def with_debateargumentlikes(self, argument, user):
        with connection.cursor() as cursor:
            cursor.execute("SELECT arg.\"ID\" ARGUMENT_ID, arg.\"TITLE\", arg.\"TEXT\", arg.\"SCORE\", arg.\"SIDE\", arg.\"CREATED_AT\", av.\"CONTACT_ID_id\" CONTACT_ID, arg.\"DEBATE_ID_id\" DEBATE_ID, av.\"ID\", av.\"LIKE\"\
                            FROM api_argument AS arg LEFT OUTER JOIN\
                            (SELECT \"ID\", \"LIKE\", \"ARGUMENT_ID_id\" ARGUMENT_ID, \"CONTACT_ID_id\"\
                            FROM api_argument_vote\
                            WHERE \"CONTACT_ID_id\"=%s\
                            ) av ON arg.\"ID\" = av.ARGUMENT_ID\
                            WHERE arg.\"DEBATE_ID_id\"=%s;", [user, argument])
            objects_list = []
            for row in cursor.fetchall():
                #sys.stderr.write("LINES" + str(row[0]) + str(row[1]) + str(row[2]) + str(row[3]))
                d = collections.OrderedDict()
                d["ID"] = row[0]
                d["TITLE"] = row[1]
                d["TEXT"] = row[2]
                d["SCORE"] = row[3]
                d["SIDE"] = row[4]
                d["CREATED_AT"] = row[5]
                d["CONTACT_ID"] = row[6]
                d["DEBATE_ID"] = row[7]
                d["VOTE_ID"] = row[8]
                d["LIKE"] = row[9]
                objects_list.append(d)
        return objects_list
        
class Argument(models.Model):
    ID = models.AutoField(primary_key=True)
    TITLE = models.CharField(max_length=200)
    TEXT = models.CharField(max_length=600, blank=True, null=True)
    DEBATE_ID = models.ForeignKey(Debate, on_delete=models.CASCADE)
    SCORE = models.IntegerField(default=0, null=False)
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    SIDE = models.CharField(max_length=3)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    objects = ArgumentManager()

class CounterArgumentManager(models.Manager):
    def with_counterargumentlikes(self, argument, user):
        with connection.cursor() as cursor:
            cursor.execute("SELECT arg.\"ID\" COUNTER_ARGUMENT_ID, arg.\"TITLE\", arg.\"TEXT\", arg.\"SCORE\", arg.\"CREATED_AT\", arg.\"CONTACT_ID_id\" CONTACT_ID, arg.\"ID\" ARGUMENT_ID\
                FROM api_counter_argument AS arg LEFT OUTER JOIN\
                (SELECT \"LIKE\", \"COUNTER_ARGUMENT_ID_id\" COUNTER_ARGUMENT_ID\
                FROM api_counter_argument_vote\
                WHERE \"CONTACT_ID_id\"=%s AND \"COUNTER_ARGUMENT_ID_id\"=%s) av ON arg.\"ID\" = av.COUNTER_ARGUMENT_ID;", [user, argument])
            objects_list = []
            for row in cursor.fetchall():
                #sys.stderr.write("LINES" + str(row[0]) + str(row[1]) + str(row[2]) + str(row[3]))
                d = collections.OrderedDict()
                d["COUNTER_ARGUMENT_ID"] = row[0]
                d["TITLE"] = row[1]
                d["TEXT"] = row[2]
                d["SCORE"] = row[3]
                d["CREATED_AT"] = row[4]
                d["CONTACT_ID"] = row[5]
                d["ARGUMENT_ID"] = row[6]
                objects_list.append(d)
        return objects_list
    def with_userchoices(self, argument, user):
        with connection.cursor() as cursor:
            cursor.execute("SELECT ca.\"ID\", ca.\"TITLE\", ca.\"TEXT\", ca.\"ARGUMENT_ID_id\", ca.\"SCORE\", ca.\"CONTACT_ID_id\", ca.\"CREATED_AT\", cav.\"ID\", cav.\"LIKE\"\
                            FROM api_counter_argument ca LEFT OUTER JOIN\
                            (SELECT \"ID\",\"LIKE\", \"COUNTER_ARGUMENT_ID_id\"\
                            FROM api_counter_argument_vote\
                            WHERE \"CONTACT_ID_id\"=%s) cav ON cav.\"COUNTER_ARGUMENT_ID_id\" = ca.\"ID\"\
                            WHERE ca.\"ARGUMENT_ID_id\"=%s;", [user, argument])
            objects_list = []
            for row in cursor.fetchall():
                #sys.stderr.write("LINES" + str(row[0]) + str(row[1]) + str(row[2]) + str(row[3]))
                d = collections.OrderedDict()
                d["ID"] = row[0]
                d["TITLE"] = row[1]
                d["TEXT"] = row[2]
                d["ARGUMENT_ID"] = row[3]
                d["SCORE"] = row[4]
                d["CONTACT_ID"] = row[5]
                d["CREATED_AT"] = row[6]
                d["VOTE_ID"] = row[7]
                d["LIKE"] = row[8]
                objects_list.append(d)
        return objects_list

class Counter_argument(models.Model):
    ID = models.AutoField(primary_key=True)
    TITLE = models.CharField(max_length=200)
    TEXT = models.CharField(max_length=600, blank=True, null=True)
    ARGUMENT_ID = models.ForeignKey(Argument, on_delete=models.CASCADE, blank=True, null=False)
    SCORE = models.IntegerField(default=0, null=False)
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    objects = CounterArgumentManager()

class Debate_vote(models.Model):
    ID = models.AutoField(primary_key=True)
    SIDE = models.CharField(max_length=3)
    DEBATE_ID = models.ForeignKey(Debate, on_delete=models.CASCADE, blank=True, null=False)
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("DEBATE_ID", "CONTACT_ID"),)

class Argument_vote(models.Model):
    ID = models.AutoField(primary_key=True)
    ARGUMENT_ID = models.ForeignKey(Argument, on_delete=models.CASCADE, blank=True, null=False)
    LIKE = models.IntegerField()
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("ARGUMENT_ID", "CONTACT_ID"),)

class Counter_argument_vote(models.Model):
    ID = models.AutoField(primary_key=True)
    COUNTER_ARGUMENT_ID = models.ForeignKey(Counter_argument, on_delete=models.CASCADE, blank=True, null=False)
    LIKE = models.IntegerField()
    CONTACT_ID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("COUNTER_ARGUMENT_ID", "CONTACT_ID"),)