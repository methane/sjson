from setuptools import setup
from distutils.core import Extension

sjson_pyx = Extension('sjson.sjson_pyx', sources=['sjson/sjson_pyx.c'])

setup(name='sjson',
      packages=['sjson'],
      ext_modules=[sjson_pyx],
)
