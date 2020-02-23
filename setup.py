import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# original author - Fredrik Averpil
# original author email - fredrik@averpil.com
# original url - https://github.com/fredrikaverpil/pyvfx-boilerplate
name = "pyvfx.boilerplateinherited"
author = "Zachary Cole"
author_email = "zcole@nzaneproductions.com"
url = "https://github.com/nzanepro/pyvfx.boilerplateinherited"
description = "An example inherited boilerplate Py* app that runs inside of Maya, Nuke, python2, or python3"
package_dir = "source"
cli_modules = [
    "pyvfx_boilerplateinherited=pyvfx.boilerplateinherited.cli:main",
]

setuptools.setup(
    setup_requires=['setuptools_scm'],
    use_scm_version={
        'local_scheme': 'node-and-timestamp',
    },
    name=name,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    packages=setuptools.find_packages(package_dir),
    package_dir={"": package_dir},
    entry_points={
        'console_scripts': cli_modules,
    },
    package_data={
        name: ["resources/*.ui", "resources/*.json"],
    },
    install_requires=[
        'pyvfx.boilerplate'
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
