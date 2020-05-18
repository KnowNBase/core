from setuptools import setup  # type: ignore

setup(
      name="knb",
      version="0.1",
      url="https://github.com/intey/knb-core",
      license="MIT",
      author="Intey",
      author_email="ziexe0@gmail.com",
      description="Core domain for making knowledge base",
      packages=[
            'knb',
            'knb.errors',
            'knb.use_cases',
            'knb.utils',
      ],
      long_description=open("README.md").read(),
      zip_safe=False,
)
