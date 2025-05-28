#media com while
# 'nota_total' e o acumulador de notas
nota_total = 0
bimestre = 0

while bimestre < 4:
    nota = float(input('digite a nota do aluno: '))
    nota_total += nota #acumulado a nota total 
    bimestre += 1
    print(f'a{nota} digitada do aluno foi armazenada com sucesso!')
    
media = nota_total / 4 # calculando a media apos sair do loop
print(f'a media do aluno e {media}')
