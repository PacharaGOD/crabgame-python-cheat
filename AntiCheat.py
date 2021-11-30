import pymem
import re

pm = pymem.Pymem('Crab Game.exe')
client = pymem.process.module_from_name(pm.process_handle,
                                        'GameAssembly.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
address = client.lpBaseOfDll + re.search(rb'\x40\x53\x48\x83\xEC\x20\x48\x8B\xD9\x48\x85\xC9\x74\x71',
                                         clientModule).start()

pm.write_bytes(address, b"\xC3\x90", 2)
pm.close_process()