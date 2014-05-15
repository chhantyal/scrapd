===============================
scrapd
===============================


Python web scrapping utils.

``scrapd`` is small util as well as Flask application to scrap contents from www.zalando.de.

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
    Steps ::

    $ git clone https://github.com/chhantyal/zalando or get gzipped package

    Install package using setuptools. It will also install a command line application, which can be
    used to run flask app::

    $ python setup.py install

    To run the zalando command line app::

    $ zalando # runs flask app at port 5000. Use --port to specify different port.
