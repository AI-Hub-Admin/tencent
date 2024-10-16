from setuptools import setup, find_packages
import pathlib

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'FinanceAgent>=0.0.2',
    'requests>=2.17.0'
]

extras = dict()
extras['dev'] = ['flask>=2.0.0']
extras['test'] = extras['dev'] + []


setup(
    name="tencent",     # Required
    version="1.0.3",    # Required
    description="Contributed APIs Collection of Tencent Product and Service Open AI, such as Wechat Public Account Automatic Reply, etc.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email="dingo0927@126.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="tencent,Wechat,QQ",
    packages=find_packages(where="src"),  # Required
    package_data={'tencent': ['*.txt'], 'tencent.data': ["*.txt"]},
    install_requires=install_requires,    # Required packages
    package_dir={'': 'src'},
    python_requires=">=3.4",
    extras_require=extras,
    project_urls={
        "repository": "https://github.com/AI-Hub-Admin/tencent",
        "homepage": "http://www.deepnlp.org/blog?category=tencent",
    },
)
