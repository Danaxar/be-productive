let {PythonShell} = require('python-shell')

const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => {
  createWindow()

PythonShell.run('killer.py', null, function (err) {
  if (err) throw err;
  console.log('finished');
});


})

