from distutils.core import setup


setup(
    name='constants',
    version='0.6.0',
    description='The simple way to deal with environment constants.',
    long_description=open('README.rst').read(),
    author='Eugene Van den Bulke, Andrew Schell',
    author_email='eugene.vandenbulke@gmail.com, andrewschell3@gmail.com',
    url='http://github.com/3kwa/constants',
    py_modules=['constants'],
    license='BSD',
    install_requires=['tox', 'distutils', 'distutils.core', 'pytest', 'functools', 'unittest',
                      'logging', 'warnings', 'configparser'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
        ],
)
