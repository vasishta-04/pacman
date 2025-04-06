from ghosts import dfs_class

class utility:
    def __init__(self) -> None:
        self.num_nodes=0

    def get_utility(self, state):
        state.num_nodes_explored += 1
        self.num_nodes+=1

        if state.get_pos_pacman() == state.get_pos_ghost(1) or state.get_pos_pacman() == state.get_pos_ghost(2):
            return state.score - 10000000

        return (
            state.score
            + dfs_class(state.get_board(),state.get_size(),state.get_pos_pacman()
                        ).find_len_path(state.get_pos_ghost(1)[0],state.get_pos_ghost(1)[1],state.get_pos_pacman())*1000000
            + dfs_class(state.get_board(),state.get_size(),state.get_pos_pacman()
                        ).find_len_path(state.get_pos_ghost(2)[0],state.get_pos_ghost(2)[1],state.get_pos_pacman())*1000
        )

    def is_game_finished(self, state):
        return (
            self.is_pacman_win(state)
            or state.get_pos_pacman() == state.get_pos_ghost(1)
            or state.get_pos_pacman() == state.get_pos_ghost(2)
        )

    def is_pacman_win(self, state):
        for row in state.get_board():
            if "*" in row:
                return False
        return True

    def distance_from_near_food(self, state):
        board = state.get_board()
        size = state.get_size()
        pos_pacman = state.get_pos_pacman()

        sizes = list()
        for i in range(size[0]):
            for j in range(size[1]):
                if board[i][j] == "*":
                    sizes.append(self._euclidean_distance((i, j), pos_pacman))
        return min(sizes)

    def distance_from_near_food(self, state):
        pos_pacman = state.get_pos_pacman()
        ghosts1 = state.get_pos_ghost(1)
        ghosts2 = state.get_pos_ghost(2)

        ed1, ed2 = self._euclidean_distance(
            pos_pacman, ghosts1
        ), self._euclidean_distance(pos_pacman, ghosts2)
        return min(ed1, ed2)

    def _euclidean_distance(self, point1, point2):
        import math as m

        return m.sqrt(pow(point1[0] - point1[0], 2) + pow(point2[0] - point2[0], 2))
