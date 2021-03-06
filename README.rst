===========
Django Blog
===========

A multi-author blog for Django.

Installation from Source
========================

::

 $ git clone git://github.com/jbergantine/django-blog.git
 $ cd django-blog
 $ python setup.py install


Installation via PIP Requirements File
======================================

Include in the PIP requirements file the following lines:

::

 -e git://github.com/jbergantine/django-blog.git#egg=django_blog

And then install as normal (IE:)

::

 $ pip install -r path/to/requirements/file.txt


Setup the Project For the Application
=====================================

Add to the project's settings file tuple of INSTALLED_APPS: 

::

 'django_blog',

In the project's urls.py file add: 

::

 url(r'^blog/author/', include('django_blog.urls.authors')),
 url(r'^blog/category/', include('django_blog.urls.categories')),
 url(r'^blog/feeds/', include('django_blog.urls.feeds')),
 url(r'^blog/', include('django_blog.urls.entries')),

Specify the AUTH_PROFILE_MODULE in the project's settings file: 

::

 AUTH_PROFILE_MODULE = 'django_blog.Author'

If you're using South, initiate the migration and then migrate the database.

::

 $ ./manage.py schemamigration --init django_blog
 $ ./manage.py migrate django_blog

If you're not using South, sync the database.

::

 $ ./manage.py syncdb

A list of the latest 15 posts can now be linked to: 

::

 <a href="{% url 'blog_entry_archive' %}">Blog</a>

A list of all posts in a specific year can be linked to, passing in the year: 

::

 <a href="{% url 'blog_entry_archive_year' 2012 %}">2012</a>

A list of all posts in a specific month can be linked to, passing in year and month: 

::

 <a href="{% url 'blog_entry_archive_month' 2012 01 %}">Jan, 2012</a>

A list of all posts on a specific day can be linked to, passing in year, month and day: 

::

 <a href="{% url blog_entry_archive_day 2012 01 01 %}">Jan 01, 2012</a>

A specific blog post can be linked to, passing in year, month, day and slug: 

::

 <a href="{% url 'blog_entry_detail' 2012 01 01 'first-post' %}">First Post</a>
    
A list of all categories can be linked to: 

::

 <a href="{% url 'blog_category_list' %}">Categories</a>

A list of all posts in a specific category can be linked to, passing in the slug of the category: 

::

 <a href="{% url 'blog_category_detail' 'spying' %}">Posts about Spying</a>

A list of all the posts by a specific author can be linked to, passing in the id of the author: 

::

 <a href="{% url 'blog_author_detail' 2 %}">Posts by James Bond</a>

The RSS feed can now be referred to in the ``<head>`` of your HTML templates: 

::
    
 <link rel="feed alternate" type="application/rss+xml" title="Blog" href="{% url 'blog_feed' %}" />

Configure the Templates
=======================

By default the templates contain only the bare necessities. To override the default templates, create a directory called django_blog in your templates directory and copy the templates from the project into that directory in order to make adjustments to them. If you're using Virtualenv, ``cd`` to the root of the django project and execute the following command:

::

 cp -r $VIRTUAL_ENV/src/django-blog/django_blog/templates/django_blog templates/django_blog

Template Tags
=============

{% authors_list %}
******************

Returns an unordered list of all authors via the template ``_authors_list.html``.

Usage:

::

 {% load authors_list %}
 {% authors_list %}

{% categories_list %}
*********************

Returns an unordered list of all categories via the template ``_categories_list.html``.

Usage:

::

 {% load categories_list %}
 {% categories_list %}

Draft Entries
=============

Draft entries can be previwed directly by clicking the View on Site link from within the Entries Admin. These entries will not be added to any of the list views nor will they be published in the XML (RSS) feed until their status is changed to Live.

Hidden Entries
==============

In addition to not being listed in any of the list views or the XML (RSS) feed, Hidden entries will return a 404 Page Not Found if the URL for the detail view is accessed directly. This can be used to remove an Entry without completely deleting it. It can still be accessed from within the site Admin.

Live Entry Manager
==================

The live entry manager can be used to return all entries with a live status. Example usage would be in ``sitemaps.py``:

::

 from django.contrib.sitemaps import Sitemap
 from django_blog.models import Entry
 
 class BlogSitemap(Sitemap):
   def items(self):
     Entry.live.all()

   def lastmod(self, obj):
     return obj.pub_date
