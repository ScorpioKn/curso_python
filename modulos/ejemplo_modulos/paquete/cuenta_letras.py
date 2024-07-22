def f_cuenta_letras(txt:str):
    contador=0
    for n in txt:
        if n != " ":
            contador+=1
    return contador
