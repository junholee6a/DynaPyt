import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynapyt",
    version="0.0.1",
    author="Aryaz Eghbali",
    author_email="aryaz.egh@gmail.com",
    description="Dynamic analysis framework for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sola-st/python-dynamic-analysis",
    project_urls={
        "Bug Tracker": "https://github.com/sola-st/python-dynamic-analysis/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src", "test": "test"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)