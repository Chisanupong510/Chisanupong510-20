sum = 0 
i=1


while i<=10:
    print('Frame # %d' %i)
    while True:
        n=int(input('Number of pins down:'))
        if n==10:
            print('Strike')
            i+=1
            sum +=n
            break
        j= int(input('Number of pins down'))
        m= n+j
        if m==10:
            print('Spare')
            i+=1
            sum +=m
            break
        if m<10 :
            print('Open Frame')
            i+=1
            sum +=m
            break
print('total score is %d' %sum)