# coding: utf-8

from setuptools import setup, find_packages

version = '0.1.0'
readme = open('README.rst').read()

setup(name='extreme_fluidity',
      version=version,
      description='Fluidity for the masses!',
      long_description=readme,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
      ],
      keywords='fluidity state machine python flexibility',
      author='Rodrigo Manhães',
      author_email='rmanhaes@gmail.com',
      url='https://github.com/nsi-iff/extreme_fluidity',
      license='MIT License',
      packages=find_packages()
      )

