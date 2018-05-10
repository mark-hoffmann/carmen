import setuptools

with open('carmen/__init__.py') as fid:
    for line in fid:
        if line.startswith('__version__'):
            VERSION = line.strip().split()[-1][1:-1]
            break

setuptools.setup(
    name="carmenproxy",
    version=VERSION,
    url="https://github.com/mark-hoffmann/fastteradata",

    author="Mark Hoffmann",
    author_email="markkhoffmann@gmail.com",

    description="Tool for proxying programmatic HTTP requests.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['beautifulsoup4','bs4','fake-useragent','pytest'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
