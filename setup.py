import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "SynthSeq",
    version = "0.0.1",
    author = "Ana Bulovic",
    author_email = "bulovic.ana@gmail.com",
    description = ("A bioinformatical utility for generating sythetic"
                            " sequencing reads from genes or genomes."),
    license = "GPL",
    keywords = "bioinformatics sequencing",
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)