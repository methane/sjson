def serialize(x):
    L = []
    serialize_obj(x, L)
    return ''.join(L)


cdef serialize_obj(x, list L):
    cdef bint comma

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
        comma = 0
        for it in x:
            serialize_obj(it, L)
            L.append(',')
            comma = 1
        if comma:
            L[-1] = ']'
        else:
            L.append(']')
    else:
        raise TypeError('Unsupported type: %s' % type(x))
