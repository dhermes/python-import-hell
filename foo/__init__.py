from __future__ import absolute_import
import os
import google
CURR_DIR = os.path.abspath(os.path.dirname(__file__))
LOCAL_GOOGLE = os.path.join(CURR_DIR, 'google')
google.__path__.append(LOCAL_GOOGLE)
