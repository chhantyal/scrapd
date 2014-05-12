===============================
zalando
===============================

.. image:: https://badge.fury.io/py/zalando.png
    :target: http://badge.fury.io/py/zalando
    
.. image:: https://travis-ci.org/chhantyal/zalando.png?branch=master
        :target: https://travis-ci.org/chhantyal/zalando

.. image:: https://pypip.in/d/zalando/badge.png
        :target: https://pypi.python.org/pypi/zalando


Python web scrapping utils.

``zalando`` is small util as well as Flask application to scrap contents from www.zalando.de.

Usage
-----
It scraps products information from given path.
Example:
  >>> import zalando
  >>> URL_PATH = "damenbekleidung-jeans-straight-leg"
  >>> category = zalando.get_category(URL_PATH)
  >>> # Returns categories as Python dict
  >>> print category["name"]  # prints "Straight Leg"
  >>> print category["url"]
  >>> # prints "http://www.zalando.de/damenbekleidung-jeans-straight-leg/"
  >>> print len(category["articles"])
  >>> # etc.

The Flask app exposes same functionality to the web interface.

Install
--------

    $ git clone https://github.com/chhantyal/zalando or get gzipped package

    Install package using setuptools. It will also install a command line application, which can be
    used to run flask app::

    $ python setup.py install

    $ zalando # runs flask app at port 5000. Use --port to specify different port.
