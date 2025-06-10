import os

commands = [
    'sudo apt update',
    'sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb',
    'sudo apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver',
    'sudo apt install xfce4-terminal -y',
    'sudo apt install firefox-esr -y',
    'sudo apt-get install geany -y',
    'sudo apt-get install vim-gtk3 -y',
    'sudo apt install iputils-ping -y'
]

for cmd in commands:
    exit_code = os.system(cmd)
    if exit_code != 0:
        print (f"Command failed with exit code {exit_code}: {cmd}")
        # You might want to add break or handle the error here

print ("VNC setup complete")
