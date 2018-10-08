
from collections import namedtuple
import re

URL = namedtuple('URL', ['user', 'archive', 'source'])

def _parse_url(url):
    m = re.match(r'ppa:([^/]+)/([^/]+)(?:/(.+))?$', url)
    if m is None:
        return None
    user, archive, source = m.groups()
    return URL(user, archive, source)

