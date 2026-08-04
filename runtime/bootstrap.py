"""
Flora Bootstrap
"""

from runtime.builder import build_runtime
from runtime.cache import update_cache


def bootstrap():

    build_runtime()

    update_cache()

    print("Flora Runtime Ready")


if __name__ == "__main__":

    bootstrap()
