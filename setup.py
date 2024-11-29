from setuptools import find_packages, setup


setup(
    name="ShannonScanner",
    version="1.0",
    author="Andy Keefe",
    author_email="andrewrkeefe@gmail.com",
    description="A cryptographic scanner for auditing and compliance.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/andykeefe/ShannonScanner",
    packages=find_packages(),
    package_data={
        'ShannonScanner.utils': ['*.json']
    }
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: Linux"
    ],
    python_requires=">=3.6",
    install_requires=[
        "exrex",
        "pyahocorasick"
    ],
    entry_points= {
        "console_scripts": [
            "shannonscan=ShannonScanner.shannonscan:main",
        ],
    },
)