# Homebrew requires any external commands be named 'brew-<cmd>'; so
# the lack of a .py extension and hyphen in the middle make it somewhat
# hard to test properly.
#
# For this reason I create a symlink in lib/ instead.

from lib.brew_pip import get_package_info

def test_get_package_info():
    tests = [
        ('Django', ('django', '1.3.1')),
        ('django', ('django', '1.3.1')), # lowercase, too
        ('Django==1.2', ('django', '1.2')),
        ('./transmissionrpc-0.9.tar.gz', ('transmissionrpc', '0.9')),
        ('transmissionrpc-0.9.tar.gz', ('transmissionrpc', '0.9')),
        ('./transmissionrpc-0.9.zip', ('transmissionrpc', '0.9')),
        ('~/src/transmissionrpc-0.9.tar.gz', ('transmissionrpc', '0.9')),
        ('http://example.com/transmissionrpc-0.9.tar.gz', ('transmissionrpc', '0.9')),
        ('git+https://github.com/edavis/django-memcached2', ('django-memcached2', 'HEAD')),
    ]

    for s, answer in tests:
        info = get_package_info(s)
        assert info == answer, ("%s != %s" % (info, answer))