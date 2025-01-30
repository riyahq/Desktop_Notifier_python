import time
import json
from plyer import notification
import requests
from datetime import datetime
from PIL import Image
from io import BytesIO

def load_tasks(filename="tasks.json"):
    try:
        with open(filename,"r") as file:
            return json.load(file)
    except:
        return []
    
def check_due_tasks(tasks):
    now=datetime.now().strftime("%Y-%m-%d %H:%M")
    for task in tasks:
        if task["deadline"]==now:
            show_notification("Task Due!",task["task"])
        
def show_notification(title,message,icon_path=None):
    notification.notify(
        title=title,
        message=message,
        app_name="Task Notifier",
        timeout=10,
        app_icon=icon_path
    )

def download_icon(url,filename="icon.ico"):
    try:
        response=requests.get(url)
        img=Image.open(BytesIO(response.content))
        img.save(filename,format="ICO")
        return filename
    except:
        return None

if __name__=="__main__":
    icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTYm5_hKP7n0gipJaXS-hDB3Jpf0y9a7xFhw&s"
    icon_path=download_icon(icon_url)

    while True:
        tasks=load_tasks()
        check_due_tasks(tasks)
        time.sleep(60)