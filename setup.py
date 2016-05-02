from setuptools import setup, find_packages


setup(name='helloworld',
      version='0.0.1',
      description="An intro to travis CI",
      url="https://github.com/nitlev/pyzmq-helloworld",
      author='Veltin DUPONT',
      author_email='veltind@gmail.com',
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Software Development :: CI Tools',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 3.5',
      ],
      keywords='datascience continuous integration travis',
      packages=find_packages(),
      package_data={
          'model': ['model'],
      },
      )