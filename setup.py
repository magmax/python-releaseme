# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from releaseme import APP


def read_description():
    with open('README.rst') as fd:
        return fd.read()


setup(name='releaseme',
      version=APP.version,
      description=APP.description,
      long_description=read_description(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      keywords='version,versions,versioning,release,releasing',
      author='Miguel Ángel García',
      author_email='miguelangel.garcia@gmail.com',
      url='https://github.com/magmax/python-releaseme',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'pluginloader>=0.1.2',
      ],
      )
