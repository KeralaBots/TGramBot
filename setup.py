import re
from sys import argv

from setuptools import setup, find_packages

from compiler import build_types, build_methods

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open('tgrambot/version.txt', encoding='utf-8') as f:
    version = re.findall(r'__version__ = \"(.+)\"', f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

if len(argv) > 1 and argv[1] in ["sdist", "install", "develop"]:
    build_types()
    build_methods()

setup(
    name="TGramBot",
    version=version,
    description="Partially Auto-generated and asynchronous Minimal Telegram BOT API framework in Python for bots",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/KeralaBots",
    download_url="https://github.com/KeralaBots/TgramBot/releases/latest",
    author="Anand",
    author_email="anandpskerala@gmail.com",
    license="LGPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
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
    python_requires=">=3.8",
    packages=find_packages(exclude=["tests*", "examples*"]),
    zip_safe=False,
    install_requires=requires
)
