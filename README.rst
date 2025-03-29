Python Wrapper for Qiita API v2
===============================

fork from qiita_v2(https://github.com/petitviolet/qiita_py)

Version
-------

1.0(2025/04/01)

Setup
-----

`qiita_v2: Python Package Index <https://pypi.python.org/pypi/qiita_v2>`_
::

  pip install qiita_nn

How to Use
----------

Simple usage
~~~~~~~~~~~~

::

  from qiita_v2.client import QiitaClient

  client = QiitaClient(access_token=<access_token>)
  res = client.get_user('petitviolet')
  res.to_json()
  # => jsonified contents


Lisence
-------

`MIT License <http://petitviolet.mit-license.org/>`_
