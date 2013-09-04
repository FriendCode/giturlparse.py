# Imnports
import unittest
from . import parse

# Main
def main():
    # Suite of suites ...
    suite = unittest.TestSuite([
        parse.suite
    ])

    # Runner
    unittest.TextTestRunner(verbosity=2).run(suite)

    unittest.main()

# If entrypoint
main()