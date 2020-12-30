import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AoE2ScenarioParser",
    version="0.0.16",
    author="Kerwin Sneijders",
    author_email="ksneijders@hotmail.com",
    description="This is a project for editing parts of an 'aoe2scenario' file from Age of Empires 2 Definitive Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KSneijders/AoE2ScenarioParser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
