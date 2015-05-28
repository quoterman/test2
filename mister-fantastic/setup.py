from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6',
            'South<=1.0.1',
            'psycopg2<=2.5.4',
            'wsgiref<=0.1.2',
           ]

# if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
#      packages.append('django-redis-cache')
#      packages.append('hiredis')

setup(name='misterfantastic',
      version='1.0',
      description='OpenShift App',
      author='Artur',
      author_email='example@example.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

