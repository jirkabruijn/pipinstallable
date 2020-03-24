from setuptools import setup
exec(open('pipinstallable/version.py').read())

setup(
    name = 'pipinstallable',
    version=__version__,
    description = 'A test package to test pipinstallables',
    url = 'https://github.com/jirkabruijn/pipinstallable.git',
    author = 'Jiri Bruijn',
    author_email = 'jirka.bruijn@gmail.com',
    license = 'unlicensed',
    packages=['pipinstallable'],
    zip_safe=False
)
