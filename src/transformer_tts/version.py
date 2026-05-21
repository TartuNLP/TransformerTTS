from importlib.metadata import version
from setuptools.dist import Version
import logging
import subprocess


logger = logging.getLogger(__name__)


def generate_version():
    version_number = "0"
    suffix = ""
    try:
        git_hash = (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
            .strip()
            .decode()
        )
        suffix = f"-dev+{git_hash}"

        tag = (
            subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
            .strip()
            .decode()
            .lstrip("v")
        )
        version_number = str(Version(tag))

        full_tag = (
            subprocess.check_output(["git", "describe", "--tags"])
            .strip()
            .decode()
            .lstrip("v")
        )
        if full_tag == tag:
            suffix = ""
    finally:
        return version_number + suffix


__version__ = generate_version()


def get_version():
    try:
        version_ = version("transformer_tts")
    except Exception:
        logger.warning(
            "Could not get version from package metadata. Reversing to git info."
        )
        version_ = __version__
    return version_
