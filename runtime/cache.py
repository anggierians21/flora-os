"""
Flora Runtime Cache
"""

from pathlib import Path
import hashlib

RUNTIME = Path("runtime/build/runtime.md")
CACHE = Path("runtime/build/runtime.sha256")


def update_cache():

    content = RUNTIME.read_bytes()

    digest = hashlib.sha256(content).hexdigest()

    CACHE.write_text(digest)

    return digest
