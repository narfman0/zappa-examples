scheduled-weather
=================

Scheduled function printing the weather

Usage
-----

Create a new virtual environment::

    virtualenv venv

Activate environment::

    source venv/bin/activate

Install requirements::

    pip install -r requirements.txt

To run the program/function locally for testing::

    python app.py

To deploy to AWS::

    zappa deploy prod

View the logs for a view minutes to confirm it is being run every minute::

    zappa tail prod

To update AWS::

    zappa update prod

To bring down all the code::

    zappa undeploy prod

To only schedule/unschedule an already deployed gateway (N/A here, but whatever :))::

    zappa schedule prod
    OR
    zappa unschedule prod
