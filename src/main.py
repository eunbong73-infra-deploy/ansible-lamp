# main.py

from fastapi import FastAPI
import subprocess
import tailer
import threading
import time
from fastapi.responses import PlainTextResponse



global proc
proc = None
startLogBuffer = ""
ans_base_dir="/home/osboxes/ansible-demos-exercises/"
job_base_dir= ans_base_dir + "lamp_handson/"


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello"}

@app.get("/create")
async def create():
    #exec_sh  = '/home/osboxes/ansible-demos-exercises/lamp_handson/create.sh'
    #log_file = open("/home/osboxes/ansible-demos-exercises/lamp_handson/create.log","w")
    exec_sh  = job_base_dir + "create.sh"
    log_file = open( job_base_dir + "create.log","w")
    global proc
    global startLogBuffer
    startLogBuffer = ""
    proc = subprocess.Popen( [exec_sh], shell=True, stdout=log_file)
    t = threading.Thread( target=checkCreate )
    t.start()
    t2 = threading.Thread( target=startLog )
    t2.start()

    return {"message": proc.poll() }

@app.get("/createLog", response_class=PlainTextResponse)
async def createLog( startLine: int=0):

    if startLine <= 0 :
        print ("LOG=="+startLogBuffer)
        return startLogBuffer
    else :
        arrLog = startLogBuffer.split('\n')
        if startLine > len(arrLog) :
            return startLogBuffer

        retLog = '\n'.join (arrLog[startLine:])
        return retLog


@app.get("/status")
async def status():
    global proc
    if proc != None:
        status = proc.poll()
        return {"message": status}

    return {"message": "no start"}


@app.get("/delete")
async def delete():
    exec_sh  = job_base_dir + "delete.sh"
    log_file = open( job_base_dir + "delete.log","w")

    startLogBuffer = ""
    proc = subprocess.Popen( [exec_sh], shell=True)
    return {"message": "delete"}


def checkCreate():

    while True:
        try:
            time.sleep(10)
            if proc.poll() == None:
                print ("Creation is continue")
            else:
                print (f'Creation is finished { proc.poll() } ')
                break

        except:
            print (f'Creation0 is finished { proc.poll() } ')
            break
    log_file = open( job_base_dir + "create.log","a")
    log_file.writelines(["END"])
    log_file.flush()
    log_file.close()

def startLog():
    global startLogBuffer
    llog_file = open( job_base_dir + "create.log")
    for line in tailer.follow(llog_file):
        print (line);
        if line == "END":
            break
        else:
            startLogBuffer = startLogBuffer + line + '\n'

    print ("!!! !!!END!!! startLog")
