import random as rd


def maquina():
    jugada = rd.randrange(0, 3)
    if jugada == 0:
        return 'Piedra'
    if jugada == 1:
        return 'Papel'
    if jugada == 2:
        return 'Tijera'


def match(jugada, juego_maquina):
    if jugada == juego_maquina:
        return 0
    if jugada == 'piedra' and juego_maquina == 'tijera':
        return 1
    if jugada == 'piedra' and juego_maquina == 'papel':
        return -1
    if jugada == 'papel' and juego_maquina == 'piedra':
        return 1
    if jugada == 'papel' and juego_maquina == 'tijera':
        return -1
    if jugada == 'tijera' and juego_maquina == 'papel':
        return 1
    if jugada == 'tijera' and juego_maquina == 'piedra':
        return -1


def resultado(resultado):
    if resultado == 0:
        return 'Empate'
    if resultado > 0:
        return 'Ganaste'
    if resultado < 0:
        return 'Perdiste'
