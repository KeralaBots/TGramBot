import re
from sys import argv

from setuptools import setup, find_packages

from constructor.build_api import build_api
from constructor.build_types import build_types

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open('tgrambot/version.txt', encoding='utf-8') as f:
    version = re.findall(r'__version__ = \"(.+)\"', f.read())[0]

if len(argv) > 1 and argv[1] in ["sdist", "install", "develop"]:
    build_api()
    build_types()

setup(
    name="TgramBot",
    version=version,
    description="Partially Auto-generated and asynchronous Minimal Telegram BOT API framework in Python for bots",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/KeralaBots",
    download_url="https://github.com/KeralaBots/TgramBot/releases/latest",
    author="Anand",
    author_email="anandpskerala@gmail.com",
    license="LGPLv3",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    keywords="telegram chat messenger bot api library python",
    project_urls={
        "Tracker": "https://github.com/KeralaBots/Tgrambot/issues",
        "Community": "https://t.me/Keralasbots",
        "Source": "https://github.com/Keralabots/Tgrambot",
    },
    python_requires="~=3.8",
    packages=find_packages(exclude=["constructor*", "tests*"]),
    zip_safe=False,
    install_requires=requires
)
