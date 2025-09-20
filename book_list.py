list1=['history']
list2=['sport']
list3=['roman']
list4=['learning']
list5=['offer']

while True :
    print('\n')
    print ('(( OFFICIAL LIBRARY ))')
    print ('\n')
    print ('(1).adding book') 
    print ('(2).show your list')
    print ('(3).search your book')
    print ('(4).offer book')
    print ('(5).exit')
    print ('----------------------')

    user= input ('select one  : ')
  
    if user == '1' :
        print('....... types ......   ')
        print('1.history      2.sport ')
        print('3.roman        4.learning ')
        print('5.offer (just for admin)')
        print('\n')
        A = input ('_select your book type : ')
        B = input ('_enter your book name : ')
        if A in list1 :
            list1.append(B)
            print('* the book added *')
        elif A in list2 :
            list2.append(B)
            print('* the book added *')
        elif A in list3 :
            list3.append(B)
            print('* the book added *')
        elif A in list4 :
            list4.append(B)
            print('* the book added *')
        elif A in list5 :
            list5.append(B)
            print ('* the book added *')
        else :
            print ('there is no type ') 
    
    elif user == '2' :
        print ('....library lists....')
        print('list1 = history')
        print('list2 = sport')
        print('list3 = roman')
        print('list4 = learning')
        # print('list5 = offer book')
        print('-----------------------')
        C = input (' witch type of list ? ')
        if C == 'history' :
            for i in list1 :
                print (i)
        elif C == 'sport' :
            for n in list2 :
                print (n)
        elif C == 'roman' :
            for m in list3 :
                print (m)
        elif C == 'learning' :
            for z in list4 :
                print (z)   
        # elif C == 'offer' :
        #     code = 4321
        #     S = input ('please enter code : ') 
        #     if S == code :
        #         print ('right code')
        #     for t in list5 :
        #         print (t)
        # else :
        #     print ('wrong list')
        
        
    elif user == '3' :
        print ('   search mode...  ')
        X = input ('search your book name : ')
        for u in list1 :
          if X in list1 :
            print ('# in history list')
            break  
        for y in list2 : 
          if X in list2 :
            print ('# in sport list ') 
            break 
        for p in list3 :
          if X in list3 :
            print ('# in roman list ')
            break
        for l in list4 :
          if X in list4 :
            print ('# in learning list ')
            break 
        # else :
        #    print ('no book in list')  
          
    elif user == '4' :
        print ('  offer list !')
        code = 1234
        D = input('please enter offer code : ')
        if D == code :
            print ('your offer books ')
            for j in list5 :
                print (j)
        # else :
        #     print ('wrong code!!')


    elif user == '5' :
        print ('see you soon :) ')
        break




         
