#faca while if
#print("Salve")

#n1 = 2

#n2 = 3

#soma= n1+ n2



#print(soma)

#if(soma>6):
   #print(maior que 6)

#for i range(10)
    #print(i)


def media(n):
    soma=0
    media=0
    while(n != 0 and n > 0):
        n = input('Digite a nota')
        soma = soma + int(n)
        n = int(n) - 1 


    media = soma/n


    print("media é "+ str(media) )

    if(media<6):
        print("Vermelha")
    else:
        print("Azul")


x = input('Digite a quantidade de notas')
media(x)


        

        

