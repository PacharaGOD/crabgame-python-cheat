import pymem
import re

pm = pymem.Pymem('Crab Game.exe')
client = pymem.process.module_from_name(pm.process_handle,
                                        'GameAssembly.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
address = client.lpBaseOfDll + re.search(rb'\xC6\x43\x24\x00\x48\x8B\xCB',
                                         clientModule).start() + 3

pm.write_uchar(address, 1)
pm.close_process()