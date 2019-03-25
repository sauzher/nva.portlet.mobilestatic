# -*- coding: utf-8 -*-
from __future__ import absolute_import
from Acquisition import aq_inner
from nva.portlet.mobilestatic import _
from plone import schema
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlet.static.static import IStaticPortlet
from plone.portlet.static.static import Assignment as staticAssignment
from plone.portlet.static.static import AddForm as staticAddform
from plone.portlet.static.static import EditForm as staticEditForm
from plone.portlet.static.static import Renderer as staticRenderer
from plone.portlet.static.static import USE_AUTOFORM

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form import field
from zope.component import getMultiAdapter
from zope.interface import implementer

import json
import six.moves.urllib.request
import six.moves.urllib.parse
import six.moves.urllib.error
import six.moves.urllib.request
import six.moves.urllib.error
import six.moves.urllib.parse


class IMobileStaticPortlet(IStaticPortlet):
    """ Mobile Static text portlet interface
    """


@implementer(IMobileStaticPortlet)
class Assignment(staticAssignment):
    schema = IMobileStaticPortlet
    header = _(u"title_mobile_static_portlet",
               default=u"Static text portlet for Mobile")


class AddForm(base.AddForm):

    if USE_AUTOFORM:
        schema = IMobileStaticPortlet
    else:
        fields = field.Fields(IMobileStaticPortlet)

    label = _(u"title_add_mobile_static_portlet",
              default=u"Add a mobile static text portlet")
    description = _(
        u"description_static_portlet",
        default=u"A portlet which can display static HTML text."
    )

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    if USE_AUTOFORM:
        schema = IMobileStaticPortlet
    else:
        fields = field.Fields(IMobileStaticPortlet)

    label = _(
        u"title_edit_mobile_static_portlet",
        default=u"Edit static text portlet for Mobile"
    )
    description = _(
        u"description_mobile_static_portlet",
        default=u"A portlet which can display static HTML text for Mobile devices"
    )


class Renderer(staticRenderer):
    schema = IMobileStaticPortlet
    render = ViewPageTemplateFile('mobile_static.pt')
