#encoding:utf-8

from microcomputador import Microcomputador

class Servidor(Microcomputador):
	servidores = []

	def __init__(self, codigo_patrimonio, descricao, capacidade_do_hd, quantidade_de_ram, estacao, quantidade_maxima_de_buffer):
		self.codigo_patrimonio = codigo_patrimonio
		self.descricao = descricao
		self.capacidade_do_hd = capacidade_do_hd
		self.quantidade_de_ram = quantidade_de_ram
		self.estacao = estacao
		self.quantidade_maxima_de_buffer = quantidade_maxima_de_buffer
		self.impressoras_conectadas = 0
		Servidor.adicionar_servidor(self)

	@staticmethod
	def adicionar_servidor(servidor):
		Servidor.servidores.append(servidor)

