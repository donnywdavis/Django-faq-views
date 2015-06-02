from django.contrib import admin

from faq.models import Topics
from faq.models import Questions


class QuestionsInline(admin.TabularInline):
    """
    Set up a tabular list of questions and answers
    for the admin interface
    """

    model = Questions
    extra = 2


class TopicsAdmin(admin.ModelAdmin):
    """
    Set up the FAQ Topics in the admin interface
    """

    inlines = [QuestionsInline]


admin.site.register(Topics, TopicsAdmin)
