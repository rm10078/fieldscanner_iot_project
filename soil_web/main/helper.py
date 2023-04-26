
from datetime import datetime
def empty_check(sen):
    if sen in '':
        return False
    else:
        return True
def password_check(data1,data2):
    if len(data1)>7 and data1==data2:
        return True
    else:
        return False


if __name__=='__main__':
  pass