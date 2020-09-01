import os
import distro

# AUR package names
arch = 'https://aur.archlinux.org/'
google = 'google-chrome'
github = 'github-desktop-bin'
code = 'visual-studio-code-bin'
git = '.git'
caffeine = 'caffeine-ng'
vue = 'vue-cli'
gconf = 'gconf'
nvm = 'nvm'

# sudo variables
sudo = 'sudo pacman -S '

# getting current file path
path = os.getcwd()
# changing into install folder thats currently created and empty
os.chdir(r'packages')

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
	"echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.bashrc",
	'exec $SHELL',
	# list of available versions for Node.JS
	'nvm ls-remote',
	# choose your version (recommend 12.18.3 LTS)
	'nvm install 12.18.3',
	'npm version',
    sudo + 'ruby-sass',
    'sass -v',
    sudo + 'scrapy',
    'scrapy version',
    sudo + 'git',
    sudo + 'neofetch',
    'neofetch'
]

if (user == "Manjaro Linux") or (user == "Arch Linux") or (user == 'EndeavourOS'):
    # AUR package downloads using download function
    download('Google Chrome', arch + google + git, google)
    download('GConfig', arch + gconf + git, gconf)
    download('Github Desktop', arch + github + git, github)
    download('Visual Studio Code', arch + code + git, code)
    download('Caffeine', arch + caffeine + git, caffeine)
    download('Vue CLI', arch + vue + git, vue)
    download('NVM', arch + nvm + git, nvm)

    for script in scripts:
    os.system(script)

    # changing path to initial directory
    os.chdir(path)

    # changing path to remove junk files
    os.chdir(r'packages')

    # garbage collection
    print("Deleting junk files")

    # list of item paths to delete
    items = [
        google, github, code, caffeine, vue, gconf, nvm
    ]

    # loop to delete items
    for item in items:
        print('Deleting ' + item + ' AUR folders')
        os.system('rm -rf ' + item)

else:
    print("Your operating system does not match")
    print("Your operating system distro is: " + distro.name())
    os.system('exit')







