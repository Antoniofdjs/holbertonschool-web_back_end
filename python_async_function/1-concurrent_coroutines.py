#!/usr/bin/env python3
"""
    Import wait_random from the previous python file that you’ve written and
    write an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.
"""
from basic_async_syntax import wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
        Returns list of delays in floats ascending order
    '''
    results = []
    tasks = [asyncio.ensure_future(wait_random(max_delay)) for _ in range(n)]
    while tasks:
        done, tasks = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_COMPLETED
            )
        for task in done:
            results.append(await task)
    return results
