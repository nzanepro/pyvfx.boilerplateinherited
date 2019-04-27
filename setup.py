import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvfx.boilerplateinherited",
    version="0.0.2",
    author="Zachary Cole",
    author_email="zcole@nzaneproductions.com",
    description="An example inherited boilerplate Py* app that runs inside of Maya, Nuke, python2, or python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nzanepro/pyvfx.boilerplateinherited",
    packages=setuptools.find_packages(),
    package_data={
        "pyvfx.boilerplateinherited": ["resources/*.ui"],
    },
    install_requires=[
                      'Qt.py',
                      'pyvfx.boilerplate'
                        ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
