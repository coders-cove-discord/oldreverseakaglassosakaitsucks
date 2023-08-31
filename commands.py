import pickle
import time
import platform
import gpm

plat = platform.platform()
hostcpu = platform.processor()
hostarchitecture = platform.architecture()
hostmachinearchitecture = platform.machine()

def write():
    text = input(" admin/textedit > ")
    print("Saved file as text.txt")
    pickle.dump(text, open("text.txt","wb"))

def opentext():
    text = input(" admin/texteditor.gos > ")
    try:
        print(" opening file..")
        fromfile = pickle.load(open("text.txt", "rb"))
        time.sleep(1)
        print(fromfile)
    except FileNotFoundError:
        print("file doesnt exist")

def clock():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Current time is " + current_time)

def help():
    print("""All system commands:
    write : makes a new .txt file (dont edit the file outside the os or the text editor will go boom boom)
    opentext : open text.txt
    clock : shows current time
    shutdown : closes this commandline
    sysinfo : shows system info -_-
    """)
    
def sysinfo():
    print("""  
   _____ _                  ____   _____ 
  / ____| |                / __ \ / ____|
 | |  __| | __ _ ___ ___  | |  | | (___  
 | | |_ | |/ _` / __/ __| | |  | |\___ \ 
 | |__| | | (_| \__ \__ \ | |__| |____) |
  \_____|_|\__,_|___/___/  \____/|_____/ 
        System info
                                          """)
    time.sleep(1)
    print("GlassOS version : v0.3")
    print("Host OS : ",plat)
    print("Host CPU : ",hostcpu)
    print("Host OS` Architecture : ",hostarchitecture)
    print("Host Machine`s Architecture : ",hostmachinearchitecture)
    
def admingpm():
    gpm.install()
    
def changes():
        print("--GlassOS Changelog--")
        print(""" Added gpm package manager 
 Added system info
 Added clock 
 Added load system that reloads some externals (built in remote tool)
              """)
        print("--GlassOS Bugfixes--")
        print(" Fixed texteditor crashing the host")
        print("Fixed issue where the os would crash after running help")

def shutdown():
    print("Shutting down...")
    quit()
    
def useless():
    print("AHAHA FUCK YOU HERES A FUCKING ERROR CODE 420 (kernel commited wallshart)")
    while True:
        input("YOU CANT ECAPE THE HARRY POTTER CHARACTERS FUCKING EACHOTHER")