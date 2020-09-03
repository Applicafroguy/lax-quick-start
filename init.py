import os

# AUR package names - variable shortcuts
arch = 'https://aur.archlinux.org/'
google = 'google-chrome'
github = 'github-desktop-bin'
code = 'visual-studio-code-bin'
git = '.git'
caffeine = 'caffeine-ng'
vue = 'vue-cli'
gconf = 'gconf'

# sudo variables
sudo = 'sudo pacman -S '
# getting current file path
path = os.getcwd()
# changing into install folder thats currently created and empty
os.chdir(r'aur')

# function to download AUR packages
def download(download, bash, path):
    print('Fetching ' + download + ' AUR')
    # downloading AUR package
    os.system('git clone ' + bash)
    # changing directory
    os.chdir(path)
    # making package
    os.system('makepkg -si')
    print("Downloading and installing " + download)

# scripts list to loop through 
scripts = [
    sudo + 'base-devel',
    sudo + 'git',
    sudo + 'ruby-sass',
    sudo + 'scrapy',
    sudo + 'neofetch',
]

# looping through above scripts
for script in scripts:
    os.system(script)

# AUR package downloads using 'download' function
download('Google Chrome', arch + google + git, google)
download('GConfig', arch + gconf + git, gconf)
download('Github Desktop', arch + github + git, github)
download('Visual Studio Code', arch + code + git, code)
download('Caffeine', arch + caffeine + git, caffeine)
download('Vue CLI', arch + vue + git, vue)

# changing path to initial directory
os.chdir(path)
# changing path to remove junk files
os.chdir(r'aur')

# list of item paths to delete from packages directory
items = [
    google, 
    github, 
    code, 
    caffeine, 
    vue, 
    gconf
]

# loop to delete items
for item in items:
    print('Deleting ' + item + ' AUR folders')
    os.system('rm -rf ' + item)
    
# finishing script
print("Script is finished, close the terminal if you wish.")
print("If you had any errors please refer to documentation at https://github.com/quelchlax/lax-quick-start")








