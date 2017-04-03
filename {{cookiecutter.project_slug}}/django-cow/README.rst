django_cow
==========

Cow example zappa friendly cms app

Usage
-----

Virtual environment initialization::

    virtualenv venv
    source venv/bin/activate
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
#. Update DATABASES with non-sqlite server :)
