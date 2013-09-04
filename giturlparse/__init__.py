# Imports
from giturlparse.parser import parse as _parse
from giturlparse.result import GitUrlParsed


def parse(url):
	return GitUrlParsed(_parse(url))

def validate(url):
    return parse(url).valid
