zappa-examples
==============

Collection of some examples using zappa, to be used for documentation
as helpful working samples / tutorials.

Usage
-----

Download and install cookiecutter (use ``sudo`` if you must to install globally)::

    pip install cookiecutter

Download the project and populate settings via cookiecutter questions. It will
ask two things: your name and s3 bucket (which must be globally unique)::

    cookiecutter gh:narfman0/zappa-examples

Navigate to the new directory named ``zappa-examples`` to view generated examples
with ready-to-go settings. Each subproject should have a README as well that
should be referred to for usage.

Examples
--------

``flask-hello-world`` Simple hello world app for flask to work with zappa!

``flask-template-routes`` Flask app demonstrating jinja template usage and
multiple routes

``flask-image-service`` Flask app using Pillow to modify an image and upload
to s3. Uses ``lambda-packages`` for pillow related binaries.

``django_hello_world`` Simple hello world django app zappaified!

License
-------

Copyright (c) 2016 Jon Robison

See included LICENSE for licensing information
