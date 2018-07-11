#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter

try:
    from .termo import TermoColecao, Termo
    from .frequency import inverse_frequency as idf_class
    from .documento import Documento
except ImportError:
    from termo import TermoColecao, Termo
    from frequency import inverse_frequency as idf_class
    from documento import Documento

from .probabilistic import get_top_l_sentences, get_top_k_words


class Colecao(object):
    def __init__(self):
        self.qtDocumentos = 0
        self.listTermosColecao = []
        self.listDocuments = []
        self.tokens = {}
        self.idf = {}

        self.qtToken = 0
        self.qtStopword = 0
        self.qtAdverbio = 0

        self.qtTermoDocumento = {}
        self.algoritmo = {'tf': 'DoubleNormalization',  # RawFrequency, DoubleNormalization, LogNormalization
                          'idf': 'InverseFrequencySmooth',  # InverseFrequency, InverseFrequencySmooth
                          'tfidf': 'TFIDF'}  # TFIDF

    def __str__(self):
        return 'qtDocumentos: ' + str(self.qtDocumentos) + ', qtWord: ' + \
               str(self.qtToken) + ', qtStopword: ' + str(self.qtStopword) + \
               ', qtAdverbio: ' + str(self.qtAdverbio)

    def addDocumento(self, nome, text):
        posicao = self.pesquisarDocumento(nome)
        if posicao == -1:
            doc = Documento(nome, text)
            doc.remove_stopwords()
            doc.processar(self)

            self.qtToken += doc.qtTokenTotal
            self.qtStopword += doc.qtStopwordTotal
            self.qtAdverbio += doc.qtAdverbioTotal

            self.listDocuments.append(doc)
            self.qtDocumentos += 1
            self.updateIdf()
            return doc
        else:
            print('O documento %s já está na coleção' % (nome))
            return -1

    def pesquisarWord(self, word):
        if word in self.listTermosColecao:
            return self.listTermosColecao.index(word)
        return -1

    def pesquisarDocumento(self, nome):
        for doc in self.listDocuments:
            if nome == doc:
                return self.listDocuments.index(doc)
        return -1

    def updateIdf(self):
        # print('Colecao().updateIdf()')
        strategyIDF = self.instanciar(idf_class, self.algoritmo['idf'])
        self.idf = {}
        for key in self.qtTermoDocumento:
            self.idf[key] = strategyIDF.calcPeso(self.qtDocumentos, self.qtTermoDocumento[key])
        return self.idf

    def instanciar(self, origem, nome):
        try:
            return getattr(origem, nome)()
        except AttributeError:
            print('Error, a classe %s não existe' % (nome))

    def calcular_similaridade(self, consulta):
        idf = self.idf
        docs = self.listDocuments

        result = {}
        for doc in docs:
            sum_q = sum_d = similaridade = 0.0
            for termo in doc.tf:
                idff = 0.0
                if termo in idf:
                    idff = idf[termo]
                sum_d += (doc.tf[termo] * idff) ** 2

            for termo in consulta.tokens:
                idff = 0.0
                if termo in idf:
                    idff = idf[termo]
                sum_q += (consulta.tokens[termo] * idff) ** 2

            for word in consulta.tokens:
                doc_weight = 0.0
                if word in doc.listaTermos:
                    doc_weight = doc.tf[word] * idf[word]
                idff = 0.0
                if word in idf:
                    idff = idf[word]
                similaridade += consulta.tokens[word] * (idff * doc_weight)
            sum_q = sum_q ** (0.5)
            sum_d = sum_d ** (0.5)
            if sum_d == 0.0 or sum_q == 0.0:
                similaridade = 0.0
            else:
                similaridade = similaridade / (sum_q * sum_d)
            if similaridade > 0.0:
                result[doc.nome] = similaridade
        print('... colecao()calcular_similaridade()  result: ', result)
        return sort_dic(result, 1, True)

    def calcular_similaridade_x(self, consulta):
        # put your stuff
        docs = self.listDocuments
        words = self.listTermosColecao
        print('setup terms and docs [OK]')
        k_words = get_top_k_words(words, 300)
        result = get_top_l_sentences(docs, consulta, k_words, 300)
        print('get top sentences [OK]')
        return sort_dic(result, 1, True)


def sort_dic(dic, indice=0, reverse=False):
    return sorted(dic.items(), key=itemgetter(indice), reverse=reverse)
