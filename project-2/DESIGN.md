# Online Worksheet
### CS50x Indonesia

> This is our CS50 Final Project. This program was held in collaboration between the Ministry of Education and Culture of the Republic of Indonesia and Harvard University.

### Introduction
> Online Worksheet is a prototype of an online website that can be used to learn 10th grade mathematics, 11th grade mathematics and guidance and counseling materials. This website is created by combining Flask, Python, HTML, CSS, SQL and several other online tools to complete.

## Installation Instruction
### Setup
#### 1. Clonning Repo
    git clone https://github.com/nrwahyuaji/Proyek-CS50.git
    cd Proyek-CS50
    cd project-2
#### 2. Prerequisites
Make sure to run this program, your computer or server must have Python installed.
After that, make sure that you have installed Flask. If you don't have it installed, you can install it using the example below.

    pip install flask
or if you are using pip3 you can execute this

    pip3 install flask
The next step is to install the package from cs50 (because we are still using the package from cs50, check `App.py`)
To install packages from cs50, please do this.

    pip install cs50
   or
   

    pip3 install cs50

#### 3. Run Flask
To run this program, you can use VSCode for testing or try it directly on your server.
##### Virtual Studio Code
1.Open VSCode <br>
2.Click File > Open Folder <br>
3.Navigate to Folder Project-CS50/project-2 <br>
![enter image description here](https://github.com/nrwahyuaji/Proyek-CS50/raw/master/project-2/static/img/project-2-folder.png)
<br>
4.Clik Terminal > New Terminal
![enter image description here](https://github.com/nrwahyuaji/Proyek-CS50/raw/master/project-2/static/img/new-terminal.png)
<br>
5.Make sure the active terminal location is on

    %YOURFOLDERLOCATION%\Proyek CS50\project-2
 
or as in the image below.
![enter image description here](https://github.com/nrwahyuaji/Proyek-CS50/raw/master/project-2/static/img/terminal-location.png)
<br>
6.Then run the command below

    flask run

7.If the program runs smoothly without errors, it will appear like this.

    Running on http://127.0.0.1:5000
    INFO: Press CTRL+C to quit

8.Done!
<br>
##### Deploy to Server
You can use your own server by installing Python and Flask first. You can also use free service providers such as [PythonAnywhere](https://www.pythonanywhere.com/).
