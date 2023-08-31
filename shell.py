import commands
import gpm

def init():
    
    while True:
       
     line = input(" User > ")

     if line == "write":
        commands.write()

     if line == "opentext":
        commands.opentext()

     if line == "clock":
        commands.clock()

     if line == "shutdown":
        commands.shutdown()
        
     if line == "sysinfo":
        commands.sysinfo()
        
     if line == "admin gpm":
        commands.admingpm()
         
     if line == "changes":
        commands.changes()
        
     if line == "help":
        commands.help()
        
     if line == "useless":
        commands.useless()