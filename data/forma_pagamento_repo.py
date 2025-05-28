from typing import Optional
from data.forma_pagamento_model import FormaPagamento
from data.forma_pagamento_sql import *
from data.util import get_connection


def criar_tabela() -> bool:            #retorna se a tabela foi criada ou nao (true - maior que 0(linhas afetadas) ou false) #select n precisa de comit
    with get_connection() as conn:     #com o with, nao precisa fechar a conexao, ele fecha automaticamente
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return cursor.rowcount > 0     #retorna o numero de linhas afetadas pelo comando, no caso, a tabela criada


def inserir(forma_pagamento: FormaPagamento) -> Optional[int]:  #retorna oq está dentro dos colchetes ou none
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            forma_pagamento.nome, 
            forma_pagamento.desconto))
        id_inserido = cursor.lastrowid     #retorna o id do ultimo registro inserido
        return id_inserido

                                                       #select retorna dados. fetchall traz tudo. fatone - traz um registro. fatmany - traz em lotes

def obter_todas() -> list[FormaPagamento]:             #se nao tiver nada parece lista vazia
    with get_connection() as conn:                          
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [FormaPagamento(
            id=row["id"], 
            nome=row["nome"], 
            desconto=row["desconto"])
            for row in rows]
