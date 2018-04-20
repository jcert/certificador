import sys
import csv

if len(sys.argv)==2:
	if sys.argv[1]=="-h":
		print("use:"+sys.argv[0]+ " <template svg> <commonevent info> <user data in cvs format>") 
	if sys.argv[1]=="-g":
		example_common = """pronome_evento,x 
tipo_evento,encontros
nome_evento,Grupo de Estudos
dia_ou_dias,em 1/02/99
qtd_horas,80h
primeira_assinatura,João Silva
primeiro_cargo,Ajudante
segunda_assinatura,Cristiano
segundo_cargo,Presidente
data,1/04/99"""
		example_users ="""nome,atuacao
joão,jogador
maria,advogada"""
		try:
			open("common.csv","r")
		except Exception:
			with open("common.csv","w") as f:
				f.write(example_common)
		try:
			open("users.csv","r")
		except Exception:
			with open("users.csv","w") as f:
				f.write(example_users)
	exit()

if len(sys.argv)!=4:
	print("use:"+sys.argv[0]+ " <template svg> <commonevent info> <user data in cvs format>") 
	exit()


print(sys.argv[0])#name
print(sys.argv[1])#template svg
print(sys.argv[2])#common event info
print(sys.argv[3])#user data in cvs format 


try:
	open(sys.argv[1],"r")
	open(sys.argv[2],"r")
	open(sys.argv[3],"r")
except Exception:
	raise

#read common event info 
common_info = {}
with open(sys.argv[2],"r") as f:
	common = csv.reader(f, delimiter=',')
	for row in common:
		common_info[row[0]] = row[1]

#read user data and make many svg for each user
with open(sys.argv[3],"r") as f:
	data = csv.DictReader(f, delimiter=',')
	with open(sys.argv[1],"r") as template_file:
		template = template_file.read()
		for key in common_info:
			template = template.replace("^$"+key+"$&amp;",common_info[key])
		for row in data:
			certificate = template
			for key in row:
				certificate = certificate.replace("^$"+key+"$&amp;",row[key])
			identifier = row["nome"]
			with open("certificado_"+identifier+".svg","w") as certificado_file:
				certificado_file.write(certificate)		

#create pdf for each user
#delete svgs





