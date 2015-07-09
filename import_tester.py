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
            if VALUES_FOR_IDS_FOUND.get(curr_id) != (key, value):
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
