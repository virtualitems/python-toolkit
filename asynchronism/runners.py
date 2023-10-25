# -*- coding: utf-8 -*-

"""
Python runners usage
"""

# standard
from __future__ import annotations
from typing import TYPE_CHECKING

import asyncio

# typing
if TYPE_CHECKING:  # pragma: no cover
    pass


async def async_print_message(message: str, delay: int):
    """
    Async message
    """
    await asyncio.sleep(delay)
    print(message)


# ----------------------------------------
# Basic +3.7
# ----------------------------------------

asyncio.run(async_print_message(message="Greetings!", delay=1))

# ----------------------------------------
# Contextual +3.11
# ----------------------------------------

with asyncio.Runner() as runner:
    runner.run(async_print_message(message="Greetings!", delay=1))

    runner_loop = runner.get_loop()
    asyncio_loop = asyncio.get_event_loop()
    loop_are_equals = runner_loop is asyncio_loop

    print(f'Runner loop is asyncio loop: {loop_are_equals}')
