
from distutils.core import setup

setup(
    name="git-cl",
    version="0.1",
    description="Tool for uploading git revisions to reitveld.",
    url="https://github.com/mithro/git-cl",
    scripts=['git-cl', 'upload.py']
)
