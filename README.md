# Reference Software for Software Production 2023 Course

## Requirements

- Install tkinter
- Install customtkinter

### On MacOS

```brew install python-tk```

```pip3 install customtkinter```

### On Ubuntu

```sudo apt update```

```sudo apt install python3-tk```

```pip3 install customtkinter```

## WSL

If not working with WSL, go to the folder where the `main.py` file is, run `powershell.exe` and then `python main.py` to start the python application from Windows side.

# Other Development Tasks

## Adding a New Page

1. Create file PageNUMBER.py (you can just copy content of any old page)
2. In `App.py`, import the page on top after other pages
3. In `App.py` add the page into the member variable pages