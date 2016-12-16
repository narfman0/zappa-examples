django-hello-world
=================

Simple hello world app for django to work with zappa!

Usage
-----

Create a new virtual environment::

    virtualenv venv

Activate environment::

    source venv/bin/activate

Install requirements::

    pip install -r requirements.txt

Create database and populate with a user::

    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py collectstatic

To deploy to AWS::

    zappa deploy prod

To update a deploy::

    zappa update prod

To bring down all the code::

    zappa undeploy prod

Next steps
----------

#. Generate new secret key in settings :)
#. Change sqlite to postgres or any other database
#. Extract settings to dev and prod settings. Ref: 2 scoops django.
