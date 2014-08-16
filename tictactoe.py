# -*- coding: utf-8 -*-
"""
  ----------------------------------------------------------------------
  |  tictactoe.py
  |  ------------
  |
  |  Programa para jogo da velha
  |  
  |  :copyright: © 2014 By Helder e Lucas Morais
  |  :license: BSD, see LICENSE for more details.
  |
  ----------------------------------------------------------------------
"""

import sys
import os
from random import randint

jogo = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]


def mostra():
    print '              1   2   3               '
    print
    print '         1    ' + jogo[0][0] + '   ' + jogo[0][1] + '   ' + jogo[0][2]
    print
    print '         2    ' + jogo[1][0] + '   ' + jogo[1][1] + '   ' + jogo[1][2]
    print
    print '         3    ' + jogo[2][0] + '   ' + jogo[2][1] + '   ' + jogo[2][2]
    print


computador = 0
humano = 0

while (1):
    os.system('cls')
    mostra()

    if (jogo[0][0] == 'O' and jogo[0][1] == 'O' and jogo[0][2] == 'O') or \
            (jogo[1][0] == 'O' and jogo[1][1] == 'O' and jogo[1][2] == 'O') or \
            (jogo[2][0] == 'O' and jogo[2][1] == 'O' and jogo[2][2] == 'O') or \
            (jogo[0][0] == 'O' and jogo[1][1] == 'O' and jogo[2][2] == 'O') or \
            (jogo[0][2] == 'O' and jogo[1][1] == 'O' and jogo[2][0] == 'O') or \
            (jogo[0][0] == 'O' and jogo[1][0] == 'O' and jogo[2][0] == 'O') or \
            (jogo[0][1] == 'O' and jogo[1][1] == 'O' and jogo[2][1] == 'O') or \
            (jogo[0][2] == 'O' and jogo[1][2] == 'O' and jogo[2][2] == 'O'):
        print
        print "            COMPUTADOR GANHOU"
        sys.exit()

    if (jogo[0][0] == 'X' and jogo[0][1] == 'X' and jogo[0][2] == 'X') or \
            (jogo[1][0] == 'X' and jogo[1][1] == 'X' and jogo[1][2] == 'X') or \
            (jogo[2][0] == 'X' and jogo[2][1] == 'X' and jogo[2][2] == 'X') or \
            (jogo[0][0] == 'X' and jogo[1][1] == 'X' and jogo[2][2] == 'X') or \
            (jogo[0][2] == 'X' and jogo[1][1] == 'X' and jogo[2][0] == 'X') or \
            (jogo[0][0] == 'X' and jogo[1][0] == 'X' and jogo[2][0] == 'X') or \
            (jogo[0][1] == 'X' and jogo[1][1] == 'X' and jogo[2][1] == 'X') or \
            (jogo[0][2] == 'X' and jogo[1][2] == 'X' and jogo[2][2] == 'X'):
        print
        print "          HUMANO GANHOU"
        sys.exit()

    # EMPATE
    achou = 0
    for (i, linha) in enumerate(jogo):
        if achou:
            break;
        for (c, coluna) in enumerate(linha):
            if coluna in '_':
                achou = 1
                break
    if achou == 0:
        print
        print "  ->         EMPATE "
        sys.exit()

    linha = int(raw_input(' Linha: '))
    coluna = int(raw_input(' Coluna: '))

    # Valida numero da linha e coluna
    if (linha < 1 or linha > 3) or (coluna < 1 or coluna > 3):
        continue

    # Permitido colocar um O em qualquer lugar onde nao tenha um X nem uma O
    if jogo[linha - 1][coluna - 1] != '_':
        continue;
    jogo[linha - 1][coluna - 1] = 'X'

    # AI - Jogar no meio se tiver vazio
    if jogo[1][1] == '_':
        jogo[1][1] = 'O'
        continue

    # IA - Ataque quando tiver 2 pontos
    if jogo[0][0] == '_' and jogo[0][1] == 'O' and jogo[0][2] == 'O':
        jogo[0][0] = 'O'
        continue
    if jogo[0][1] == '_' and jogo[0][0] == 'O' and jogo[0][2] == 'O':
        jogo[0][1] = 'O'
        continue
    if jogo[0][2] == '_' and jogo[0][0] == 'O' and jogo[0][1] == 'O':
        jogo[0][2] = 'O'
        continue
    if jogo[1][0] == '_' and jogo[1][1] == 'O' and jogo[1][2] == 'O':
        jogo[1][0] = 'O'
        continue
    if jogo[1][1] == '_' and jogo[1][0] == 'O' and jogo[1][2] == 'O':
        jogo[1][1] = 'O'
        continue
    if jogo[1][2] == '_' and jogo[1][0] == 'O' and jogo[1][1] == 'O':
        jogo[1][2] = 'O'
        continue
    if jogo[2][0] == '_' and jogo[2][1] == 'O' and jogo[2][2] == 'O':
        jogo[2][0] = 'O'
        continue
    if jogo[2][1] == '_' and jogo[2][0] == 'O' and jogo[2][2] == 'O':
        jogo[2][1] = 'O'
        continue
    if jogo[2][2] == '_' and jogo[2][0] == 'O' and jogo[2][1] == 'O':
        jogo[2][2] = 'O'
        continue

    if jogo[0][0] == '_' and jogo[1][0] == 'O' and jogo[2][0] == 'O':
        jogo[0][0] = 'O'
        continue
    if jogo[0][1] == '_' and jogo[1][1] == 'O' and jogo[2][1] == 'O':
        jogo[0][1] = 'O'
        continue
    if jogo[0][2] == '_' and jogo[1][2] == 'O' and jogo[2][2] == 'O':
        jogo[0][2] = 'O'
        continue
    if jogo[1][0] == '_' and jogo[0][0] == 'O' and jogo[2][0] == 'O':
        jogo[1][0] = 'O'
        continue
    if jogo[1][1] == '_' and jogo[0][1] == 'O' and jogo[2][1] == 'O':
        jogo[1][1] = 'O'
        continue
    if jogo[1][2] == '_' and jogo[0][2] == 'O' and jogo[2][2] == 'O':
        jogo[1][2] = 'O'
        continue
    if jogo[2][0] == '_' and jogo[0][0] == 'O' and jogo[1][0] == 'O':
        jogo[2][0] = 'O'
        continue
    if jogo[2][1] == '_' and jogo[0][1] == 'O' and jogo[1][1] == 'O':
        jogo[2][1] = 'O'
        continue
    if jogo[2][2] == '_' and jogo[0][2] == 'O' and jogo[1][2] == 'O':
        jogo[2][2] = 'O'
        continue

    if jogo[0][0] == '_' and jogo[1][1] == 'O' and jogo[2][2] == 'O':
        jogo[0][0] = 'O'
        continue
    if jogo[1][1] == '_' and jogo[0][0] == 'O' and jogo[2][2] == 'O':
        jogo[1][1] = 'O'
        continue
    if jogo[2][2] == '_' and jogo[0][0] == 'O' and jogo[1][1] == 'O':
        jogo[2][2] = 'O'
        continue
    if jogo[0][2] == '_' and jogo[1][1] == 'O' and jogo[2][0] == 'O':
        jogo[0][2] = 'O'
        continue
    if jogo[1][1] == '_' and jogo[0][2] == 'O' and jogo[2][0] == 'O':
        jogo[1][1] = 'O'
        continue
    if jogo[2][0] == '_' and jogo[1][1] == 'O' and jogo[0][2] == 'O':
        jogo[2][0] = 'O'
        # input('chegou')
        continue



    # IA - Defesa colocar X onde tiver 2 pontos
    if jogo[0][0] == '_' and jogo[0][1] == 'X' and jogo[0][2] == 'X':
        jogo[0][0] = 'O'
        continue
    if jogo[0][1] == '_' and jogo[0][0] == 'X' and jogo[0][2] == 'X':
        jogo[0][1] = 'O'
        continue
    if jogo[0][2] == '_' and jogo[0][0] == 'X' and jogo[0][1] == 'X':
        jogo[0][2] = 'O'
        continue
    if jogo[1][0] == '_' and jogo[1][1] == 'X' and jogo[1][2] == 'X':
        jogo[1][0] = 'O'
        continue
    if jogo[1][1] == '_' and jogo[1][0] == 'X' and jogo[1][2] == 'X':
        jogo[1][1] = 'O'
        continue
    if jogo[1][2] == '_' and jogo[1][0] == 'X' and jogo[1][1] == 'X':
        jogo[1][2] = 'O'
        continue
    if jogo[2][0] == '_' and jogo[2][1] == 'X' and jogo[2][2] == 'X':
        jogo[2][0] = 'O'
        continue
    if jogo[2][1] == '_' and jogo[2][0] == 'X' and jogo[2][2] == 'X':
        jogo[2][1] = 'O'
        continue
    if jogo[2][2] == '_' and jogo[2][0] == 'X' and jogo[2][1] == 'X':
        jogo[2][2] = 'O'
        continue

    if jogo[0][0] == '_' and jogo[1][0] == 'X' and jogo[2][0] == 'X':
        jogo[0][0] = 'O'
        continue
    if jogo[0][1] == '_' and jogo[1][1] == 'X' and jogo[2][1] == 'X':
        jogo[0][1] = 'O'
        continue
    if jogo[0][2] == '_' and jogo[1][2] == 'X' and jogo[2][2] == 'X':
        jogo[0][2] = 'O'
        continue
    if jogo[1][0] == '_' and jogo[0][0] == 'X' and jogo[2][0] == 'X':
        jogo[1][0] = 'O'
        continue
    if jogo[1][1] == '_' and jogo[0][1] == 'X' and jogo[2][1] == 'X':
        jogo[1][1] = 'O'
        continue
    if jogo[1][2] == '_' and jogo[0][2] == 'X' and jogo[2][2] == 'X':
        jogo[1][2] = 'O'
        continue
    if jogo[2][0] == '_' and jogo[0][0] == 'X' and jogo[1][0] == 'X':
        jogo[2][0] = 'O'
        continue
    if jogo[2][1] == '_' and jogo[0][1] == 'X' and jogo[1][1] == 'X':
        jogo[2][1] = 'O'
        continue
    if jogo[2][2] == '_' and jogo[0][2] == 'X' and jogo[1][2] == 'X':
        jogo[2][2] = 'O'
        continue

    if jogo[0][0] == '_' and jogo[1][1] == 'X' and jogo[2][2] == 'X':
        jogo[0][0] = 'O'
        continue
    if jogo[1][1] == '_' and jogo[0][0] == 'X' and jogo[2][2] == 'X':
        jogo[1][1] = 'O'
        continue
    if jogo[2][2] == '_' and jogo[0][0] == 'X' and jogo[1][1] == 'X':
        jogo[2][2] = 'O'
        continue
    if jogo[0][2] == '_' and jogo[1][1] == 'X' and jogo[2][0] == 'X':
        jogo[0][2] = 'O'
        continue
    if jogo[1][1] == '_' and jogo[0][2] == 'X' and jogo[2][0] == 'X':
        jogo[1][1] = 'O'
        continue
    if jogo[2][0] == '_' and jogo[1][1] == 'X' and jogo[0][2] == 'X':
        jogo[2][0] = 'O'
        # input('chegou')
        continue


    # IA - Lista opcoes disponiveis
    disponiveis = []
    for (i, linha) in enumerate(jogo):
        for (c, coluna) in enumerate(linha):
            if coluna in '_':
                disponiveis.append([i, c])


    # print disponiveis
    quantidade = len(disponiveis)
    if quantidade > 0:
        x = randint(2, quantidade) - 1
        coluna = disponiveis[x]
        jogo[coluna[0]][coluna[1]] = 'O'
        # print quantidade
        # print x
        #sys.exit()
