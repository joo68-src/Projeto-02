from basic_players import Player
from random import choice as ch

# Implemente neste arquivo seus jogadores

# Estratégia que criamos. 
class NormalPlayer(Player):

    def __init__(self):
        super().__init__(0, "Not So Dummie")

    def play(self, board_extremes, play_hist):
        playable_tiles = self._tiles

        if len(board_extremes) > 0:
            if board_extremes[0] >= board_extremes[1]:
                biggest_extreme = board_extremes[0]
                lowest_extreme = board_extremes[1]
            else: 
                biggest_extreme = board_extremes[1]
                lowest_extreme = board_extremes[0]
            
            playable_tiles = [tile for tile in self._tiles if tile[0] == biggest_extreme or tile[1] == biggest_extreme]

        # Caso não haja nenhuma peça que possa ser colocada no extremo de maior valor do tabuleiro, eles usam a maior peça possível que pode ser usada no menor extremo. Isso aproxima eles da nossa estratégia: usar a menor peça possível, mas que tenha uma pontuação razoável
        if len(playable_tiles) == 0 and len(board_extremes) > 0:
            playable_tiles = [tile for tile in self._tiles if tile[0] == lowest_extreme or tile[1] == lowest_extreme]
            highest = -1
            tile_sum = -1
            for i in range(len(playable_tiles)):
                if playable_tiles[i][0] + playable_tiles[i][1] > tile_sum:
                    tile_sum = playable_tiles[i][0] + playable_tiles[i][1]
                    highest = i
            if highest >= 0:
                return 1, playable_tiles[highest]
            else: 
                return 1, None
        else:
            lowest_tile = 18
            lowest_tile_position = -1

            # Implementação da nossa estratégia

            # O que queremos fazer é aplicar a maior peça possível que force o oponente a jogar uma peça pequena.
            for tile in range(len(playable_tiles)):
                if playable_tiles[tile][0] + playable_tiles[tile][1] < lowest_tile:
                    lowest_tile = playable_tiles[tile][0] + playable_tiles[tile][1]
                    lowest_tile_position = tile
            if lowest_tile_position != -1:
                return 1, playable_tiles[lowest_tile_position]
            else:
                return 1, None

# Função que define o nome da dupla:
def pair_name():
    return "kinda dummies" # Defina aqui o nome da sua dupla

# Função que cria a dupla:
def create_pair():
    return (NormalPlayer(), NormalPlayer()) # Defina aqui a dupla de jogadores. Deve ser uma tupla com dois jogadores.	
