#!/usr/bin/python3
# coding: utf-8

def tag(name, *content, cls=None, **attrs):
    
    """Gera uma ou mais tags HTML"""
    
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join( '%s="%s"' % (attr, value)
                                    for attr, value
                                    in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s %s>%s</%s>' %
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s %s />' % (name, attr_str)
