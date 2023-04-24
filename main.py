import colorama  # type: ignore
from playsound import playsound # type: ignore
colorama.just_fix_windows_console()

# Funktion gibt den Inhalt einer Zelle des Spielfeldes zurück, wenn die Zelle innerhalb des Spielfeldes liegt


def get(matrix, x, y):

    try:
        if x < 0 or y < 0:
            return False
        return matrix[y][x]
    except:
        return False

# Klasse Board erstellt das Spielfeld und verwaltet die Spielregeln


class Board:

    # Konstruktor der Klasse Board
    def __init__(self, players=[colorama.Fore.RED+"⬤"+colorama.Style.RESET_ALL, colorama.Fore.BLUE+"⬤"+colorama.Style.RESET_ALL]):
        # Erstellt ein leeres Spielfeld
        self.board = [[" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "]]
        # Speichert die Spieler
        self.players = players
        # speichert die Gewinnmuster
        self.winpatterns = [[[-3, 0], [-2, 0], [-1, 0], [0, 0]],
                            [[-2, 0], [-1, 0], [0, 0], [1, 0]],
                            [[-1, -1], [0, 0], [1, 1], [2, 2]],
                            [[0, 0], [1, 1], [2, 2], [3, 3]],
                            [[3, 0], [2, 0], [1, 0], [0, 0]],
                            [[2, 0], [1, 0], [0, 0], [-1, 0]],
                            [[1, -1], [0, 0], [-1, 1], [-2, 2]],
                            [[0, 0], [-1, 1], [-2, 2], [-3, 3]],
                            [[-3, 0], [-2, 0], [-1, 0], [0, 0]],
                            [[-2, 0], [-1, 0], [0, 0], [1, 0]],
                            [[-1, 1], [0, 0], [1, -1], [2, -2]],
                            [[0, 0], [1, -1], [2, -2], [3, -3]],
                            [[3, 0], [2, 0], [1, 0], [0, 0]],
                            [[2, 0], [1, 0], [0, 0], [-1, 0]],
                            [[1, 1], [0, 0], [-1, -1], [-2, -2]],
                            [[0, 0], [-1, -1], [-2, -2], [-3, -3]],
                            [[0, 0], [0, 1], [0, 2], [0, 3]],
                            [[0, 0], [0, -1], [0, -2], [0, -3]],
                            [[0, -1], [0, 0], [0, 1], [0, 2]],
                            [[0, 1], [0, 0], [0, -1], [0, -2]]]

    # Funktion fügt einen Spielstein in das Spielfeld ein
    def play(self, player: str, row: int):
        # Das Spielfeld wird umgedreht, da die Spielsteine bei play() von oben nach unten eingefügt werden
        self.board.reverse()
        # Schleife, die durch das Spielfeld geht und den Spielstein an die erste freie Stelle setzt
        for i, c in enumerate(self.board):
            if c[row] == " ":
                c[row] = player
                break
        # Umgedrehtes Spielfeld wird wieder in den Ursprungszustand gebracht
        self.board.reverse()
        # Koordinaten des Spielsteins werden zurückgegeben
        return [row, len(self.board)-i-1]

    # Funktion überprüft, ob ein Spieler gewonnen hat
    def check_win(self, cords: list):
        # Schleife, die durch alle Gewinnmuster geht und überprüft, ob 4 Steine in einer Reihe liegen
        for i in self.winpatterns:
            if get(self.board, cords[0] + i[0][0], cords[1] + i[0][1]) == get(self.board, cords[0] + i[1][0], cords[1] + i[1][1]) == get(self.board, cords[0] + i[2][0], cords[1] + i[2][1]) == get(self.board, cords[0] + i[3][0], cords[1] + i[3][1]) != " ":
                # Wenn 4 Steine in einer Reihe liegen, wird der Inhalt der Zelle (Spieler) zurückgegeben
                return get(self.board, cords[0] + i[0][0], cords[1] + i[0][1])

    # Funktion gibt das Spielfeld als String zurück

    def __str__(self):
        string = "  1   2   3   4   5   6   7"
        for i in self.board:
            string += "\n" + "--" * len(self.board[0]) * 2 + "-\n|"
            for j in i:
                string += f" {j} |"

        return string


# Funktion, die die Hauptschleife des Spiels enthält
def main():

    # Spielfeld wird erstellt
    board = Board()
    # Endlosschleife, die durch die Spieler geht und für jeden eine Eingabe abfragt
    while True:
        for player in board.players:
            print(board)
            # Spielstein wird an einer Spalte eingefügt. wenn der Spieler keine Zahl zwischen 1 und 7 eigibt, wird erneut abgefragt.
            while True:
                try:
                    col = input(f"{player} pick column: ")
                    if col == "Blutwurstblase":
                        board = Board()
                        col = input(f"{player} pick column: ")
                    elif col == "":
                        playsound("assets/easteregg.mp3")
                    if 0 < int(col) < 8:
                        break
                    print("invalid input(valid: 1-7)")
                except ValueError:
                    print("invalid input(valid: 1-7)")

            cords = board.play(player, int(col) - 1)
            # Gewinner wird überprüft
            winner = board.check_win(cords)
            if winner:

                # Wenn ein Gewinner gefunden wurde, wird das Spielfeld ausgegeben und der Gewinner angezeigt
                print(board)
                print(f"{winner} won!")
                return
            # Spielfeld wird ausgegeben
            


# Prüft, ob das Programm direkt gestartet wurde
if __name__ == "__main__":
    main()
