from django.contrib import admin

# Register your models here.
from .models import Hero, yourMom, Contact, Debate, Argument, Counter_argument, Debate_vote, Argument_vote, Counter_argument_vote, Voting_right, Usergroup, Usergroup_contact
admin.site.register(Hero)
admin.site.register(yourMom)
admin.site.register(Contact)
admin.site.register(Debate)
admin.site.register(Argument)
admin.site.register(Counter_argument)
admin.site.register(Debate_vote)
admin.site.register(Argument_vote)
admin.site.register(Counter_argument_vote)
admin.site.register(Voting_right)
admin.site.register(Usergroup)
admin.site.register(Usergroup_contact)