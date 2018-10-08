
from collections import namedtuple
from enum import Enum
import re
from . import auth
from lazr.restfulclient import errors as resterrors

URL = namedtuple('URL', ['user', 'archive', 'source'])

Source = namedtuple('Source', ['name', 'version', 'status', 'distro_series', 'date_published'])

class Error(Enum):
    noSuchFile = 1
    noSuchArchive = 2
    noSuchSeries = 3
    badUrl = 4
    unknown = 5

def _parse_url(url):
    m = re.match(r'ppa:([^/]+)/([^/]+)(?:/(.+))?$', url)
    if m is None:
        return (None, Error.badUrl)
    user, archive, source = m.groups()
    return (URL(user, archive, source), None)

def ls(url, status='Published', series=None):
    url, err = _parse_url(url)
    if url is None:
        return (None, err)
    lp = auth.login_anon()
    owner = lp.people(url.user)
    try:
        kwargs = dict(exact_match=True)
        if status is not None:
            kwargs['status'] = status
        if url.source is not None:
            kwargs['source_name'] = url.source
        if series is not None:
            try:
                kwargs['distro_series'] = lp.distributions['ubuntu'].getSeries(name_or_version=series).self_link
            except resterrors.NotFound:
                return (None, Error.noSuchSeries)
            except:
                return (None, Error.unknown)
        sources = owner.getPPAByName(name=url.archive).getPublishedSources(**kwargs)
    except resterrors.NotFound:
        return (None, Error.noSuchArchive)
    except:
        return (None, Error.unknown)
    result = [ Source(name=src.source_package_name,
                      version=src.source_package_version,
                      status=src.status,
                      distro_series=lp.load(src.distro_series_link).name,
                      date_published=src.date_published)
               for src in sources ]
    if url.source is not None and len(result) == 0:
        return (None, Error.noSuchFile)
    return (result, None)

