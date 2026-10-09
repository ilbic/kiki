from position import Position
from bitboards import (
    WHITE_PAWNS,
    WHITE_ROOKS,
    WHITE_KNIGHTS,
    WHITE_BISHOPS,
    WHITE_QUEEN,
    WHITE_KING,
    BLACK_PAWNS,
    BLACK_ROOKS,
    BLACK_KNIGHTS,
    BLACK_BISHOPS,
    BLACK_QUEEN,
    BLACK_KING,
)

def set_starting_position(position):
    position.white_pawns = WHITE_PAWNS
    position.white_rooks = WHITE_ROOKS
    position.white_knights = WHITE_KNIGHTS
    position.white_bishops = WHITE_BISHOPS
    position.white_queens = WHITE_QUEEN
    position.white_king = WHITE_KING

    position.black_pawns = BLACK_PAWNS
    position.black_rooks = BLACK_ROOKS
    position.black_knights = BLACK_KNIGHTS
    position.black_bishops = BLACK_BISHOPS
    position.black_queens = BLACK_QUEEN
    position.black_king = BLACK_KING