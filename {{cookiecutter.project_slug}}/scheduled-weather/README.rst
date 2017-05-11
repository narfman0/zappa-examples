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

    zappa schedule prod

To bring down all the code::

    zappa unschedule prod
