
from launchpadcli import ppa

def test_parse_url():
    url = ppa._parse_url('ppa:kimura-o/retune')
    assert url.user == 'kimura-o' and url.archive == 'retune' and url.source is None
    url = ppa._parse_url('ppa:kimura-o/retune/tig')
    assert url.user == 'kimura-o' and url.archive == 'retune' and url.source == 'tig'
    url = ppa._parse_url('ppa:kimura-o//tig')
    assert url is None
    url = ppa._parse_url('kimura-o/retune/tig')
    assert url is None
    url = ppa._parse_url('ppm:kimura-o/retune/tig')
    assert url is None
    url = ppa._parse_url('ppa:/retune/tig')
    assert url is None
    url = ppa._parse_url('ppa:kimura-o/retune/')
    assert url is None

