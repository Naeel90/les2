def keercijfersom( item ):
    return (642%10) *100 + (int(item/10) %10) *10 + int(item/100)
numlist = [314 , 315, 642, 246, 129, 999]
numlist.sort( key=keercijfersom )
print( numlist )
