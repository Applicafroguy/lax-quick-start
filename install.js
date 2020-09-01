const shell = require('shelljs')

function download(){
  shell.exec('python3 init.py')
}

download()
