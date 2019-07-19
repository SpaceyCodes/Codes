import hashlib
passwd = {1:hashlib.sha3_512('qwerty'.encode()).hexdigest()}
data = []
with open("/WEN KANG/Coding/source/repos/hashed passwords/pass.txt","r", errors='ignore') as f:
    data = f.readlines()
def start():
    x = 0
    y = 0
    while y <110000:
        dataknown = data[x]
        while '\n' in dataknown:
            dataknown = dataknown.replace('\n', '')
        x += 1
        checkpass = hashlib.sha3_512(dataknown.encode()).hexdigest()
        if passwd.get(1) == checkpass:
            print ('|Found Password| |Found on line:%s|' %x)
            print ('|Password:%s|' %dataknown)
            break
        else:
            print ('Line:%s ' %x, 'Original:%s' %dataknown)
        checkpass = hashlib.sha3_512(str(y).encode()).hexdigest()
        y += 1
        if str(passwd.get(1)) == checkpass:
            print ('|Found Password| |Found on line:%s|' %x)
            print ('|Password:%s|' %y)
            break
        else:
            print ('Line:%s ' %x, 'Original:%s' %y)

start()
