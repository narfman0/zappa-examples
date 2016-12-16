djangocms-api
=============

Zappa djangocms example. Includes rest framework for easy API usage. Based on
mobile-backend_:

.. _mobile-backend: http://github.com/narfman0/mobile-backend/

Usage
-----

* AWS precursor setup

Ensure CORS is enabled for the s3 bucket (aws / s3 / bucket / properties /
permissions / edit CORS / save)

Ensure postgres (or similar) is set up. A CMS with readonly sqlite db is
near useless (you could update it locally and push it each deploy, but then why
are you using a cms and not a static site generator like jekyll?). Update
``djangocms_api/settings/base DATABASES`` ASAP, using the commented out settings
as a guide.

* Execution

Create a new virtual environment::

    virtualenv venv

Activate environment::

    source venv/bin/activate

Install requirements::

    pip install -r requirements.txt

Create database (see AWS precursor setup above) and populate with a user::

    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py collectstatic

Note: if you are using sqlite just for testing purposes, you will want to run
the server locally and populate the db with content. This will entail logging
in, creating a home page (at least), and possibly other content. Run the server
locally with::

    ./manage.py runserver

To deploy to AWS::

    zappa deploy prod

Now you may navigate to your site! It may be blank, so add ``/admin/`` to the
url and log in to make initial page. Also not an API is included, so navigate
to ``/api/`` to see what is available. Note: internationalization makes it a
little obnoxious to get to these urls - remove the language prefix e.g. ``en``
and things should work.

To update a deploy::

    zappa update prod

To bring down all the code::

    zappa undeploy prod

Known issues
------------

When uploading an image, PIL throws an exception, possibly related to
lambda-packages. See status here_

.. _here: https://github.com/narfman0/cookiecutter-mobile-backend/issues/1

License
-------

Copyright (c) 2016 {{ cookiecutter.author_name }}

See included LICENSE for licensing information
