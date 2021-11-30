import pymem
import re

pm = pymem.Pymem('Crab Game.exe')
client = pymem.process.module_from_name(pm.process_handle,
                                        'GameAssembly.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
address = client.lpBaseOfDll + re.search(rb'\x48\x89\x5C\x24.\x48\x89\x74\x24.\x57\x48\x83\xEC.\x80\x3D.....\x48\x8B\xF2\x48\x8B\xD9\x75.\x48\x8D\x0D....\xE8....\x48\x8D\x0D....\xE8....\xC6\x05.....\x48\x8B\x7B',
                                         clientModule).start()

pm.write_bytes(address, b"\xC3\x90\x90\x90\x90", 5)
pm.close_process()