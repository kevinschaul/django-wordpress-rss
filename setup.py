from distutils.core import setup

setup(
    name='django-wordpress-rss',
    version='0.1.0',
    author='Kevin Schaul',
    author_email='kevin.schaul@gmail.com',
    url='http://www.kevinschaul.com',
    description='A Django template tag for integrating Wordpress articles.',
    long_description='Check out the project on GitHub for the latest information <http://github.com/kevinschaul/django-wordpress-rss>',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'django>=1.3',
        'feedparser==5.1.2',
    ],
    packages=[
        'wordpress_rss',
        'wordpress_rss.templatetags',
    ],
)

