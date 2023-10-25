# -*- coding: utf-8 -*-

"""
Python coroutines and tasks usage
"""

# standard
from datetime import datetime
import asyncio


# ----------------------------------------
# Coroutine
# ----------------------------------------

# las funciones asincronas deben pasar por 3 etapas:

# 1. definición -> usando la palabra reservada async
async def async_message():
    """
    Retorna un texto tras un tiempo de espera
    """
    await asyncio.sleep(1)
    return 'Greetings!'

async def coroutines():

    fn_instance = async_message

    # 2. ejecución -> se ejecuta la función y se obtiene un objeto coroutine
    co_instance = async_message()

    print(f'Definición de la función: {fn_instance}')
    print(f'Ejecución de la función: {co_instance}')

    # 3. await -> se ejecuta la coroutine con "await"
    message = await co_instance
    print(f'Mensaje: {message}')


# Iniciar ejecución asincrona
asyncio.run(coroutines())


# ----------------------------------------
# Basic tasks
# ----------------------------------------

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def basic_tasks():
    coro1 = say_after(2, 'Terminando tarea 1')
    task1 = asyncio.create_task(coro1)

    coro2 = say_after(1, 'Terminando tarea 2')
    task2 = asyncio.create_task(coro2)

    # Al igual que las coroutines
    # Las Task se ejecutan con "await"
    await task1
    await task2


# Iniciar ejecución asincrona
asyncio.run(basic_tasks())


# ----------------------------------------
# Tasks group
# ----------------------------------------

async def obtener_hora_actual():
    return datetime.now()


async def tasks_group():
    print('Ejecutando grupo de tareas... ', end='')

    # Contexto con grupo de tareas
    async with asyncio.TaskGroup() as tg:

        # Crear tareas
        task1 = tg.create_task(obtener_hora_actual())
        task2 = tg.create_task(obtener_hora_actual())

    # Al finalizar el contexto de ejecución
    print(f'Resultados: {task1.result()}, {task2.result()}')


# Iniciar ejecución asincrona
asyncio.run(tasks_group())