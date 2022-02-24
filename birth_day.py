def birthdate():
    import datetime

    print('input your birthdate (00/00/0000)')
    x = input()


    d,m,y = x.split('/')
    d,m,y = [int(d),
            int(m),
            int(y)]
        
    x = datetime.datetime(y,m,d)


    print(x.strftime('%A'))

birthdate()