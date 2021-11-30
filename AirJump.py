import pymem
import re

pm = pymem.Pymem('Crab Game.exe')
client = pymem.process.module_from_name(pm.process_handle,
                                        'GameAssembly.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
address = client.lpBaseOfDll + re.search(rb'\x80\xBB.....\x74\x09\x80\xBB.....',
                                         clientModule).start()

pm.write_bytes(address, b"\x90\x90\x90\x90\x90\x90\x90\x90\x90", 9)
pm.close_process()