from padroes.meta_singleton import MetaSingleton

"""Classe utilizada como exemplo"""


class ExemploSingleton(metaclass=MetaSingleton):
    pass


"""instancia de classes ExemploSingleton"""
n = ExemploSingleton()
m = ExemploSingleton()

"""Resultado: criamos uma instancia da classe ExemploSingleton que funciona como ponto de acesso global."""
"""Dessa forma toda classe instanciada ira acessar a mesma instancia."""
"""um bom exemplo de utilização desse padrão
 seria a utilização dele em um projeto que necessite de uma infraestrutura para controle do log de dados."""
print(n == m) # Resultado: True
