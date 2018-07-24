from setuptools import setup

setup(name='linguistic_analysis',
      version='1.0-alpha2',
      description='Tools for extracting meaning from text',
      author='Peter Wright',
      license='MIT',
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
