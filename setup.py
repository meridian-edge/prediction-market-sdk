from setuptools import setup, find_packages

setup(
    name="meridianedge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests>=2.25"],
    python_requires=">=3.8",
    description="Prediction market consensus data from multiple regulated markets",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://meridianedge.io",
    author="Meridian Edge",
    author_email="support@meridianedge.io",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords="prediction markets consensus probability sports finance api",
    project_urls={
        "Documentation": "https://meridianedge.io/docs.html",
        "Dashboard": "https://meridianedge.io/dashboard.html",
        "Source": "https://github.com/meridian-edge/prediction-market-sdk",
    },
)
