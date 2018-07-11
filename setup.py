from setuptools import setup

setup(name='linguistic_analysis',
      version='0.0.1',
      description='Tools for extracting meaning from text',
      author='Peter Wright',
      url='https://github.com/peteraw77/linguistic-analysis',
      packages=['linguistic_analysis'],
      zip_safe=True,
      classifiers=[
          'Programming Language :: Python :: 3',
      ],
      install_requires=[
          'spacy',
      ]
     )
