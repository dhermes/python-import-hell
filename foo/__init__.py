from __future__ import absolute_import
import os
import google
CURR_DIR = os.path.abspath(os.path.dirname(__file__))
LOCAL_GOOGLE = os.path.join(CURR_DIR, '_generated', 'google')
google.__path__.append(LOCAL_GOOGLE)

import sys
alternate_key = __name__ + '._generated.google'
if alternate_key in sys.modules:
    raise ImportError(alternate_key, 'has already been imported')
# Re-use the module
sys.modules[alternate_key] = google
