nome = (input())

acertos1 = (input())
acertos2 = (input())
acertos3 = (input())
acertos4 = (input())
acertos5 = (input())
acertos6 = (input())
nota1 = float(acertos1)
nota2 = float(acertos2)
nota3 = float(acertos3)
nota4 = float(acertos4) / 6 * 10
nota5 = float(acertos5) / 6 * 10
nota6 = float(acertos6) / 6 * 10
media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6) / 6
acertos = [acertos1,acertos2,acertos3,acertos4,acertos5,acertos6]
nao_respondidas = sum(1 for acerto in acertos if acerto == 0)
print(f"A média de {nome} é {media:.1f}")
if nota1 <= nota2 <= nota3 <= nota4 <= nota5 <= nota6:
    print("Progresso constante! Parabéns pelo esforço!")
else:
    print("Alerta! Queda no rendimento")
if nao_respondidas >= 2:
    print("Alerta! Múltiplas listas não respondidas.")
if media >= 8:
    print('Parabéns pelo excelente desempenho! Continue "au" sim.')
elif 7<= media < 8:
    print("Parabéns pelo bom desempenho!")
elif media < 7 :
    print("Alerta! Desempenho abaixo do esperado.")
   


