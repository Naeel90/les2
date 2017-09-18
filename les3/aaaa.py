mylist=['ahmad','ali','mosa','hasan']
def swa(mylist):

      if len(mylist) > 1:
           mylist[0],mylist[-1]=mylist[-1],mylist[0]
           print (mylist)


swa(mylist)
