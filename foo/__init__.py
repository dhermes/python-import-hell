from __future__ import absolute_import
import os
import google
# print('google:')
# print(google)
# print('id(google):')
# print(id(google))
# print('google.__path__:')
# print(google.__path__)
CURR_DIR = os.path.abspath(os.path.dirname(__file__))
LOCAL_GOOGLE = os.path.join(CURR_DIR, 'google')
google.__path__.append(LOCAL_GOOGLE)
