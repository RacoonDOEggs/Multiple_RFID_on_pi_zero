import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adg728",
    version="0.0.1",
    author="Marc-Olivier Beaulieu",
    author_email="beaulieumolivier@gmail.com",
    description="A library to integrate the ADG728 analog switch IC with the Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="TBD",
    packages=setuptools.find_packages(),
    install_requires=[
        'smbus'
        ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        'Topic :: System :: Hardware',
    ],
)