*********
CHANGELOG
*********

`v1.1.2`_ (2019-01-30)
======================
* Fixes for XSD datatypes
* Change the default value of *default_namespace* argument of XPath2Parser to ``None``

`v1.1.1`_ (2019-01-19)
======================
* Improvements and fixes for XSD datatypes
* Rewritten AbstractDateTime for supporting years with value > 9999
* Added fn:dateTime()

`v1.1.0`_ (2018-12-23)
======================
* Almost full implementation of XPath 2.0
* Extended XPath errors management
* Add XSD datatypes for data/time builtins
* Add constructors for XSD builtins

`v1.0.12`_ (2018-09-01)
=======================
* Fixed the default namespace use for names without prefix.

`v1.0.11`_ (2018-07-25)
=======================
* Added two recursive protected methods to context class
* Minor fixes for context and helpers

`v1.0.10`_ (2018-06-15)
=======================
* Updated TDOP parser and implemented token classes serialization

`v1.0.8`_ (2018-06-13)
======================
* Fixed token classes creation for parsers serialization

`v1.0.7`_ (2018-05-07)
======================
* Added autodoc based manual with Sphinx

`v1.0.6`_ (2018-05-02)
======================
* Added tox testing
* Improved the parser class with raw_advance method

`v1.0.5`_ (2018-03-31)
======================
* Added n.10 XPath 2.0 functions for strings
* Fix README.rst for right rendering in PyPI
* Added ElementPathMissingContextError exception for a correct
handling of static context evaluation

`v1.0.4`_ (2018-03-27)
======================
* Fixed packaging ('packages' argument in setup.py).

`v1.0.3`_ (2018-03-27)
======================
* Fixed the effective boolean value for a list containing an empty string.

`v1.0.2`_ (2018-03-27)
======================
* Add QName parsing like in the ElementPath library (usage regulated by a *strict* flag).

`v1.0.1`_ (2018-03-27)
======================
* Some bug fixes for attributes selection.

`v1.0.0`_ (2018-03-26)
======================
* First stable version.


.. _v1.0.0: https://github.com/brunato/elementpath/commit/b28da83
.. _v1.0.1: https://github.com/brunato/elementpath/compare/v1.0.0...v1.0.1
.. _v1.0.2: https://github.com/brunato/elementpath/compare/v1.0.1...v1.0.2
.. _v1.0.3: https://github.com/brunato/elementpath/compare/v1.0.2...v1.0.3
.. _v1.0.4: https://github.com/brunato/elementpath/compare/v1.0.3...v1.0.4
.. _v1.0.5: https://github.com/brunato/elementpath/compare/v1.0.4...v1.0.5
.. _v1.0.6: https://github.com/brunato/elementpath/compare/v1.0.5...v1.0.6
.. _v1.0.7: https://github.com/brunato/elementpath/compare/v1.0.6...v1.0.7
.. _v1.0.8: https://github.com/brunato/elementpath/compare/v1.0.7...v1.0.8
.. _v1.0.10: https://github.com/brunato/elementpath/compare/v1.0.8...v1.0.10
.. _v1.0.11: https://github.com/brunato/elementpath/compare/v1.0.10...v1.0.11
.. _v1.0.12: https://github.com/brunato/elementpath/compare/v1.0.11...v1.0.12
.. _v1.1.0: https://github.com/brunato/elementpath/compare/v1.0.12...v1.1.0
.. _v1.1.1: https://github.com/brunato/elementpath/compare/v1.1.0...v1.1.1
.. _v1.1.2: https://github.com/brunato/elementpath/compare/v1.1.1...v1.1.2
