class Endereco(object):
    logradouro = ''
    cep = None
    cidade = ''
    estado = ''
    def __init__(self, logradouro = None, cep = None, cidade = None, estado = None ):
        self.logradouro = logradouro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
class Pessoa(object):
    nome =''
    idade = None
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
        self.endereco = Endereco ()

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = None
    def __int__(self, cpf = None , nome = None, idade = None):
        Pessoa.__init__(self,Nome, idade)
        self.cpf = cpf

class Tarefa(object):
    descricao = ''
    datainic = None
    datafim = None
    prioridade = None
    def __init__(self,descricao = None, datainic = None, datafim = None):
        Pessoa.__init__(self, cpf, nome, idade)
        self.descricao = descricao
        self.datainic = datainic
        self.datafim = datafim

    def __str__(self):
        return self.descricao

class Projeto(object):
    Nome = ''
    def __init__(self, nome=None):
    Tarefa.__init__(self, descricao, datainic, datafim )
        self.nome

    def __str__(self):
        return self.Nome

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj = None, nome = None, descricao = None):
        Pessoa.__init__(self, nome,)
        self.cnpj = cpnj
        self.Tarefa = Tarefa()

        def __str__(self):
            return self.cnpj
