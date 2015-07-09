#!/bin/bash
set -ev

python2.6 import_tester.py
python2.7 import_tester.py
python3.3 import_tester.py
python3.4 import_tester.py
