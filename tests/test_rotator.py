import pytest
from carmen import ProxyRotator


pr = ProxyRotator()
pr.get_proxies()

def test_getting_proxies():
    pr = ProxyRotator()
    pr.get_proxies()
    assert len(pr.proxies) > 0

def test_making_request():
    r = pr.make_request('http://cnn.com')

    assert r.status == 200
    assert r.msg == 'OK'
    assert len(r.read()) > 0
