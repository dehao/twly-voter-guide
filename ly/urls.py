from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from api import views


admin.autodiscover()
#--> rest framework url
router = routers.DefaultRouter()
router.register(r'legislator', views.LegislatorViewSet)
router.register(r'legislator_terms', views.LegislatorDetailViewSet)
router.register(r'committees', views.CommitteesViewSet)
router.register(r'legislator_committees', views.Legislator_CommitteesViewSet)
router.register(r'sittings', views.SittingsViewSet)
router.register(r'proposal', views.ProposalViewSet)
router.register(r'legislator_proposal', views.Legislator_ProposalViewSet)
router.register(r'vote', views.VoteViewSet)
router.register(r'legislator_vote', views.Legislator_VoteViewSet)
router.register(r'bill', views.BillViewSet)
router.register(r'legislator_bill', views.Legislator_BillViewSet)
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'platform', views.PlatformViewSet)
#<--
urlpatterns = patterns('',
    url(r'^legislator/', include('legislator.urls', namespace="legislator")),
    url(r'^vote/', include('vote.urls', namespace="vote")),
    url(r'^proposal/', include('proposal.urls', namespace="proposal")),
    url(r'^bill/', include('bill.urls', namespace="bill")),
    url(r'^issue/', include('issue.urls', namespace="issue")),
    url(r'^about/$', 'ly.views.about', name='about'),
    url(r'^reference/$', 'ly.views.reference', name='reference'),
    url(r'', include('legislator.urls', namespace="legislator")),
    url(r'^api/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Examples:
    # url(r'^$', 'ly.views.home', name='home'),
    # url(r'^ly/', include('ly.foo.urls')),

    # Uncomment the next line to enable the admin:
)
