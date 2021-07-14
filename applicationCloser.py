import os

def openFile():
    os.startfile()
    
def closeFile():
    try: 
        os.system('TASKKILL /F /IM VALORANT-Win64-Shipping.exe') 
    except Exception as e: print(e)

closeFile()
