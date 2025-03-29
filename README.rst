Python Wrapper for Qiita API v2
===============================

fork from qiita_v2(https://github.com/petitviolet/qiita_py)

Version
-------

1.0(2025/04/01)

Setup
-----

`qiita_v2: Python Package Index <https://pypi.python.org/pypi/`_
::

  pip install qiita_nn

How to Use
----------

Simple usage
~~~~~~~~~~~~

::

  from qiita_nn.client2 import QiitaClient2

  client = QiitaClient(access_token=<access_token>)
  res = client.get_user('petitviolet')
  res.to_json()
  # => jsonified contents

Caution
----------

2025/4/1 以下のメソッドに対応しています。

::

  get_item
  get_user
  list_user_items
  list_items
  list_tag_items
  list_user_stocks
  get_authenticated_user_items
  list_users
  get_authenticated_user
  list_user_followees
  list_user_followers
  list_item_stockers

projects、templatesなどには対応しておりません。
今後対応したいと思います。


Lisence
-------

`MIT License <http://petitviolet.mit-license.org/>`_
