from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views, tokens

router = routers.DefaultRouter()
#router.register(r'Contacts', views.ContactViewSet)
router.register(r'Arguments', views.ArgumentViewSet)
router.register(r'Debates', views.DebateViewSet)
router.register(r'CounterArguments', views.CounterArgumentViewSet)
router.register(r'DebateVotes', views.DebateVoteViewSet)
router.register(r'ArgumentVotes', views.ArgumentVoteViewSet)
router.register(r'CounterArgumentVotes', views.CounterArgumentVoteViewSet)
router.register(r'Category', views.CategoryViewSet)
router.register(r'ChatComments', views.ChatCommentViewSet, basename="ChatCommentViewSet")
router.register(r'DebateTop20byActivity', views.DebateTop20ActivityViewSet)
#router.register(r'UserGrhellooupContacts', views.hello, basename= 'test')
#router.register(r'test', views.hello)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^argumentsbydebateid$', views.ListOfArguments),
    #url(r'^counterargumentsbyid$', views.ListOfCounterArguments),
    url(r'^searchdebatesbynameandtitles$', views.SearchDebatesAPIView.as_view()),
    url(r'^GetOrCreateDebateVote$', views.GetOrCreateDebateVote),
    url(r'^ListDebatesWithUserChoices$', views.ListDebatesWithUserChoices),
    url(r'^ListCounterArgumentsWithUserChoices$', views.ListCounterArgumentsWithUserChoices),
    url(r'^ListArgumentsWithUserChoices$', views.ListArgumentsWithUserChoices),
    url(r'^debatevotesbydebateid$', views.DebateVotesbyDebateId),
    #url(r'^createuser/$', views.CreateUserWithConfirmation),
    #url(r'^GetAllDebatesWithVotersBySideAndID$', views.GetAllDebatesWithVotersBySideAndID),
    #url(r'^GetAllArgumentsWithVotersByID$', views.GetAllArgumentsWithVotersByID),
    url(r'^GetTokenUsername$', views.GetTokenUsername),
    url(r'^GetUserHistory$', views.UserHistory),
    path(r'activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('contact/', views.contact),
    path('createusercpt/', views.recaptcha_valid),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published)
]
