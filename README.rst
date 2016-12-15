zappa-examples
==============

Collection of some examples using zappa, to be used for documentation
as helpful working samples / tutorials.

Usage
-----

Download and install cookiecutter (use `sudo` if you must to install globally)::

    pip install cookiecutter

Then download the project and populate settings via cookiecutter questions.
It will ask four things: your name, aws credentials, and s3 bucket (which
must be globally unique)::

    cookiecutter gh:narfman0/zappa-examples

Navigate to the new directory named `zappa-examples` to view generated examples
with ready-to-go settings. Each subproject should have a README as well that
should be referred to for usage.

Examples
--------

```hello-world``` is a starter flask app, responding "Hello world"

License
-------

Copyright (c) 2016 Jon Robison

See included LICENSE for licensing information
