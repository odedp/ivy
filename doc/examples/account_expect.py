import pexpect


def run(name,opts,res,spawn):
    child = spawn('./{}'.format(name))
    try:
        child.expect('>')
        child.sendline('account.get_balance')
        child.expect('0')
        child.expect('>')
        child.sendline('account.deposit(5)')
        child.expect('>')
        child.sendline('account.get_balance')
        child.expect('5')
        child.expect('>')
        child.sendline('account.withdraw(2)')
        child.expect('>')
        child.sendline('account.get_balance')
        child.expect('3')
        child.expect('>')
        child.sendline('account.withdraw(4)')
        child.expect('>')
        child.sendline('account.get_balance')
        child.expect('65535')
        return True
    except pexpect.EOF:
        print(child.before)
        return False
