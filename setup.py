import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cliner_greg",
    version="0.0.1",
    author="Greg Werner",
    author_email="gregory@amida.com",
    description="My port of CliNER",
    long_description=long_description,
    long_description_content_type="text/text/x-rst",
    url="https://github.com/pypa/sampleproject",
    package_data={'cliner': ['*.txt', 'tools/*']},
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
