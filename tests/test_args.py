import pytest
from pyvorbiscomment import create_argparser


@pytest.fixture
def parser():
    return create_argparser()


def test_parser_no_args(parser):
    args = parser.parse_args([])
    assert args.inputfile is None
