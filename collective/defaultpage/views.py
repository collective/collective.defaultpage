from Products.CMFCore.interfaces import IContentish, IFolderish
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from Products.Five import BrowserView
from plone import api

from collective.defaultpage import _


class DefaultPageView(BrowserView):
    """ Redirects to the first object which the current user can view.
        Useful to create different default pages for different users and groups.
    """

    def __call__(self):
        mtool = getToolByName(self, 'portal_membership')
        roles_in_context = api.user.get_roles(
            username=mtool.getAuthenticatedMember().getUserName(),
            obj=self.context)
        if ('Reviewer' in roles_in_context) or ('Manager' in roles_in_context):
            # summary_view = getMultiAdapter(
            #     (self.context, self.request), name='folder_summary_view')
            #summary_view = summary_view.__of__(self.context)
            st_msg = IStatusMessage(self.request)
            st_msg.add(
                _(
                    u"You have extended rights in this context, thats why we"\
                    u"don't show the default page here, to make your life"\
                    u"easier."
                ),
                type="info"
            )

            summary_view = self.context.restrictedTraverse('folder_summary_view')
            return summary_view()

        for obj in self.context.objectValues():
            if not IContentish.providedBy(obj):
                continue
            if not mtool.checkPermission('View', obj):
                continue

            return self.request.RESPONSE.redirect(obj.absolute_url())
