proggramm=True
vvodmark=0
vvodpersons=0
ucenik=[]
mark=[]
markv=[]
markk=0
while proggramm==True:
    print(*ucenik, sep=", ")
    print('Введите номер учинека что бы перейти к его оценкам')
    print('Введите 0, что бы доабвить учиника')
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
            if mark==[]:
                print('Оценок пока нет!')
            else:
                print(*mark[vvodpersons-1], sep=", ")
            
        elif vvodmark=="4":
            proggramm=False
        else:
            print("Ошибка! ПРоверьте написаник, не должно быть пробелов и лишних знаков!")