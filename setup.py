from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="eopi_solutions",
    version="0.1",
    description="Solutions to Elements of Programming Interviews in Python",
    url="https://github.com/nakulcr7/eopi-solutions",
    author="Nakul Camasamudram",
    author_email="nakul.cr7@gmail.com",
    license="MIT",
    packages=["eopi_solutions"],
    test_suite="nose.collector",
    tests_require=["nose"],
    zip_safe=False,
)
