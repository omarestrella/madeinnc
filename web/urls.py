from django.conf.urls import patterns, url, include

from rest_framework import routers

from web import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls))
)

urlpatterns += patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
