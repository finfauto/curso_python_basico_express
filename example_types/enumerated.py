from enum import Enum


class ResultadoQuiniela(Enum):
    HOME_WINS = 0
    DRAW = 1
    AWAY_WINS = 2


print(ResultadoQuiniela.HOME_WINS)
resultado_quiniela = ResultadoQuiniela.AWAY_WINS
if resultado_quiniela == ResultadoQuiniela.AWAY_WINS:
    print("Visiting team won")
