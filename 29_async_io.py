#
#   ASYNCIO
#
#       When accessing EXTERNAL RESOURCES, use SYNCHRONIZED code is not a good idea, because if one operation
#       last too long, the whole program could get BLOCKED, except if we use multiprocessing (PARALLELISM).
#       On the other hand, we can also use as alternative, threading or asyncIO (CONCURRENCY).
#
#       In Python, we have 3 CONCURRENCY TYPES:
#           - Cooperative multitasking (ASYNCIO), the tasks decide when to give up control of a SINGLE THREAD.
#           - Pre-emptive (by preference) multitasking (THREADING), the OS decides when to switch tasks,
#             regardless Python, using SEVERAL THREADS to share a SINGLE PROCESSOR/CORE.
#           - MULTIPROCESSING, the tasks run all simultaneously, using SEVERAL PROCESSORS/CORES.
#
#       The EVENT LOOP is where asynchronous processes get executed, sharing a SINGLE THREAD,
#       allowing to lock and to set free the thread, which uses resources more efficiently.
#
#       ASYNC OPERATIONS have different syntax depending on Python version:
#           - For Python 3.4, we must use generator-based coroutines, yielding from slow() operation.
#                   " @asyncio.coroutine def py34_coro(): yield from slow() "
#           - For Python +3.5, we could use native coroutines, just having to await for slow() operation.
#                   " async def py35_coro(): await slow() "
#
#       Besides that, there're also differences between how to MANAGE THE EVENT LOOP:
#           - For Python 3.4-3.6, we must handle the event loop manually, getting or creating it, (and later, stopping
#             and closing it), and creating a future, linking that future with an operation and adding a callback.
#           - For Python +3.7, we can just call run() with the operation desired, and Python will manage the
#             event loop automatically for us, creating or getting it, and then destroying it.
#
#       When using ASYNCIO, we should use also ASYNC third-party LIBRARIES, instead of sync libraries. For example,
#       we have 'AIOFILES' for local files handling, 'AIOCACHE' for caching, or 'ASYNCIO_EXTRAS' for several tasks
#       (decorators for building asynchronous context managers, helpers for non-blocking file IO, decorators and
#       context managers for running a function or parts of a function in a thread pool...). We also have async test
#       specialized libraries, such as 'ASYNCTEST' or 'PYTEST-ASYNCIO'.
#
from asyncio import sleep as asyncsleep, get_event_loop, Future, ensure_future, run, gather
from time import sleep as timesleep, perf_counter_ns as getnstimestamp

print("---------------------- Simple asynchronous example -----------------------")

async def slow(future_):  # coroutine or awaitable
    await asyncsleep(0.1)
    future_.set_result('\n\tFuture completed.')

def got(future_):
    print(future_.result())
    loop.stop()

loop = get_event_loop()  # get the current event loop
future = Future()  # promise of a result

ensure_future(slow(future))  # wrap a coroutine or an awaitable in a future (if the arg is a future, return it directly)
future.add_done_callback(got)  # add callback for Future

try:
    loop.run_forever()
finally:
    loop.close()

async def speller():
    for letter in '\tHI!':
        await asyncsleep(0.25)
        print(letter, end='')
run(speller())
print()

print("\n---------------------- Sync vs. async runtime comparision -----------------------")

EXECUTE_N_TIMES = 5

def sync_half_second_awaiter(i):
    print(f'\t\t[\tFirst part #{i}', end='\t')
    timesleep(0.2)
    print(f'\t\tLast part #{i}\t]')

def sync_counter():
    for _ in range(1, EXECUTE_N_TIMES+1):
        sync_half_second_awaiter(_)

print('\n\tSynchronous counter...')
init_ns = getnstimestamp()
sync_counter()
diff_ns = getnstimestamp() - init_ns
first_mark = diff_ns
print(f'\tThe process last {diff_ns / 1000000000:.7f} seconds.')

async def async_half_second_awaiter(i):
    print(f'\t\t#{i}', end=' ')
    if i == EXECUTE_N_TIMES:
        print()
    await asyncsleep(0.2)
    print(f'\t\t#{i}', end=' ')

async def async_counter():
    invocations = []
    for i in range(1, EXECUTE_N_TIMES+1):
        invocations.append(async_half_second_awaiter(i))
    await gather(*invocations)

print('\n\tAsynchronous counter...')
init_ns = getnstimestamp()
run(async_counter())  # the output could be unordered, but in a deterministic way (not random, always the same order)
diff_ns = getnstimestamp() - init_ns
second_mark = diff_ns
print(f'\n\tThe process last {diff_ns / 1000000000:.7f} seconds.')
print(f'\n\tThe second process is {first_mark/second_mark:.2f} times faster than first one.')
