#from subprocess import Popen, PIPE
import subprocess
from pathlib import Path
import time

pythonPath = "python"
folders = ["" , r"\bin" , r"\python"]

def execute_microservice(a,b, microName):
    microPath = find(microName);
    if(not microPath): return "could'nt find " + microName
    command = pythonPath + " " + '"' + microPath + '"' + " " + str(a) + " " + str(b)
    return run_command(command)

def find(microName):
    for folder in folders:
        microPath = folder+microName
        if(Path(microPath).is_file()):
            return microPath
    return None    
    
def run_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out,err) = p.communicate()
    if err : return err
    return out
