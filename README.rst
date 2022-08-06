Introduction
============

A folder view, which selects the first page in a folder which the user can access.
This can be useful if you want different default pages for different users or
groups in a folder. It also supports optional login enforcement per Folder.

Usage
-----

Just activate the extension in Plone add-ons and select the default-page-view
in folders display menu. You can then put multiple pages in the folder and
the first page which can be view, would be present to the user.

If you want to enforce a login before redirecting to the first object, you can enable enforce login in the settings fieldset on the Folder.

Please note: For users with the manager or review role, the folder_summary_view
will be show instead of redirecting.
