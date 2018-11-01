# -*- coding: utf-8 -*-
"""Tests for streamstats Watershed class."""

from vcr_unittest import VCRTestCase
from streamstats import Watershed


class WatershedUnitTests(VCRTestCase):
    '''
    Using a test class based on VCRTestCase allows automatic capture of
    web responses into "cassettes" upon the first run of a given test.
    These cassettes will be "played back" on future tests.
    '''

    @staticmethod
    def test_find_watershed():
        """Verify that the JSON response contains expected keys."""
        wshed = Watershed(lat=43.939, lon=-74.524)
        keys = wshed.data.keys()
        assert 'workspaceID' in keys
        assert 'featurecollection' in keys
        assert 'parameters' in keys
        assert 'messages' in keys
        assert '04150305' in str(wshed)
        assert str(wshed.lat) in str(wshed)
        assert str(wshed.lon) in str(wshed)
