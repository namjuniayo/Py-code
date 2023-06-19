import json

proggramm=True
vvodmark=0
vvodpersons=0



with open("ucenik", "r") as fp:
    ucenik=json.load(fp)
with open("mark", "r") as fp:
    mark=json.load(fp)



markv=[]
markk=0
markprint=[0,0,0,0]
markprintt=[]


while proggramm==True:
    print(*ucenik, sep=", ")
    print('Введите номер учинека что бы перейти к его оценкам')
    print('0 - Введите что бы доабвить учиника')

    vvodpersons=int(input())
    if vvodpersons==0:
        ucenik.append(str(input("Введите имя")))
    elif vvodpersons<1 or vvodpersons>len(ucenik):
        print("Ошибка, попробуйте ещё раз")

    else:
        print('Вы выбрали ученика по имени', ucenik[vvodpersons-1] )
        print('Выбери действие:')
        print('1 - Посмотреть оценки')
        print('2 - Посмотреть среднестатитическую оценку')
        print('3 - Добавиь оценку')
        print('4 - Выйти')
        vvodmark=str(input(': '))
        if vvodmark=='3':
            while vvodmark=='3':
                markv.append(int(input('Введите оценку')))
                vvodmark=str(input('Введите 3 что бы поставить ещё одну оценку, введите 0 число чтобы выйти'))
                if vvodmark !='0' and vvodmark!='3':
                    print('Ошибка')
                    while vvodmark!='0' or vvodmark!='0':
                        vvodmark=str(input('Введите 3 что бы поставить ещё одну оценку, введите 0 число чтобы выйти'))

            mark.append(markv)
            markv=[]
        elif vvodmark=='2':
            if mark==[]:
                print('Оценок пока нет!')
            else:
                markk=0

                for i in mark[vvodpersons-1]:
                    markk+=i
                print(markk/len(mark[vvodpersons-1]))
        elif vvodmark=='1':
            dva=0
            tri=0
            chet=0
            pyat=0
            if mark==[]:
                print('Оценок пока нет!')
            else:
                markprint=[0,0,0,0]
                markprintt=mark[vvodpersons-1]
                for i in markprintt:
                    if i==2:
                        markprint[0]+=1
                    elif i==3:
                        markprint[1]+=1
                    elif i==4:
                        markprint[2]+=1
                    elif i==5:
                        markprint[3]+=1
                print(markprint[0] , '- двоек')
                print(markprint[1], '- троек')
                print(markprint[2], '- четвёрок')
                print(markprint[3], '- пятёрок')

                
                # print(*mark[vvodpersons-1], sep=", ")
            
        elif vvodmark=="4":
            proggramm=False
        else:
            print("Ошибка! ПРоверьте написаник, не должно быть пробелов и лишних знаков!")





with open("ucenik", "w") as fp:
    json.dump(ucenik, fp)
    
with open("mark", "w") as fp:
    json.dump(mark, fp)