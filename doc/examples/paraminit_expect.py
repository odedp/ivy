import pexpect

def run(name,opts,res,spawn):
    child = spawn('./{} 0'.format(name))
    try:
        child.expect('>')
        child.sendline('foo.get_bit')
        child.expect(r'= 0')
        return True
    except pexpect.EOF:
        print(child.before)
        return False
    finally:
        child.close()
        
