

#abrir arquivo
f = open("sinalização.csv")

for line in f:     #p/ cada linha do arq eu quero fazer um print
  print(line.strip().split(";")) #o strip tira os espaços em branco e o /n, e o split divide a linha em colunas,
