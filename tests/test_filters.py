import os
from liquidluck.filters import content_url, static_url
from liquidluck.options import settings
ROOT = os.path.abspath(os.path.dirname(__file__))


def test_content_url():
    ctx = {'writer': {'filepath': 'a/b'}}

    assert content_url(ctx, 'index.html') == '/'

    settings.config['permalink'] = '{{category}}/{{filename}}.html'
    assert content_url(ctx, 10) == '/10.html'
    assert content_url(ctx, 'a') == '/a.html'
    assert content_url(ctx, 'a.html') == '/a.html'
    assert content_url(ctx, 'a/') == '/a.html'
    assert content_url(ctx, 'a', 'b') == '/a/b.html'
    assert content_url(ctx, 'a/index.html') == '/a/'
    assert content_url(ctx, 'a/feed.xml') == '/a/feed.xml'
    assert content_url(ctx, 10) == '/10.html'

    settings.config['permalink'] = '{{category}}/{{filename}}'
    assert content_url(ctx, 'a') == '/a'
    assert content_url(ctx, 'a.html') == '/a'
    assert content_url(ctx, 'a/') == '/a'
    assert content_url(ctx, 'a', 'b') == '/a/b'
    assert content_url(ctx, 'a/index.html') == '/a/'
    assert content_url(ctx, 'a/feed.xml') == '/a/feed'
    assert content_url(ctx, 10) == '/10'

    settings.config['permalink'] = '{{category}}/{{filename}}/'
    assert content_url(ctx, 'a') == '/a/'
    assert content_url(ctx, 'a.html') == '/a/'
    assert content_url(ctx, 'a/') == '/a/'
    assert content_url(ctx, 'a', 'b') == '/a/b/'
    assert content_url(ctx, 'a/index.html') == '/a/'
    assert content_url(ctx, 'a/feed.xml') == '/a/feed/'
    assert content_url(ctx, 10) == '/10/'

    settings.config['permalink'] = '{{category}}/{{filename}}'
    settings.config['relative_url'] = True
    assert content_url(ctx, 'a') == '../a'
    assert content_url(ctx, 'a/b') == '../a/b'
    assert content_url(ctx, '/a/b') == '../a/b'

    settings.config['relative_url'] = False


def test_static_url():
    path = os.path.join(ROOT, 'source')
    ctx = {'writer': {'filepath': 'a/b'}}
    func = static_url(path)
    func(ctx, 'settings.py')
    path = os.path.join(ROOT, 'source', 'post')
    func = static_url(path)
    func(ctx, 'demo-rst-1.rst')
