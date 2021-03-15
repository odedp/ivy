import pexpect

def run(name,opts,res,spawn):
    child = [spawn('./{} {}'.format(name,idx)) for idx in range(2)]
    try:
        # child[0].expect('>')
        child[0].expect(r'< serv.elect')
        return True
    except pexpect.EOF:
        print(child.before)
        return False
    finally:
        for idx in range(2):
            child[idx].close()
