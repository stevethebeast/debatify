from django.contrib import admin

# Register your models here.
from .models import Debate, Argument, Counter_argument, Debate_vote, Argument_vote, Counter_argument_vote, User, ChatComment, RecentChatComments, Picture
admin.site.register(User)
admin.site.register(Debate)
admin.site.register(Argument)
admin.site.register(Counter_argument)
admin.site.register(Debate_vote)
admin.site.register(Argument_vote)
admin.site.register(Counter_argument_vote)
admin.site.register(ChatComment)
admin.site.register(RecentChatComments)
admin.site.register(Picture)