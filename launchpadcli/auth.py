
from launchpadlib.launchpad import Launchpad

CONSUMER = 'launchpad-cli'
ROOT     = 'production'
VERSION  = 'devel'

def login_anon():
    lp = Launchpad.login_anonymously(CONSUMER, ROOT, None, version=VERSION)
    return lp

