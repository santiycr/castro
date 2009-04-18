from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='castro',
      version=version,
      description="Screencasting library",
      long_description="""\
Castro is a library for recording automated screencasts.

Castro is a minor fork of pyvnc2swf, allowing one to use pyvnc2swf as a 
regular Python library, instead of a Tk GUI application or command line 
utility. 

The specific improvement Castro brings to pyvnc2swf is the ability to start 
and stop recording programmatically via a regular Python API. Castro 
uses a simple file-based IPC to tell pyvnc2swf when to stop recording.

Ordinarily, pyvnc2swf's command line utility, vnc2swf.py, expects users to 
stop recording by manually typing "Control-C", sending a KeyboardInterrupt 
and allowing the process to exit cleanly. On Linux, emulating KeyboardInterrupt
is simple enough to do by sending a SIGINT signal. But this does not work cross-
platform, specifically on Windows. And a big reason for using pyvnc2swf is its
ability to record vnc video on any platform *from* any platform.
""",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: MacOS X',
          'Environment :: Win32 (MS Windows)',
          'Environment :: X11 Applications',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='pyvnc2swf screencast video',
      author='Jason R. Huggins',
      author_email='jason@jrandolph.com',
      url='http://github.com/hugs/castro',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'processing',
          'setuptools',
          'simplejson',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )