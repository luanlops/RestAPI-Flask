from models import Pessoas, Usuarios, db_session

#Inserir dados na tabela 
def insere_pessoas():
    pessoa = Pessoas(nome='Luan', idade=25)
    print(pessoa)
    pessoa.save()

#consultar dados inseridos na tabela
def consulta():
    pessoas = Pessoas.query.all()
    
    pessoa = Pessoas.query.filter_by(nome='Luan').first()
    print({pessoa.idade, pessoa.nome})

#Alterar dados na tabela
def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Luan').first()
    pessoa.idade = 40
    pessoa.save()

#excluir dados da tabela 
def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Paulo').first()
    pessoa.delete()

def inserir_usuario(login, senha):
    usuarios = Usuarios(login=login, senha=senha)
    usuarios.save()

def consulta_usuario():
    usuarios = Usuarios.query.all()
    print(usuarios)

#Funcao para chamar os metodos
if __name__ == '__main__':
    #inserir_usuario('luan','123')
    #onsulta_usuario()
    insere_pessoas()
    #alterar_pessoa()
    #excluir_pessoa()
    consulta()