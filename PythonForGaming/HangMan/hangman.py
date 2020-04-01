from engine.engineHangman import HangMan
import sys


def main(args):
    hang = HangMan()
    palabra = hang.obtenerPalabra()
    hang.jugar(palabra)
    while input('Te vuelvo a ganar insecto? [S/N]: ').upper() == 'Y':
        palabra = hang.obtenerPalabra()
        hang.jugar(palabra)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
