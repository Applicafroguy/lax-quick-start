const sh = require('shelljs')

try {
    sh.echo('Package has some issues within running within NPM. Opening browser to documentation for manual install. Cheers!')
    sh.exec('python3 open.py')
} catch (error) {
    sh.echo(error + ' was found')
    sh.exit(1)
}

