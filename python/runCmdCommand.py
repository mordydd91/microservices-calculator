import subprocess,os
from pathlib import Path

pythonPath = "python"
folders = ["","bin" , "python"]
def execute_microservice(a,b, microName):
    microPath = find(microName);
    if(not microPath): return "could'nt find " + microName
    if(a == None): a=""
    if(b == None): b=""
    command = pythonPath + " " + '"' + microPath + '"' + " " + str(a) + " " + str(b)
    return run_command(command)

def find(microName):
    if(".py" not in microName): microName+=".py"
    for folder in folders:
        microPath = folder+"\\"+microName
        if(Path(microPath).is_file()):
            return microPath
    x = os.path.dirname(os.path.abspath(__file__))
    for folder in folders:
        microPath = x+"\\" + folder + ("\\" if folder !="" else "") +microName
        if(Path(microPath).is_file()):
            return microPath
    return None

def run_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out,err) = p.communicate()
    if err : return err
    return out
