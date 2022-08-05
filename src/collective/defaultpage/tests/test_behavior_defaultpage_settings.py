# -*- coding: utf-8 -*-
from collective.defaultpage.behaviors.defaultpage_settings import IDefaultpageSettingsMarker
from collective.defaultpage.testing import COLLECTIVE_DEFAULTPAGE_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class DefaultpageSettingsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_DEFAULTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_defaultpage_settings(self):
        behavior = getUtility(IBehavior, 'collective.defaultpage.defaultpage_settings')
        self.assertEqual(
            behavior.marker,
            IDefaultpageSettingsMarker,
        )
