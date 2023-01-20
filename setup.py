import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'click>=8.1,<8.2'
]

setuptools.setup(
    name="rootbranch",
    version="1.0.0",
    author="Shayan Karimi",
    author_email="shayankarimi0078@gmail.com",
    description="A command line tools to manage a multi-repo project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shywn-mrk/rootbranch",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points= {
        "console_scripts": [
            "rootbranch = rootbranch.__main__:cli"
        ]
    }
)