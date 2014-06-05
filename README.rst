==============  ===============  =========  ============
VERSION         DOWNLOADS        TESTS      COVERAGE
==============  ===============  =========  ============
|pip version|   |pip downloads|  |travis|   |coveralls|
==============  ===============  =========  ============

Goal and Philosophy
===================

**Releaseme** should ease the process of **versioning** a product and **increment** its version when required, despite the version is managed as a file or a repository tag.



Documentation
=============

Installation
------------

Two options: to install it in your system/project::

    pip install releaseme

And you can use it with::

    python -m releaseme -h


Or just `download the lastest zip`_ and use it with::

   python releaseme-X.Y.Z.zip -h


Examples and FAQ
----------------

Let's see an example. We have git project with a file in ``project/__init__.py``:

.. code:: python

    __version__ = '2.3.4'

We want to manage versions with **releaseme**. And just a command is required::

    $ python -m releaseme.__main__ --git --file project/__init__.py

What does this?
~~~~~~~~~~~~~~~

- Sets a git tag to 2.3.4
- Upgrades the version in the file to '2.3.5'

What??
~~~~~~

This can seem a bit confusing at the beginning, but it is easy to explain: The git tag should mark the point where that version was launched, but the file should change to indicate the version we are working on.

This way, **the file will always contain the next version** to be used and the git tag, the point when it was released.

Can I set an explicit version?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Just edit the file with version and put the desired one.

What happens if there are different versions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The higher one will be used.

What if I want to maintain several files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not a problem, because you can use::

    $ python -m releaseme.__main__ --file project/__init__.py setup.py

and it will set the same version for all of them.


Options
-------

**Releaseme** format is::

    [-h] [-v] [--git] [--file [FILE [FILE ...]]] [ACTION]

Where **Action** is any of :code:`get` or :code:`increment`. If none is provided, `increment` will be used:

- `get` shows current version after processing all files.
- `increment` will read the version and increment it in all files.

:code:`--git`
~~~~~~~~~~~~~

If you are using a Git repository, this will use git tags to get/set the version. No more arguments are required.

:code:`--file`
~~~~~~~~~~~~~~

Allows you to select one or several files (space separated) to manage the version.

About the version number
========================

Versions are up to 4 numbers separated by points. In addition, it can contain a hyphon ('-') and an alphanumeric string at the end. So, valid version numbers are:

- 1
- 1.2
- 1.2.3
- 1.2.3.4
- 1-foo1
- 1.2-foo1
- 1.2.3-foo1
- 1.2.3.4-foo1

Version numbers that will not be managed correctly include:

- 1-1
- 1.a.1
- 1.foo1

If more than one number is retrieved, the higher one will be used. So:

- '1' vs '1.2' will use '1.2'
- '1.2.3.4' vs '1.2' will use '1.2.3.4'
- '1.2.1' vs '1.3.0' will use '1.3.0'

Finally, only the minor number will be incremented:

- '1' increments to '2'
- '1.1' increments to '1.2'
- '1.1-foo1' increments to '1.2-foo1'

Using it like a pro
===================

The best way to use it is launching it just after releasing. So, the best way to do it is to add the **releaseme** call to your publishing script.

Why it doesn't support NNNN technology?
=======================================

Because I still didn't require it. Please, feel free to add an issue and/or send a pull-request.


License
=======

Copyright (c) 2014 Miguel Ángel García (`@magmax9`_).

Licensed under `the MIT license`_.


.. |travis| image:: https://travis-ci.org/magmax/python-releaseme.png
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://coveralls.io/repos/magmax/python-releaseme/badge.png
  :target: `Coveralls`_
  :alt: Coveralls results_

.. |pip version| image:: https://pypip.in/v/releaseme/badge.png
    :target: https://pypi.python.org/pypi/releaseme
    :alt: Latest PyPI version

.. |pip downloads| image:: https://pypip.in/d/releaseme/badge.png
    :target: https://pypi.python.org/pypi/releaseme
    :alt: Number of PyPI downloads

.. _Travis: https://travis-ci.org/magmax/python-releaseme
.. _Coveralls: https://coveralls.io/r/magmax/python-releaseme

.. _@magmax9: https://twitter.com/magmax9

.. _the MIT license: http://opensource.org/licenses/MIT
.. _download the lastest zip: https://pypi.python.org/pypi/releaseme
