# Example of a multi-page application made with TKInter

![image](https://user-images.githubusercontent.com/3810422/210073524-f357885d-22b7-42ef-848b-9e8a2feab2fe.png)
![image](https://user-images.githubusercontent.com/3810422/210073538-bc8c0681-419c-418e-a5c8-72c62b0180e5.png)
![image](https://user-images.githubusercontent.com/3810422/210073551-f2c46e80-39a4-4f78-871d-2d6ec0a72b10.png)


## Tutorial Series

Below you can find links to three-part series tutorial which explains the structure of this template and how to get started with it.

This starter template was originally made for a software development course, so the videos might have some references to that specific course.

[Part 1 (16 min)](https://www.youtube.com/watch?v=d49E8tq4iLs&ab_channel=CodeTeachr)

[Part 2 (17 min)](https://www.youtube.com/watch?v=3iEbriQYS2M&ab_channel=CodeTeachr)

[Part 3 (11 min)](https://www.youtube.com/watch?v=qy_AJj42QXI&ab_channel=CodeTeachr)

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
