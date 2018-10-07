
from launchpadcli import auth

def test_login():
    lp = auth.login_anon()
    assert lp != None

