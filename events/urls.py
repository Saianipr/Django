from django.conf.urls import url,include

from django.views.generic import ListView, DetailView

from events.models import events

urlpatterns=[url(r'^$',ListView.as_view(
                                    queryset=events.objects.all(),
                                    template_name="events.html")),

			
            ]