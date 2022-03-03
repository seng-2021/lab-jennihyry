import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    s = s.ljust(1000, 'a')      #padding
    for c in s:
        if c in ['+', '-', 'å', 'ä', 'ö']:
            raise ValueError
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
    crypted = crypted[0:origlen]
    return crypted

def decode(s):
    s = encode(s).lower()
    return s
