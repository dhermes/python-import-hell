import sys


IDS_FOUND = {}


def report_imports():
    found = {}
    for key, value in sys.modules.items():
        if 'google' in key:
            found[key] = value

    if IDS_FOUND:
        id_renumber = max(IDS_FOUND.values()) + 1
    else:
        id_renumber = 0

    for key in sorted(found.keys()):
        curr_id = id(found[key])
        if curr_id not in IDS_FOUND:
            IDS_FOUND[curr_id] = id_renumber
            id_renumber += 1
        else:
            raise ValueError('Module repeated.')

        id_val = IDS_FOUND[curr_id]
        message = '    keyname: %20s, module is: %d' % (key, id_val)
        print(message)


print('---- Before imports')
report_imports()
print('---------------------------------')
from foo.google import baz
print('---- After foo.google.baz import')
report_imports()
print('---------------------------------')
from foo.google import bing
print('---- After foo.google.bing import')
report_imports()
print('---------------------------------')
