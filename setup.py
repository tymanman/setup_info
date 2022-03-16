import os

import setuptools



setuptools.setup(
    name="First_setup",
    version="0.1",
    author="lili",
    author_email="skyevilman@gmail.com",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    setup_requires=["pip>=20.2.3"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={"console_scripts": ["start=playground:main"]},
)

