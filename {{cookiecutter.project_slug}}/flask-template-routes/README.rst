flask-template-routes
=====================

Flask app demonstrating jinja template usage and multiple routes

Usage
-----

Create a new virtual environment::

    virtualenv venv

Activate environment::

    source venv/bin/activate

Install requirements::

    pip install -r requirements.txt

To run the flask app locally for testing::

    FLASK_APP=app.py flask run

To deploy to AWS::

    zappa deploy prod

To update a deploy::

    zappa update prod

To bring down all the code::

    zappa undeploy prod
