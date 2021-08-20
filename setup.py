import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chkpath",
    version="0.0.1",
    author="Toby Slight",
    author_email="tslight@pm.me",
    description="Check and optionally create paths.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tslight/chkpath",
    install_requires=['yorn'],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'chkpath = chkpath.__main__:main',
        ],
    }
)
