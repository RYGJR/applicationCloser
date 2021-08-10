import os

def openFile():
    os.startfile()
    
def closeFile():
    try: 
        os.system('TASKKILL /F /IM INSERTASKNAME') 
    except Exception as e: print(e)

closeFile()
