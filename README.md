# DDXoft Python Template

A safer, low-level Python template to control mouse movement and clicks using the DDXoft driver (`dd40605x64.dll`).  
This avoids common software-based input detection methods by sending relative mouse input at a lower level.

## Features

- Simple Python base to DDXoft functions  
- Supports relative mouse movement and mouse button presses  
- This is a template; build your own logic 
- Minimal dependencies  

## Requirements

- `dd40605x64.dll` in the same directory as your script  
- Python 3.x  
- Optional: `pywin32` for keybind detection (`pip install pywin32`)
- Administrator Privileges

## Usage

1. Place `dd40605x64.dll` alongside your Python script.  
2. Import and initialize the DLL using the provided template.  
3. Use `DD_movR(x, y)` for relative mouse movement and `DD_btn(code)` to simulate mouse button presses.

Example:
```python
# Move mouse 10 pixels right and 5 pixels down
mouse_dll.DD_movR(10, 5)

# Left mouse click
mouse_dll.DD_btn(1)  # Left button down
mouse_dll.DD_btn(2)  # Left button up
