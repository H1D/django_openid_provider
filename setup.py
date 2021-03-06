# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = "django_openid_provider",
    version = "0.4.2",
    author = "Roman Barczyński",
    description = "An OpenID provider for your django.contrib.auth accounts",
    long_description = open("README.txt", "rb").read().decode("utf-8"),
    license = "Apache",
    url = "http://www.romke.net/django/openid_provider/",
    download_url = "https://github.com/bioinf/django_openid_provider",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
