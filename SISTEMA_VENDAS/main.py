from produto import Produto
from venda import Venda
from pagamento_debito import PagamentoDebito
from pagamento_pix import PagamentoPix
from pagamento_dinheiro import PagamentoDinheiro
from pagamento_cartao import PagamentoCartao
from datetime import datetime


# OS PRODUTOS

produto1 = Produto(1, "Mouse", 100.00, "Mouse Gamer", 20)
produto2 = Produto(2, "Teclado", 180.00, "Teclado Mecânico", 20)
produto3 = Produto(3, "Monitor", 1000.00, "Monitor 24 polegadas", 20)


# CONTADOR ANTES DAS VENDAS

print(f"Vendas no sistema: {Venda.get_total_vendas()}")


# TESTE: MESMA COMPRA, FORMAS DE PAGAMENTO DIFERENTES

formas_de_pagamento = [
    PagamentoDebito(),
    PagamentoPix(),
    PagamentoDinheiro(),
    PagamentoCartao(),
]

for numero, pagamento in enumerate(formas_de_pagamento, start=1):
    print(f"\n##### VENDA {numero} - {pagamento.nome} #####")

    venda = Venda(numero, datetime.now(), pagamento)

    venda.adicionar_item(produto1, 2)
    venda.adicionar_item(produto2, 1)
    venda.adicionar_item(produto3, 1)

    venda.finalizar_venda()


# CONTADOR DEPOIS DAS VENDAS

print(f"\nVendas no sistema: {Venda.get_total_vendas()}")


# VISUALIZAR O ESTOQUE

print("\n========== ESTOQUE ==========")

for produto in (produto1, produto2, produto3):
    print(f"{produto.nome}: {produto.verificarEstoque()}")