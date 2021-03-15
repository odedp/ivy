import pexpect


def run(name,opts,res,spawn):
    child = spawn('./{}'.format(name))
    try:
        child.expect('>')
        child.sendline('hello')
        child.expect('< world')
        return True
    except pexpect.EOF:
        print(child.before)
        return False
