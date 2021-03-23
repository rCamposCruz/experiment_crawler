def i_should_collect(str):
    pass


def i_should_skip(some_address=''):
    return some_address.endswith('.jsp') or \
           some_address.startswith('http://google') or \
           some_address.startswith('https://google') or \
           some_address.startswith('https://twitter.com/') or \
           some_address.startswith('http://twitter.com/') or \
           some_address.startswith('https://www.instagram.com/') or \
           some_address.startswith('http: // www.instagram.com /') or \
           some_address.startswith('https://web.facebook.com/') or \
           some_address.startswith('http://web.facebook.com/') or \
           some_address.startswith('https://www.youtube.com/') or \
           some_address.startswith('http://www.youtube.com/')
