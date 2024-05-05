from User import user
from SumEqual import SumEquals
  
if __name__ == '__main__':
    user = user()
    nums, target = user.userInput()
    se = SumEquals(nums, target)
    result = se.sumEquals()
    print(result)