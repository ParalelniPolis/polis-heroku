from django.conf.urls import include, url
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^currently-playing', 'music.views.currently_playing'),
    url(r'^music/', include('music.urls')),

    url(r'^$', RedirectView.as_view(url='/music/currently-playing'))
]
