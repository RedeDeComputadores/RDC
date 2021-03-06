#encoding:utf-8

import unittest
from should_dsl import should
from microcomputador import Microcomputador
from impressora import Impressora


class TestMicrocomputador(unittest.TestCase):
	def it_teste_deve_criar_um_microcomputador(self):
		micro = Microcomputador(codigo_patrimonio=9, descricao='oi', capacidade_do_hd=500, quantidade_de_ram=2, estacao=1)
		micro.codigo_patrimonio |should| equal_to(9)
		micro.descricao |should| equal_to('oi')
		micro.capacidade_do_hd |should| equal_to(500)
		micro.quantidade_de_ram |should| equal_to(2)
		micro.estacao |should| equal_to(1)		

if __name__ == "__main__":
	unittest.main()
