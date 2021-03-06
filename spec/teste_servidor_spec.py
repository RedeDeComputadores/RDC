#encoding:utf-8

import unittest
from should_dsl import should
from servidor import Servidor

class TestServidor(unittest.TestCase):
	def it_teste_deve_criar_um_servidor(self):
		servidor = Servidor(codigo_patrimonio=10, descricao='oi', capacidade_do_hd=5, quantidade_de_ram=8, estacao=1,
quantidade_maxima_de_buffer=10)
		servidor.codigo_patrimonio |should| equal_to(10)
		servidor.descricao |should| equal_to('oi')
		servidor.capacidade_do_hd |should| equal_to(5)
		servidor.quantidade_de_ram |should| equal_to(8)
		servidor.estacao |should| equal_to(1)
		servidor.quantidade_maxima_de_buffer |should| equal_to(10)

	def it_teste_deve_criar_uma_lista_de_servidores(self):
		servidor2 = Servidor(codigo_patrimonio=11, descricao='tim', capacidade_do_hd=5, quantidade_de_ram=8, estacao=1, quantidade_maxima_de_buffer=10)
		servidor3 = Servidor(codigo_patrimonio=12, descricao='vivo', capacidade_do_hd=5, quantidade_de_ram=8, estacao=1, quantidade_maxima_de_buffer=10)
		Servidor.servidores |should| have(3).itens

if __name__ == "__main__":
	unittest.main()

