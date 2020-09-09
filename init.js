const sh = require('shelljs')
sh.cd('aur')

let arch = 'https://aur.archlinux.org/'
let google = 'google-chrome'
let github = 'github-desktop-bin'
let code = 'visual-studio-code-bin'
let git = '.git'
let caffeine = 'caffeine-ng'
let vue = 'vue-cli'
let gconf = 'gconf'
let sudo = 'sudo pacman -S '

function download(bash) {
  sh.exec('git clone ' + arch + bash + git)
  sh.cd(bash)
  sh.exec('makepkg -si')
}

var scripts = [
  sudo + 'git',
  sudo + 'ruby-sass',
  sudo + 'scrapy',
  sudo + 'python-pip',
  sudo + 'neofetch'
]

var downloads = [
  google, 
  gconf, 
  github, 
  code, 
  caffeine, 
  vue
]


function main() {
  scripts.forEach(item => {
    try {
    sh.exec(item)
    } catch (error) {
      sh.echo(error)
    }
  });
  
  downloads.forEach(item => {
    try {
      download(item)
    } catch (error) {
      sh.echo(error)
    }
  });

  downloads.forEach(item => {
    try {
      sh.rm('-rf', item)
    } catch (error) {
      sh.exec(error)
    }
  })
}
main()