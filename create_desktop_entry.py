import os

string = '''[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec={bin}
Name={name}
Icon={icon}'''


print("\nFill followings requests to create .desktop file\n")
name = input('launcher name: ')
bin = input('bin path: ')
icon = input('icon path: ')

string = string.format(bin = bin, name = name, icon = icon)

with open(name + ".desktop", "w", encoding = "utf-8") as f:
    f.write(string)

print("\nFile .desktop created!\n")

exit_status = os.system("desktop-file-validate {name}.desktop".format(name = name))
if not exit_status:
    exit_status = os.system("desktop-file-install --dir=/usr/share/applications ./{name}.desktop".format(name = name))
else:
    print("Error occurred during validation")

if not exit_status:
    exit_status = os.system("update-desktop-database /usr/share/applications")
else:
    print("An error occurred during installation")
    os.system("rm {name}.desktop".format(name = name))
    quit()

if not exit_status:
    print("File .desktop installated!")
else:
    print("An error occurred during desktop-database update")

os.system("rm {name}.desktop".format(name = name))