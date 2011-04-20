import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

requires = [
    "Akhet",
    "pyramid>=1.0a10",
    "pyramid_handlers",
    "WebError",
    "pyramid_jinja2",
    "gearman>=2.0"
]

    

entry_points = """\
    [paste.app_factory]
    main = gearmandashboard:main

    [paste.app_install]
    main = paste.script.appinstall:Installer
"""

setup(name="GearmanDashboard",
      version="0.1",
      description="GearmanDashboard",
      long_description=README + "\n\n" +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="",
      author_email="",
      url="",
      keywords="web pyramid pylons",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="gearmandashboard",
      entry_points=entry_points,
      paster_plugins=["pyramid"],
      )

