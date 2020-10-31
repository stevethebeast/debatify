from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'moms', views.MomViewSet)
router.register(r'Contacts', views.ContactViewSet)
router.register(r'Arguments', views.ArgumentViewSet)
router.register(r'Debates', views.DebateViewSet)
router.register(r'CounterArguments', views.CounterArgumentViewSet)
router.register(r'DebateVotes', views.DebateVoteViewSet)
router.register(r'ArgumentVotes', views.ArgumentVoteViewSet)
router.register(r'CounterArgumentVotes', views.CounterArgumentVoteViewSet)
router.register(r'VotingRights', views.VotingRightViewSet)
router.register(r'UserGroups', views.UserGroupViewSet)
router.register(r'UserGroupContacts', views.UserGroupContactViewSet)
#router.register(r'UserGrhellooupContacts', views.hello, basename= 'test')
#router.register(r'test', views.hello)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api/argsdebate$', views.ListOfArguments),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published)
]