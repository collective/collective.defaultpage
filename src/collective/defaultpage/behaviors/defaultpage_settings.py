# -*- coding: utf-8 -*-

from collective.defaultpage import _
from plone import schema
from plone.app.z3cform.widget import SingleCheckBoxBoolFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface, implementer, provider


class IDefaultpageSettingsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IDefaultpageSettings(model.Schema):
    """
    """
    model.fieldset(
        'settings',
        label=u'Settings',
        fields=[
            'enforce_login',
        ],
    )
    directives.widget(enforce_login=SingleCheckBoxBoolFieldWidget)
    enforce_login = schema.Bool(
        title=_(
            u'Enforce login',
        ),
        description=_(
            u'Enforce login before redirecting to first object in defaultpage view.',
        ),
        required=False,
        default=False,
        readonly=False,
    )


@implementer(IDefaultpageSettings)
@adapter(IDefaultpageSettingsMarker)
class DefaultpageSettings(object):
    def __init__(self, context):
        self.context = context

    @property
    def enforce_login(self):
        if safe_hasattr(self.context, 'enforce_login'):
            return self.context.enforce_login
        return False

    @enforce_login.setter
    def enforce_login(self, value):
        self.context.enforce_login = value
