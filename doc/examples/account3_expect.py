import pexpect

def run(name,opts,res,spawn):
    child = spawn('./{}'.format(name))
    try:
        child.expect('>')
        child.sendline('account.deposit(5)')
        child.expect('>')
        child.sendline('ask_and_check_balance')
        child.expect('ask')
        child.expect(r'\?')
        child.sendline('4')
        child.expect('1')
        child.expect('>')
        child.sendline('ask_and_check_balance')
        child.expect('ask')
        child.expect(r'\?')
        child.sendline('6')
        child.expect('0')
        return True
    except pexpect.EOF:
        print(child.before)
        return False
