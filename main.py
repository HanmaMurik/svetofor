# import time
# import asyncio
# from threading import Thread

# def red():
#     time.sleep(2)
#     return 'red'
#
# def yellow(color_1: str):
#     time.sleep(4)
#     print('yellow')
#
#
# def green():
#     time.sleep(6)
#     return 'green'
#
#
#
# t1 = Thread(target=yellow, args=['green'])
# t1.start()
# print(red())
# print(green())
# print('START!!!')
# Многопоточность


# def red():
#     time.sleep(2)
#     print('red')
#
# def yellow():
#     time.sleep(4)
#     print('yellow')
#
# def green():
#     time.sleep(6)
#     print('green')
#
# red()
# yellow()
# green()
# print('START!!!')
# Синхронность

# async def red():
#     await asyncio.sleep(2)
#     print('red')
#
#     # print('fun1 is ready')
#
# async def yellow():
#     await asyncio.sleep(4)
#     print('yellow')
#
#     # print('fun2 is ready')
#
#
# async def green():
#     await asyncio.sleep(6)
#     print('green')
#
#
# async def main():
#     task1 = asyncio.create_task(red())
#     task2 = asyncio.create_task(yellow())
#     task3 = asyncio.create_task(green())
#
#     await task1
#     await task2
#     await task3
#
# asyncio.run(main())
# print('START!!!')



