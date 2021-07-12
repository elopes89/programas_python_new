while True:
    compras = float(input('Valor total das compras? '))
    money = float(input('Valor Recebido: '))
    troco = money - compras
    cinq = troco // 50
    resto50 = troco - (cinq * 50)
    vint = resto50 // 20
    resto20 = troco - ((cinq * 50)+(vint * 20))
    dez = resto20 // 10
    resto10 = troco - ((cinq * 50)+(vint * 20) +(dez * 10))
    cinco = resto10 // 5
    res5 = troco - ((cinq * 50)+(vint * 20) +(dez * 10)+(cinco * 5))
    dois = res5 // 2
    resto2 = troco - ((cinq * 50)+(vint * 20) +(dez * 10) + (cinco * 5)+(dois * 2))
    um = resto2 // 1
    
    resto1 = troco - ((cinq * 50)+(vint * 20)+(dez * 10)+(cinco * 5)+(dois * 2)+(um * 1))
    fifty = resto1 // 0.5
    restofifty = troco - ((cinq * 50)+(vint * 20)+(dez * 10)+(cinco * 5)+(dois * 2)+(um * 1)+(fifty * 0.5))
    vc = restofifty // 0.25
    break


if money <= compras:
    print('Não há troco')
else:
    print('troco:', "%.2f" % troco)
    if cinq > 0:
        print("%.0f" % cinq, 'nota(s): R$ 50,00')
    if vint > 0:
        print("%.0f" % vint, 'nota(s): R$ 20,00')
    if dez > 0:
        print("%.0f" % dez, 'nota(s): R$ 10,00')
    if cinco > 0:
        print("%.0f" % cinco, 'nota(s): R$ 5,00')
    if dois > 0:
        print("%.0f" % dois, 'nota(s): R$ 2,00')
    if um > 0:
        print("%.0f" % um, 'moeda(s): R$ 1,00')
        
    if fifty > 0:
        print("%.0f" % fifty, 'moeda(s): R$ 0,50')
    if vc > 0:
        print("%.0f" % vc, 'moeda(s): R$ 0,25')
   



    