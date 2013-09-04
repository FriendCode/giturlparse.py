# Imnports
import unittest
from . import parse
from . import rewrite

# Main
def main():
    # Suite of suites ...
    suite = unittest.TestSuite([
        parse.suite,
        rewrite.suite,
    ])

    # Runner
    unittest.TextTestRunner(verbosity=2).run(suite)

    unittest.main()

# If entrypoint
main()