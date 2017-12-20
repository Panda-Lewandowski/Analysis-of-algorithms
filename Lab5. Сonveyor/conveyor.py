import asyncio
import logging
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(format="[%(thread)-5d]%(asctime)s: %(message)s")
logger = logging.getLogger('async')
logger.setLevel(logging.INFO)

executor = ThreadPoolExecutor(max_workers=13)  # thread pool
loop = asyncio.get_event_loop()  # event loop


def cpu_bound_op(exec_time, *data):   # fake long-running func
    logger.info("Running cpu-bound op on {} for {} seconds".format(data, exec_time))
    time.sleep(exec_time)
    return sum(data)


async def process_pipeline(data):
    # just pass the data along to level_a and return the results
    results = await level_a(data)  # Waiting for the level a
    return results


async def level_a(data):
    level_b_inputs = data, 2 * data, 4 * data
    results = await asyncio.gather(*[level_b(val) for val in level_b_inputs])  # aggregate results from the level b

    result = await loop.run_in_executor(executor, cpu_bound_op, 3, *results)
    return result


async def level_b(data):
    # similar to level a
    level_c_inputs = data, 3 * data, 5 * data
    results = await asyncio.gather(*[level_c(val) for val in level_c_inputs])
    result = await loop.run_in_executor(executor, cpu_bound_op, 2, *results)
    return result


async def level_c(data):
    result = await loop.run_in_executor(executor, cpu_bound_op, 1, data)
    return result


def main():
    start_time = time.time()
    start_clock = time.clock()
    result = loop.run_until_complete(process_pipeline(2))
    logger.info("Completed ({}) in {} seconds and {} cpu-time".format(result, time.time() - start_time, time.clock() - start_clock))


if __name__ == '__main__':
    main()

    start_time = time.time()
    start_clock = time.clock()

    # inpt = 2

    # lvl_a = inpt, inpt * 2, inpt * 4
    #
    # logger.info("Running cpu-bound op on {}".format(lvl_a))
    # lvl_b_0 = lvl_a[0], lvl_a[0] * 3, lvl_a[0] * 5
    # logger.info("Running cpu-bound op on {}".format(lvl_b_0))
    # lvl_b_1 = lvl_a[1], lvl_a[1] * 3, lvl_a[1] * 5
    # logger.info("Running cpu-bound op on {}".format(lvl_b_1))
    # lvl_b_2 = lvl_a[2], lvl_a[2] * 3, lvl_a[2] * 5
    # logger.info("Running cpu-bound op on {}".format(lvl_b_2))
    #
    # lvl_c = lvl_b_0
    #
    # branch_0 = sum(lvl_c)
    #
    # lvl_c = lvl_b_1
    #
    # branch_1 = sum(lvl_c)
    #
    # lvl_c = lvl_b_2
    #
    # branch_2 = sum(lvl_c)
    #
    # time.sleep(3 + 2 * 3 + 1 * 9)
    #
    # result = sum((branch_0, branch_1, branch_2))
    # logger.info("Running cpu-bound op on {}".format(branch_0, branch_1, branch_2))
    #
    # logger.info("Completed ({}) in {} seconds and {} cpu-time".format(result, time.time() - start_time, time.clock() - start_clock))



