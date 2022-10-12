
import io
from os import path
from setuptools import find_packages, setup

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, 'README.md'), encoding='utf-8') as readme:
    desc = readme.read()

setup(
    name='something',
    version=1.0,
    description='loved it',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='vishwanath, raghu',
    license='Apache-2.0 License',
    packages=find_packages(),
    classifiers=[
        'Topic :: Misc',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'something = something.something:main'
        ]
    },
    keywords=['something']
)
