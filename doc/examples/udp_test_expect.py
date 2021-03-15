import pexpect

def run(name,opts,res,spawn):
    child = spawn('./{}'.format(name))
    try:
        child.expect('>')
        child.sendline('foo.send(0,1,2)')
        child.expect(r'< foo.recv\(1,2\)')
        child.sendline('foo.send(1,0,3)')
        child.expect(r'foo.recv\(0,3\)')
        return True
    except pexpect.EOF:
        print(child.before)
        return False
