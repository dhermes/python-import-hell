import sys


IDS_FOUND = {}
VALUES_FOR_IDS_FOUND = {}


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
        value = found[key]
        curr_id = id(value)
        if curr_id not in IDS_FOUND:
            IDS_FOUND[curr_id] = id_renumber
            VALUES_FOR_IDS_FOUND[curr_id] = (key, value)
            id_renumber += 1
        else:
            stored_key, stored_val = VALUES_FOR_IDS_FOUND[curr_id]
            if value != stored_val:
                raise ValueError('Module repeated.')

        id_val = IDS_FOUND[curr_id]
        message = '    keyname: %25s, module is: %d' % (key, id_val)
        print(message)


print('---- Before imports')
report_imports()
print('---------------------------------')

import foo
print('---- After foo import')
report_imports()
print('---------------------------------')

from foo._generated.google import baz
print('---- After foo._generated.google.baz import')
report_imports()
print('---------------------------------')

from foo._generated.google import bing
print('---- After foo._generated.google.bing import')
report_imports()
print('---------------------------------')
