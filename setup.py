import os 
import setuptools

def setup_package():
  long_description = "pkg1"
  setuptools.setup(
      name='pkg1',
      version='0.0.1',
      description='pkg1',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='phlk',
      license='MIT License',
      packages=setuptools.find_packages(
          exclude=['docs', 'tests', 'scripts', 'examples']),
      dependency_links=[
          'https://download.pytorch.org/whl/torch_stable.html',
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7.10',
      ],
      keywords='text nlp machinelearning',
      install_requires=[
        'matplotlib==3.4.2',
      ],
  )


if __name__ == '__main__':
  setup_package()
