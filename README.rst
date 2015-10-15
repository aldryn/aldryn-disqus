=============
aldryn-disqus
=============

Integrate `Disqus <http://disqus.com>`_ into your
`django CMS <http://django-cms.org>`_ and `Aldryn projects <http://aldryn.com>`_,
and allow users to comment on and discuss content on your site.

Disqus is one of the most popular commenting systems available. It’s especially
suited to news and weblog content, but can be applied anywhere that you’d like
to provide discussion functionality.

With the Aldryn Disqus Addon you can integrate it into your projects and start
building an online community in just a few simple steps.

`See it in action on the django CMS weblog <http://www.django-cms.org/en/blog/>`_.

Installation
============

Aldryn Installation
-------------------

Choose a site you want to install the add-on to from the dashboard. Then go to
``Apps -> Install app`` and click ``Install`` next to ``Aldryn Disqus`` app.

Ensure you correctly set the ``DISQUS_SHORTNAME`` setting in the control panel
to the identifier you configured for your project at Disqus.

Redeploy the site.


Manual Installation
-------------------

Add 'aldryn_disqus' to your project's settings and run ``python manage.py migrate``.

Add ``DISQUS_SHORTNAME = 'projectname'`` to your settings. Where ``projectname``
is the identifier you configured for your project at Disqus.


Usage
-----

After configuring your Disqus account at https://disqus.com/, simply add the
``Aldryn Disqus`` plugin on the desired page(s) in your project.