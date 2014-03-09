#encoding:utf-8

import unittest
from should_dsl import should
from impressora import Impressora

class TestImpressora(unittest.TestCase):

	def it_teste_deve_criar_uma_impressora(self):
		impressora = Impressora(10, 'impressora', 100)
		impressora.codigo_patrimonio |should| equal_to(10)
		impressora.descricao |should| equal_to('impressora')
		impressora.velocidade |should| equal_to(100)

if __name__ == "__main__":
	unittest.main()