# coding=utf-8
# CP-1252 Western European like French, Spanish, German. windows-1252
# ain't no such thing as "plain text"
# utf-16 byte order mask u+feff u+fffe, little/big endian
# utf-8 use exactly same byte ordering on big/little endians
# utf-8 uses 1 byte for ASCII, 2 for Latin, 3 for Chinese
import sys

s = '深入Python'
print(len(s))
print(s[0])

print('=====formatting strings=====')
print("{1}'s password is {0}".format("too short", "someone"))
si_suffixes = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
# compound field names, access data structures
print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))

for (k, v) in sys.modules.items():
    print(k, ':', v)
print('1MB = 1000{0.modules[__main__].si_suffixes[0]}'.format(sys))

# format specifier, see format specification mini-language in python doc
print('{0:.1f} {1}'.format(698.255, 'GB'))
print('=====common string methods======')
doc_string = '''A simple
multiline docstring can
span several lines.'''
print(doc_string.splitlines())
print(doc_string.lower())
print(doc_string.upper())
print(doc_string.lower().count('s'))
query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&')
print(a_list)
# optional second argument of split(), number of times to split
a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v]
print(a_list_of_lists)
print(dict(a_list_of_lists))
# use urllib.parse.parse_qs() in real life
print(doc_string[3:20])
print('======strings vs bytes======')
# string immutable sequence of Unicode characters
# bytes immutable sequence of numbers between 0-255
by = b'abcd\x65'
print(by)
print(type(by))
print(len(by))
by += b'\xff'
print(by)
print(len(by))
print(by[0])
# by[0] = 102 TypeError immutable
barr = bytearray(by)
print(barr)
barr[0] = 102
print(barr)
by = b'simple'
print(doc_string.lower().count(by.decode('ascii')))

print('=====encode strings into bytes=====')
encodings = ['utf-8', 'gb18030', 'big5']
for encoding in encodings:
    s_enc = s.encode(encoding)
    print('encoding', encoding, s_enc, 'length', len(s_enc))
print(s == s.encode('big5').decode('big5'))
# default encoding python 2 ASCII, python 3 utf-8
