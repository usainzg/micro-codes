import ftplib

def getConnection(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('usainzg', 'mofeta')
        print('\n[x]' + str(hostname) + ' FTP login success!')
        return ftp
    except:
        print('\n[x]' + str(hostname) + ' FTP login failed!')
        return False

def changeDir(ftp, dir):
    ftp.cwd(dir)

def listDir(ftp):
    print(ftp.retrlines('LIST'))
    
def closeConnection(ftp):
    ftp.quit()

def createDir(ftp, name):
    ftp.mkd('./' + name)

    
hostname = '192.168.56.101'
ftpClient = getConnection(hostname)

changeDir(ftpClient, '/home/usainzg/FTP')
createDir(ftpClient, 'prueba')
changeDir(ftpClient, '/home/usainzg/FTP/prueba')
listDir(ftpClient)
closeConnection(ftpClient)

