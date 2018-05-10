Carmen
------

.. image:: images/carmen_sandiego.jpg
   :height: 100px
   :width: 120 px
   :scale: 50 %
   :alt: alternate text
   :align: right


Carmen is a tool for proxying programmatic HTTP requests. It finds a list of free proxy servers and routes your request traffic randomly, making everyone ask the question "Where in the world [is Carmen SanDiego] are my network requests coming from?"

This can be useful for webcrawlers where sites block bots after only a few requests.

**Disclaimer: Please use responsibily. Writing a large scale scraper can have detrimental effects on a websites performance and can cost a company a lot of money. DO NOT use this maliciously. Remember, with great power comes great responsibility. **

Installation
------------

Carmen can easily be downloaded straight from github via the following:

.. code-block:: python

  pip install carmen


Usage
-----

This package connects to 'https://www.sslproxies.org/' and finds free available proxies to then cycle through, discarding those that do not initially work.

To use Carmen, simply instantiate the ProxyRotator object, get the available proxies and pass your url into the *make_request* method. You are then returned a Response object.

.. code-block:: python

 from carmen import ProxyRotator

  pr = ProxyRotator()
  pr.get_proxies()

  r = pr.make_request('http://url.com')

  r.read()


Requirements
^^^^^^^^^^^^
- `bs4 <>`_
- `fake-useragent <https://github.com/hellysmile/fake-useragent>`_



Compatibility
-------------

carmen currently supports Python 3.6

Licence
-------

`MIT <https://github.com/mark-hoffmann/carmen/blob/master/LICENSE.txt>`_

Authors
-------

`carmen` was written by `Mark Hoffmann <markkhoffmann@gmail.com>`_.
