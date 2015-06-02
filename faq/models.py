from django.db import models


class Topics(models.Model):
    """
    Create a table for sections to list the
    question and answers under.
    """

    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'


class Questions(models.Model):
    """
    Create a table to contain all of the
    question and answers to be listed.
    """

    topic = models.ForeignKey(Topics)
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'
