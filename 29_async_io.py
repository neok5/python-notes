#
#   ASYNCIO
#
#       When accessing external resources, use SYNCHRONIZED code is not a good idea, because if one operation
#       last too long, the whole program could get BLOCKED, except if we use multiprocessing (PARALLELISM).
#       On the other hand, we can also use as alternative, threading or asyncIO (CONCURRENCY).
#
#       In Python, we have 3 CONCURRENCY TYPES:
#           - Pre-emptive multitasking (threading), the OS decides when to switch tasks, regardless Python, using
#             several threads to share a single processor.
#           - Cooperative multitasking (asyncio), the tasks decide when to give up control of a single thread.
#           - Multiprocessing, the tasks run all simultaneously, using different processors.
#
#       The EVENT LOOP is where asynchronous processes get executed, sharing a single thread,
#       allowing to set free and use resources more efficiently.
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
from asyncio import sleep, get_event_loop, Future, ensure_future, run

print("---------------------- Simple asynchronous example -----------------------")

async def slow(future_):
    await sleep(0.25)
    future_.set_result('\tFuture completed.')

def got(future_):
    print(future_.result())
    loop.stop()

loop = get_event_loop()  # get the current event loop
future = Future()  # promise of a result

ensure_future(slow(future))  # link coroutine into the current event loop
future.add_done_callback(got)  # add callback for Future

try:
    loop.run_forever()
finally:
    loop.close()

async def speller():
    for letter in '\tHello World!':  # asynchronous for loop, using an asynchronous iterator
        await sleep(0.25)
        print(letter, end='')
run(speller())
print()
