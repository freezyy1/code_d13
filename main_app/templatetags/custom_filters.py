from django import template


register = template.Library()


@register.filter(name='censored')
def censor(value, arg):
    words = value.split()
    value1 = ''
    for word in words:
        if isinstance(word, str) and isinstance(arg, str):
            if word == arg:
                word = 'unexpected word'
            value1 += word + ' '
        else:
            raise ValueError(f'Нельзя {type(word)}!')
    return value1
