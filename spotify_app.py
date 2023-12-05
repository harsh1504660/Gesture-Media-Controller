"""import subprocess
import pyautogui
pyautogui.sleep(10)

# Replace 'vlc' with the command to open VLC on your system.
vlc_command = r'C:\Program Files\VideoLAN\VLC\vlc.exe'

# Replace 'path_to_your_media_file' with the actual file path you want to play.
media_file = 'D:\music\Intentions(Mr-Jatt1.com).mp3'
choice = int(input('enter the choice 1 , 2 , 3 ,4: pause , play , next , previous'))

# Open VLC and play the specified media file
while choice != 0:
    choice = int(input('enter the choice 1 , 2 , 3 ,4: pause , play , next , previous'))
    if choice==2:
        subprocess.Popen([vlc_command, media_file])
        pyautogui.sleep(10)
    elif choice==1:
        pyautogui.hotkey('ctrl', 'alt', 'space')
        pyautogui.sleep(10)
    elif choice==4:
        pyautogui.hotkey('p')
        pyautogui.sleep(10)
    elif choice==3:
        pyautogui.hotkey('n')
        pyautogui.sleep(10)
"""

import requests
import time
import subprocess
import pyautogui
# Define the VLC web interface URL and port (adjust as needed)
vlc_url = 'http://localhost:8080/requests/status.xml'
vlc_user = ''  # Use the username if you set one in VLC preferences
vlc_password = 'harsh'  # Use the password if you set one in VLC preferences
vlc_command = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
music_file_path = r'C:\Users\Mrunmay\OneDrive\Desktop\Intentions(Mr-Jatt1.com).mp3'
#subprocess.Popen([vlc_command])
#load_command = 'in_play&input=' + music_file_path
#response = requests.get(vlc_url, auth=(vlc_user, vlc_password), params={'command': load_command})
choice=2
#time.sleep(5)
while choice != 0:
    choice = int(input('enter the choice 1 , 2 , 3 ,4,5: pause , play , next , previous,play'))
    if choice==2:
        subprocess.Popen([vlc_command, music_file_path])
        pyautogui.sleep(5)
    elif choice==1:
        pause_command = 'pl_pause'  ##only one command needed
        response = requests.get(vlc_url, auth=(vlc_user, vlc_password), params={'command': pause_command})
    elif choice==4:
        pause_command = 'pl_previous'
        response = requests.get(vlc_url, auth=(vlc_user, vlc_password), params={'command': pause_command})
        pyautogui.sleep(5)
    elif choice==3:
        pause_command = 'pl_next'   
        response = requests.get(vlc_url, auth=(vlc_user, vlc_password), params={'command': pause_command})
        pyautogui.sleep(5)
    elif choice==5:
        pause_command = 'pl_play'
        response = requests.get(vlc_url, auth=(vlc_user, vlc_password), params={'command': pause_command})
        pyautogui.sleep(5)
    elif choice==6:
        volume_up_command = 'volume'  # Adjust the volume increment as needed
        volume_value = 50
        response = requests.get(vlc_url, auth=(vlc_user, vlc_password), params={'command': volume_up_command,'val':f'+{volume_value}'})
        status_url = vlc_url
        response = requests.get(status_url, auth=(vlc_user, vlc_password))

        if response.status_code == 200:
            xml_content = response.content.decode('utf-8')
            volume_value = int(xml_content.split('<volume>')[1].split('</volume>')[0])
            print(volume_value)

        # Check if the volume element is present in the status.xml
            if volume_value == 356:
                print("Volume is at its maximum level.")
        
            else:
                print("Volume is not at its maximum level.")
        else:
            print(f"Failed to fetch VLC status. Status Code: {response.status_code}")

# Send a command to play/pause VLC






if response.status_code == 200:
    print("VLC Play/Pause Command Sent Successfully")
else:
    print("Failed to Send VLC Play/Pause Command")