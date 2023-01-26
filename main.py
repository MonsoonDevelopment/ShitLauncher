import subprocess, os

paths = f"./Monsoon/Monsoon.json"
mcDir = f"{os.path.expanduser( '~' )}/AppData/Roaming/.minecraft"
assetsDir = f"{mcDir}/assets"
monsoonJarfile = "Monsoon/mc/Monsoon.jar"
jvmPath = f"{os.getenv('JAVA_HOME')}\\bin\\java.exe"
ram = "8000" # go fuck yourself if you have less you bitch
arguments = []

# JVM Start command
arguments.append(jvmPath)

# VM args
arguments.append(f"-noverify -Xms512m -Xmx{ram}m -Djava.library.path=\"Monsoon/natives/\" -cp \"Monsoon/libraries/*;{monsoonJarfile}\"") 

# Main class
arguments.append(f"net.minecraft.client.main.WrappedLaunchLauncher")

# MC Args
arguments.append(f"--width 854 --height 400 --username haiku_is_a_cutie --version 1.8.9 --gameDir {mcDir} --assetsDir {assetsDir} --assetIndex 1.8.9 --uuid N/A --accessToken trolololol --userType mojang")

command = ""
for arg in arguments:
    command = command + arg + " "
command = command + ""

print(arguments)
subprocess.call(command)