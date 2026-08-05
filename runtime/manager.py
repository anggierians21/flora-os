"""
Flora Runtime Manager

Single entrypoint for all AI Agents.
"""

from runtime.context import get_context


class RuntimeManager:

    @staticmethod
    def load():

        return get_context()
