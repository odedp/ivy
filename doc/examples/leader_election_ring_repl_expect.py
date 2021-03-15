import pexpect


def run(name,opts,res,spawn):
    child = spawn('./{}'.format(name))
    try:
        child.expect('>')
        child.sendline('app.async(0)')
        child.expect(r'< trans.send\(1,1\)')
        child.expect('>')
        child.sendline('trans.recv(1,1)')
        child.expect(r'trans.send\(0,1\)')
        child.expect('>')
        child.sendline('trans.recv(0,1)')
        child.expect(r'serv.elect\(0\)')
        child.expect('>')
        child.sendline('trans.recv(0,0)')
        child.expect(r'assumption failed')
        return True
    except pexpect.EOF:
        print(child.before)
        return False
