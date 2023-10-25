# -*- coding: utf-8 -*-

"""
Python runners usage
"""

# standard
import asyncio


async def async_print_message(message: str, delay: int):
    """
    Muestra un mensaje tras un tiempo de espera
    """
    await asyncio.sleep(delay)
    print(message)


# ----------------------------------------
# Basic +3.7
# ----------------------------------------

asyncio.run(async_print_message(message='¡Saludos!', delay=1))

# ----------------------------------------
# Contextual +3.11
# ----------------------------------------

with asyncio.Runner() as runner:
    runner.run(async_print_message(message='¡Saludos!', delay=1))

    runner_loop = runner.get_loop()
    asyncio_loop = asyncio.get_event_loop()
    loop_are_equals = runner_loop is asyncio_loop

    print(f'Ciclo del Runner = Ciclo de asyncio: {loop_are_equals}')
