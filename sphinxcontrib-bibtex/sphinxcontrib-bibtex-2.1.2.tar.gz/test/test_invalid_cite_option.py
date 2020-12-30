"""
    test_invalid_cite_option
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Test behaviour when invalid cite option is given.
"""

import pytest
import re


@pytest.mark.sphinx('html', testroot='invalid_cite_option')
def test_invalid_cite_option(app, warning):
    app.build()
    assert re.search(
        'unknown option: "thisisintentionallyinvalid"', warning.getvalue())
