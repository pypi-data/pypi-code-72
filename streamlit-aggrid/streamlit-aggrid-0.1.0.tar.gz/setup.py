import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-aggrid", # Replace with your own username
    version="0.1.0",
    author="Pablo Fonseca",
    author_email="pablo.fonseca+pip@gmail.com",
    description="Streamlit component implementation of ag-grid",
    long_description="No time for that!",
    long_description_content_type="text/markdown",
    url="https://github.com/PablocFonseca/streamlit-aggrid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
)