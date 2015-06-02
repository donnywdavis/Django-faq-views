from django.shortcuts import render
from django.views import generic
from faq.models import Topics
from faq.models import Questions


class IndexView(generic.ListView):
    template_name = 'faq/index.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        """Return list of FAQs"""

        return Topics.objects.all()
