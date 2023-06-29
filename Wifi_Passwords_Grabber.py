import subprocess

def get_saved_wifi_passwords():
    command= ['netsh','wlan','show','profiles']
    command_output=subprocess.run(command,capture_output=True,text=True).stdout
    profiles=[]
    for line in command_output.splitlines():
        if line.startswith("    All User Profile"):
            profile_name=line.split(":")[1].strip()
            profiles.append(profile_name)
    
    passwords=[]
    for profile in profiles:
        command=['netsh','wlan','show','profile','name="{0}"','key=clear' .format(profiles)]
        command_output=subprocess.run(command,capture_output=True,text=True).stdout
        password=None
        for line in command_output.splitlines():
            if "Key Content" in line:
                password=line.split(":")[1].strip()
                break
        if password:
            passwords.append(password)
            with open("Saved Passwords.txt", 'w') as file:
                file.write(password)
    return passwords


saved_wifi_passwords=get_saved_wifi_passwords()
print(saved_wifi_passwords)






