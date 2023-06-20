import os
import setuptools


def get_readme():

    with open("README.md", "r") as f:
        content = f.read()
    f.close()
    return content


def get_version_info():

    version_path = os.path.join("plemmy", "version.py")
    file_vars = {}
    with open(version_path, "r") as f:
        exec(f.read(), file_vars)
    f.close()
    return file_vars['__version__']


VERSION = get_version_info()


setuptools.setup(
    name="plemmy",
    version=VERSION,
    description="Python API for LemmyHttp",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/tjkessler/plemmy",
    author="Travis Kessler",
    author_email="travis.j.kessler@gmail.com",
    license="Apache License 2.0",
    packages=["plemmy"],
    install_requires=["requests==2.31.0"],
    zip_safe=False
)
