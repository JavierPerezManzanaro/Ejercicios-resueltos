import asyncio
import time

async def tarea1():
    print("  Tarea Iniciada 1")
    #time.sleep(1)
    await asyncio.sleep(1)
    print("  Tarea Finalizada 1")

async def tarea2():
    print("  Tarea Iniciada 2")
    #time.sleep(1)
    await asyncio.sleep(1)
    print("  Tarea Finalizada 2")

async def main():
    print("Iniciando Main")
    t1 = asyncio.create_task(tarea1())
    t2 = asyncio.create_task(tarea2())
    print('Main continua su ejecución')
    await asyncio.gather(t1, t2)
    print("Finalizando Main")
    
    
asyncio.run(main())