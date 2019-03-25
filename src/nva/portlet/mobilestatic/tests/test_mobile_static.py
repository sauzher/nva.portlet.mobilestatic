# -*- coding: utf-8 -*-
from nva.portlet.mobilestatic.testing import NVA_PORTLET_MOBILESTATIC_FUNCTIONAL_TESTING
from nva.portlet.mobilestatic.testing import NVA_PORTLET_MOBILESTATIC_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility

import unittest


class PortletIntegrationTest(unittest.TestCase):

    layer = NVA_PORTLET_MOBILESTATIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']
        self.request = self.app.REQUEST
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_mobile_static_is_registered(self):
        portlet = getUtility(
            IPortletType,
            name='nva.portlet.mobilestatic.portlets.MobileStatic',
        )
        self.assertEqual(portlet.addview, 'nva.portlet.mobilestatic.portlets.MobileStatic')


class PortletFunctionalTest(unittest.TestCase):

    layer = NVA_PORTLET_MOBILESTATIC_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
