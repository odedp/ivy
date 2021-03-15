import pexpect

def run(name,opts,res,spawn):
    child = spawn('./{}'.format(name))
    try:
        child.expect('>')
        child.sendline('account.withdraw(4)')
        child.expect('assumption failed')
        return True
    except pexpect.EOF:
        print(child.before)
        return False
