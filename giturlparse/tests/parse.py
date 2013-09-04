# Imports
import unittest

from giturlparse import parse

# Test data
VALID_PARSE_URLS = (
    # Valid SSH, HTTPS, GIT
    ('SSH', ('git@github.com:Org/Repo.git', {
        'host': 'github.com',
        'user': 'Org',
        'repo': 'Repo',

        'protocol': 'ssh',
        'github': True,
        'bitbucket': False,
        'assembla': False
    })),
    ('HTTPS', ('https://github.com/Org/Repo.git', {
        'host': 'github.com',
        'user': 'Org',
        'repo': 'Repo',

        'protocol': 'https',
        'github': True,
        'bitbucket': False,
        'assembla': False
    })),
    ('GIT', ('git://github.com/Org/Repo.git', {
        'host': 'github.com',
        'user': 'Org',
        'repo': 'Repo',

        'protocol': 'git',
        'github': True,
        'bitbucket': False,
        'assembla': False
    })),
)

INVALID_PARSE_URLS = (
    ('SSH Bad Username', 'gitx@github.com:Org/Repo.git'),
    ('SSH No Repo', 'git@github.com:Org'),
    ('HTTPS No Repo', 'https://github.com/Org'),
    ('GIT No Repo', 'git://github.com/Org'),
)

# Here's our "unit tests".
class UrlParseTestCase(unittest.TestCase):

    def _test_valid(self, url, results):
        p = parse(url)
        for k,v in results.items():
            attr_v = getattr(p, k)
            try:
                self.assertEqual(attr_v, v, "[%s] Property '%s' should be '%s' but is '%s'" % (url, k, attr_v, v))
            except Exception as e:
                print("\nDICT = %s\n" % dict(p._matches))
                raise e
        self.failUnless(p.valid)

    def testValidUrls(self):
        for test_type, data in VALID_PARSE_URLS:
            self._test_valid(*data)

    def _test_invalid(self, url):
        p = parse(url)
        self.failIf(p.valid)

    def testInvalidUrls(self):
        for problem, url in INVALID_PARSE_URLS:
            self._test_invalid(url)

# Test Suite
suite = unittest.TestLoader().loadTestsFromTestCase(UrlParseTestCase)
