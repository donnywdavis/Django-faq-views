=========
FAQ Views
=========

.. image:: https://readthedocs.org/projects/django-faq-views/badge/?version=latest
:target: https://readthedocs.org/projects/django-faq-views/?badge=latest
:alt: Documentation Status

FAQ is a simple Django app to list frequently asked questions. Multiple
topics can be listed with separate questions and answers.


Quick start
-----------

1. Add "faq" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'faq',
    )

2. Include the faq URLconf in your project urls.py like this::

    url(r'^faq/', include('faq.urls')),

3. Run `python manage.py migrate` to create the faq models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an faq topic with questions and answers (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/faq/ to view the topics, questions, and answers.


TODO
----

- Add detail view to separate topics into separate pages
- Add unit tests