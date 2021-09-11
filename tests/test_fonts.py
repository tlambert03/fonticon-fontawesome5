from enum import EnumMeta
from inspect import ismethod
import fonticon_fa5
import pytest


@pytest.mark.parametrize("attr", fonticon_fa5.__all__)
def test_icons(attr):
    fonticon = getattr(fonticon_fa5, attr)
    assert isinstance(fonticon.__font_file__, str)
    assert fonticon.__font_file__.endswith((".ttf", ".otf"))
