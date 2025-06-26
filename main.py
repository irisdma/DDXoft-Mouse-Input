import ctypes
import os
import time

# Loads DDXoft
dll_path = os.path.abspath("dd40605x64.dll")
assert os.path.exists(dll_path), f"[ERROR] DDXoft DLL not found at {dll_path}"

mouse_dll = ctypes.WinDLL(dll_path)
time.sleep(1)  # time for the DLL to load

# define function signatures
mouse_dll.DD_btn.argtypes = [ctypes.c_int]
mouse_dll.DD_btn.restype = ctypes.c_int

mouse_dll.DD_movR.argtypes = [ctypes.c_int, ctypes.c_int]
mouse_dll.DD_movR.restype = ctypes.c_int

# initialize DDXoft
init = mouse_dll.DD_btn(0)
if init != 1:
    print("[ERROR] Failed to initialize DDXoft.")
    exit(1)
else:
    print("[OK] DDXoft loaded and ready.")

print("[INFO] YOU MUST INPUT YOUR OWN SIMULATION METHOD")

