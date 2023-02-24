from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views, tokens
from .social_auth import views as SocialViews

router = routers.DefaultRouter()
router.register(r'Arguments', views.ArgumentViewSet)
router.register(r'Debates', views.DebateViewSet)
router.register(r'CounterArguments', views.CounterArgumentViewSet)
router.register(r'DebateVotes', views.DebateVoteViewSet)
router.register(r'ArgumentVotes', views.ArgumentVoteViewSet)
router.register(r'CounterArgumentVotes', views.CounterArgumentVoteViewSet)
router.register(r'Picture', views.PictureViewSet)
router.register(r'ChatComments', views.ChatCommentViewSet, basename="ChatCommentViewSet")
router.register(r'DebateTop20byActivity', views.DebateTop20ActivityViewSet, basename="DebateTop20ActivityViewSet")
router.register(r'RecentChatComments', views.RecentChatCommentsViewSet, basename="RecentChatCommentsViewSet")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^searchdebatesbynameandtitles$', views.SearchDebatesAPIView.as_view()),
    url(r'^ListDebatesWithUserChoices$', views.ListDebatesWithUserChoices),
    url(r'^ListCounterArgumentsWithUserChoices$', views.ListCounterArgumentsWithUserChoices),
    url(r'^ListArgumentsWithUserChoices$', views.ListArgumentsWithUserChoices),
    url(r'^debatevotesbydebateid$', views.DebateVotesbyDebateId),
    url(r'^GetTokenUsername$', views.GetTokenUsername),
    url(r'^GetUserHistory$', views.UserHistory),
    path(r'activate/<uidb64>/<token>/', views.activate, name='activate'),
    path(r'reset/<uidb64>/<token>/', views.reset, name='reset'),
    path('createusercpt/', views.recaptcha_valid),
    path('logincpt/', views.logincpt),
    path('emailpasswordreset/', views.email_password_reset),
    path('change_password/', views.change_password),
    #path('google/', SocialViews.GoogleSocialAuthView.as_view()),
    #path('facebook/', SocialViews.FacebookSocialAuthView.as_view()),
    #path('twitter/', SocialViews.TwitterSocialAuthView.as_view()),
]
