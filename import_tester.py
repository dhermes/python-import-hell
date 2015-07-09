import sys
print('---- Before imports')
for key, value in sys.modules.items():
    if 'google' in key:
        message = '    keyname: %20s, module is: %d' % (key, id(value))
        print(message)
print('---------------------------------')
from foo.google import baz
print('---- After foo.google.baz import')
for key, value in sys.modules.items():
    if 'google' in key:
        message = '    keyname: %20s, module is: %d' % (key, id(value))
        print(message)
print('---------------------------------')
from foo.google import bing
print('---- After foo.google.bing import')
for key, value in sys.modules.items():
    if 'google' in key:
        message = '    keyname: %20s, module is: %d' % (key, id(value))
        print(message)
print('---------------------------------')
