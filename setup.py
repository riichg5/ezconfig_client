import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ezconfig_client",
    version="0.1",
    author="RiichTT",
    author_email="",
    description="ezconfig client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pythonml/douyin_image",
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.31.0'],
    entry_points={
        'console_scripts': [
            'ezconfig_client=ezconfig_client:main'
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)