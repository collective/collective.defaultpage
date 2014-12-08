from setuptools import setup, find_packages
import os

version = '0.1'

setup(
    name='collective.defaultpage',
    version=version,
    description="A folder view, which select the first page in a folder"\
    "which the user can access.",
    long_description=
        open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Defaultpage',
    author='Maik Derstappen',
    author_email='md@derico.de',
    url='https://github.com/collective/collective.defaultpage',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api',
        # -*- Extra requirements: -*-
    ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
