
from launchpadcli import ppa

def test_parse_url():
    url, err = ppa._parse_url('ppa:kimura-o/retune')
    assert url.user == 'kimura-o' and url.archive == 'retune' and url.source is None
    url, err = ppa._parse_url('ppa:kimura-o/retune/tig')
    assert url.user == 'kimura-o' and url.archive == 'retune' and url.source == 'tig'
    url, err = ppa._parse_url('ppa:kimura-o//tig')
    assert url is None
    url, err = ppa._parse_url('kimura-o/retune/tig')
    assert url is None
    url, err = ppa._parse_url('ppm:kimura-o/retune/tig')
    assert url is None
    url, err = ppa._parse_url('ppa:/retune/tig')
    assert url is None
    url, err = ppa._parse_url('ppa:kimura-o/retune/')
    assert url is None

def test_ls():
    sources, err = ppa.ls('ppa:kimura-o/mecab')
    assert len(sources) == 6
    sources, err = ppa.ls('ppa:kimura-o/mecab', status=None)
    assert len(sources) == 12
    sources, err = ppa.ls('ppa:kimura-o/mecab', series='precise')
    assert len(sources) == 2
    sources, err = ppa.ls('ppa:kimura-o/mecab/hoge')
    assert sources is None and err == ppa.Error.noSuchFile
    sources, err = ppa.ls('ppa:kimura-o/macab')
    assert sources is None and err == ppa.Error.noSuchArchive
    sources, err = ppa.ls('ppa:kimura-o/mecab/mecab', series='xenial')
    assert sources is None and err == ppa.Error.noSuchFile

