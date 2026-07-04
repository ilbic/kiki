class Position:
    def __init__(self):
        # having initially defined the bitboards and position metadata
        # without self, I realised I'd be essentially updating the "blueprint"
        # rather than the specific instance - self is necessary here. 


        # Bitboards
        self.white_pawns = 0
        self.white_knights = 0
        self.white_bishops = 0
        self.white_rooks = 0
        self.white_queens = 0
        self.white_king = 0

        self.black_pawns = 0
        self.black_knights = 0
        self.black_bishops = 0
        self.black_rooks = 0
        self.black_queens = 0
        self.black_king = 0

        # Position metadata
        self.active_colour = "w"
        self.castling_rights = ""
        self.en_passant = None
        self.halfmove_clock = 0
        self.fullmove_number = 1
        
    def place_piece_on_square(self, square_number, char):
            
        match char:
            case "b":
                print("found a black bishop")
            case "n":
                print("found a black knight")
            case "r":
                print("found a black rook")
            case "k":
                print("found a black king")
            case "q":
                print("found a black queen")
            case "p":
                print("found a black pawn")
            case "B":
                print("found a white bishop")
            case "N":
                print("found a white knight")
            case "R":
                print("found a white rook")
            case "K":
                print("found a white king")
            case "Q":
                print("found a white queen")
            case "P":
                print("found a white pawn")