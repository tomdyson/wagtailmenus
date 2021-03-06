import os
from setuptools import setup, find_packages
from wagtailmenus import __version__, stable_branch_name

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

base_url = "https://github.com/rkhleics/wagtailmenus/"
dowload_url = '%starball/v%s' % (base_url, __version__)
branch_url = "%stree/stable/%s" % (base_url, stable_branch_name)

# Testing dependencies
testing_extras = [
    'django-webtest>=1.8.0',
    'beautifulsoup4>=4.4.1,<4.5.02',
    'coverage>=3.7.0',
]

documentation_extras = [
    'pyenchant==1.6.6',
    'sphinxcontrib-spelling>=2.3.0',
    'Sphinx>=1.3.1',
    'sphinx-autobuild>=0.5.2',
    'sphinx_rtd_theme>=0.1.8',
]

setup(
    name="wagtailmenus",
    version=__version__,
    author="Andy Babic",
    author_email="ababic@rkh.co.uk",
    description=("An app to help you manage menus in your Wagtail projects "
                 "more consistently."),
    long_description=README,
    packages=find_packages(),
    license="MIT",
    keywords="wagtail cms model utility",
    download_url=dowload_url,
    url=branch_url,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "wagtail>=1.5",
    ],
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras
    },
)
