# =+
def checkMagazine(m,n,b):
  for i in n:
    print(i,end='')
  print('')
  for i in b:
    print(i,end='')

  return None

















if __name__ == '__main__':
    test = int(input())

    for i in range(test):
      number = int(input())
      necklace = sorted(list(int(i) for i in input().split()))
      bracelet = sorted(list(int(i) for i in input().split()))
      checkMagazine(number,necklace, bracelet)



    # 