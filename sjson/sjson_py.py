def serialize(x):
    L = []
    serialize_obj(x, L)
    return ''.join(L)


def serialize_obj(x, L):
    if x is None:
        L.append('None')
    elif x is True:
        L.append('True')
    elif x is False:
        L.append('False')
    elif isinstance(x, (int, float)):
        L.append(str(x))
    elif isinstance(x, list):
        L.append('[')
        comma = False
        for it in x:
            serialize_obj(it, L)
            L.append(',')
            comma = True
        if comma:
            L[-1] = ']'
        else:
            L.append(']')
    else:
        raise TypeError('Unsupported type: %s' % type(x))

