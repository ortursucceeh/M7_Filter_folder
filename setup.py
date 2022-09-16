from setuptools import setup, find_namespace_packages

setup(name='sort_folder',
      version='1',
      description='Useful code to clean and sort your folders',
      url='https://github.com/ortursucceeh/M6_Sort_folder.py.git',
      author='Artur Kazaryan',
      author_email='tabasus03052003@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['markdown'],
      entry_points={'console_scripts': [
          'filter_folder=sort_folder.sort_folder:main']}
      )
