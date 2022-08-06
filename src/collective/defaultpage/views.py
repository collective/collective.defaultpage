from Products.CMFCore.interfaces import IContentish, IFolderish
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from Products.Five import BrowserView
from plone import api
from zope.component import getMultiAdapter

from collective.defaultpage import _


class DefaultPageView(BrowserView):
    """ Redirects to the first object which the current user can view.
        Useful to create different default pages for different users and groups.
    """

    def __call__(self):
        enforce_login = getattr(self.context, "enforce_login", False)
        if api.user.is_anonymous() and enforce_login:
            pstate = getMultiAdapter((self.context, self.request), name='plone_portal_state')
            portal_url = pstate.portal_url()
            url = "{0}/login?came_from={1}".format(portal_url, self.context.absolute_url_path())
            return self.request.RESPONSE.redirect(url)

        if api.user.is_anonymous():
            return self.show_first_accessible_object()

        mtool = getToolByName(self, 'portal_membership')
        roles_in_context = api.user.get_roles(
            username=mtool.getAuthenticatedMember().getUserName(),
            obj=self.context)
        if ('Reviewer' not in roles_in_context) and ('Manager' not in roles_in_context):
            return self.show_first_accessible_object()

        st_msg = IStatusMessage(self.request)
        st_msg.add(
            _(
                u"You have extended rights in this context, thats why we" \
                u"don't show the default page here, to make your life" \
                u"easier."
            ),
            type="info"
        )
        summary_view = self.context.restrictedTraverse('folder_summary_view')
        return summary_view()

    def show_first_accessible_object(self):
        mtool = getToolByName(self, 'portal_membership')
        for obj in self.context.objectValues():
            if not IContentish.providedBy(obj):
                continue
            if not mtool.checkPermission('View', obj):
                continue

            return self.request.RESPONSE.redirect(obj.absolute_url())
        # if no page is accessible, we show the folder_summary_view
        summary_view = self.context.restrictedTraverse('folder_summary_view')
        return summary_view()
