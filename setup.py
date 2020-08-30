"""Generic Setup script, takes package info from __version__.py file.
"""
import os
import sys

from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

packages = ['jirakosaar', 'jirakosaar.config', 'jirakosaar.issues', 'jirakosaar.issues.auth']

requires = [
    'requests>=2.0'
]

test_requirements = []

about = {}

with open(os.path.join(here, 'src', 'jirakosaar', '__version__.py'), 'r', 'utf-8') as file:
    exec(file.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.md', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'jirakosaar': 'src/jirakosaar'},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requires,
    scripts=about['__scripts__'],
    license=about['__license__'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    project_urls={
        'Source': 'https://github.com/diwap/jirakosaar',
    },
)
