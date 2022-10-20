# Author: Kevin Riemer
# GitHub username: khriemer2596
# Date: 8/1/2022
# Description: Simulates a working Ludo Game


class Player:
    """Represents a player in the Ludo Game"""

    def __init__(self, player_pos):
        """Initialize variables"""
        self._player_pos = player_pos
        if self._player_pos == 'A':  # set start/end spaces per player position
            self._start_space = 1
            self._end_space = 50

        elif self._player_pos == 'B':
            self._start_space = 15
            self._end_space = 8

        elif self._player_pos == 'C':
            self._start_space = 29
            self._end_space = 22

        elif self._player_pos == 'D':
            self._start_space = 43
            self._end_space = 36

        self._current_space_token_p = -1  # token starts in home yard
        self._current_space_token_q = -1  # token starts in home yard
        self._current_pos_token_p = 'H'  # token starts in home yard
        self._current_pos_token_q = 'H'  # token starts in home yard
        self._current_state = 'STILL PLAYING'  # default player state

    def set_current_space_token_p(self, space_p):
        """Set current numbered space of player token p"""
        self._current_space_token_p = space_p

    def get_start_space(self):
        """Get method for the start space of any player"""
        return self._start_space

    def set_current_space_token_q(self, space_q):
        """Set current numbered space of player token q"""
        self._current_space_token_q = space_q

    def get_current_space_token_p(self):
        """Get method for the current space of each player's token p"""
        return self._current_space_token_p

    def get_current_space_token_q(self):
        """Get method for the current space of each player's token q"""
        return self._current_space_token_q

    def set_current_token_p_pos(self, new_state_p):
        """Set current type of space for player token p"""
        self._current_pos_token_p = new_state_p

    def set_current_token_q_pos(self, new_state_q):
        """Set current type of space for player token q"""
        self._current_pos_token_q = new_state_q

    def get_current_token_p_pos(self):
        """Get method for the current type of space for token p"""
        return self._current_pos_token_p

    def get_current_token_q_pos(self):
        """Get method for the current type of space for token q"""
        return self._current_pos_token_q

    def set_current_player_state(self, new_state):
        """Set the current state of the player"""
        self._current_state = new_state

    def get_current_player_state(self):
        """Get method for the current state of the player"""
        return self._current_state

    def get_completed(self):
        """Returns True or False if the player has finished or not finished the game"""
        if self._current_state == 'HAS WON AND FINISHED THE GAME':
            return True
        else:
            return False

    def get_token_p_step_count(self):
        """Returns total steps that token p has taken on the board"""
        if self._current_pos_token_p == 'H':  # if token p is in the home yard
            step_count_p = -1
            return step_count_p
        elif self._current_pos_token_p == 'R':  # if token p is in the ready to go space
            step_count_p = 0
            return step_count_p
        elif self._current_pos_token_p == 'E':  # if token p is in the finishing square
            step_count_p = 57
            return step_count_p
        else:
            if self._player_pos != 'A':  # player A's tokens will never go above 56
                step_count_p = (56 - self._start_space) + self._current_space_token_p + 1
                return step_count_p
            else:
                step_count_p = self._current_space_token_p - self._start_space + 1
                return step_count_p

    def get_token_q_step_count(self):
        """Returns total steps that token q has taken on the board"""
        if self._current_pos_token_q == 'H':  # same process as get token p step count
            step_count_q = -1
            return step_count_q
        elif self._current_pos_token_q == 'R':
            step_count_q = 0
            return step_count_q
        elif self._current_pos_token_q == 'E':
            step_count_q = 57
            return step_count_q
        else:
            if self._player_pos != 'A':
                step_count_q = (56 - self._start_space) + self._current_space_token_q + 1
                return step_count_q
            else:
                step_count_q = self._current_space_token_q - self._start_space + 1
                return step_count_q

    def get_space_name(self, steps_taken):
        """Returns the name of the space the token has landed on on the board as a string"""
        if steps_taken == -1:
            space_name = 'H'
            return space_name
        elif steps_taken == 0:
            space_name = 'R'
            return space_name
        elif 57 > steps_taken > 50:
            space_name = steps_taken - 50
            return self._player_pos + str(space_name)  # format the space name if the token is in the home squares
        elif steps_taken == 57:
            space_name = 'E'
            return space_name
        elif steps_taken == 1:
            space_name = self._start_space
            return str(space_name)
        else:
            if self._start_space + (steps_taken - 1) > 56:  # if the token has gone around the board, past square 56
                space_name = self._start_space + (steps_taken - 1) - 56
                return str(space_name)
            else:
                space_name = self._start_space + steps_taken - 1
                return str(space_name)


class LudoGame:
    """Represents the simulated Ludo Game"""

    def __init__(self):
        """Initialize variables"""
        self._list_of_players = []  # list of player position strings
        self._player_obj_dict = {}  # dictionary with player position strings as keys and player objects as values

    def get_player_by_position(self, player_pos):
        """Returns the player object based on the given player position"""
        if player_pos not in self._list_of_players:
            return "Player not found!"
        else:
            return self._player_obj_dict[player_pos]

    def move_token(self, player_obj, token_name, steps_to_move):
        """Moves the given player's token on the board by the amount of steps_to_move"""
        if player_obj.get_current_player_state() == 'HAS WON AND FINISHED THE GAME':  # check if player is finished
            return

        if token_name == 'p':  # moves token p
            pre_move_space = player_obj.get_current_space_token_p()
            post_move_space = pre_move_space + steps_to_move
            player_obj.set_current_space_token_p(post_move_space)
            if player_obj.get_current_token_p_pos() == 'H':  # moves token p out of home yard
                player_obj.set_current_space_token_p(0)
                player_obj.set_current_token_p_pos('R')
                return

            if player_obj.get_current_token_p_pos() == 'R':  # moves token p on board
                if player_obj == self._player_obj_dict['A']:
                    player_obj.set_current_space_token_p(post_move_space)
                    player_obj.set_current_token_p_pos('SOMEWHERE ON THE BOARD')
                else:
                    player_obj.set_current_space_token_p(player_obj.get_start_space() + steps_to_move - 1)
                    player_obj.set_current_token_p_pos('SOMEWHERE ON THE BOARD')
            elif player_obj.get_current_token_p_pos() == 'SOMEWHERE ON THE BOARD' and 51 <= player_obj.get_token_p_step_count() <= 56:  # enters home squares
                player_obj.set_current_space_token_p(post_move_space)
                player_obj.set_current_token_p_pos('IN HOME SQUARES')
            elif player_obj.get_current_token_p_pos() == 'IN HOME SQUARES':  # enters finishing square
                if player_obj.get_token_p_step_count() == 57:
                    player_obj.set_current_space_token_p(post_move_space)
                    player_obj.set_current_token_p_pos('E')
                    if player_obj.get_current_token_p_pos() == 'E' and player_obj.get_current_token_q_pos() == 'E':
                        player_obj.set_current_player_state('HAS WON AND FINISHED THE GAME')
                elif player_obj.get_token_p_step_count() > 57:  # bounce back case
                    over_step = player_obj.get_token_p_step_count() - 57
                    if player_obj == self._player_obj_dict['A']:
                        player_obj.set_current_space_token_p(player_obj.get_current_space_token_p() - (2 * over_step))
                    else:
                        player_obj.set_current_space_token_p(57 + player_obj.get_start_space() - over_step)
                else:
                    player_obj.set_current_space_token_p(post_move_space)

                if player_obj.get_current_token_p_pos() == 'E' and player_obj.get_current_token_q_pos() == 'E':
                    player_obj.set_current_player_state('HAS WON AND FINISHED THE GAME')

            elif player_obj.get_current_token_p_pos() == 'SOMEWHERE ON THE BOARD':  # regular move around board
                if post_move_space > 56:
                    player_obj.set_current_space_token_p(post_move_space - 56)
                    player_obj.set_current_token_p_pos('SOMEWHERE ON THE BOARD')
                else:
                    player_obj.set_current_space_token_p(post_move_space)
                    player_obj.set_current_token_p_pos(
                        'SOMEWHERE ON THE BOARD')  # updates current space and token's total steps

        elif token_name == 'q':  # same as above but for token q
            pre_move_space = player_obj.get_current_space_token_q()
            post_move_space = pre_move_space + steps_to_move
            player_obj.set_current_space_token_q(post_move_space)
            if player_obj.get_current_token_q_pos() == 'H':
                player_obj.set_current_space_token_q(0)
                player_obj.set_current_token_q_pos('R')
                return

            if player_obj.get_current_token_q_pos() == 'R':
                if player_obj == self._player_obj_dict['A']:
                    player_obj.set_current_space_token_q(post_move_space)
                    player_obj.set_current_token_q_pos('SOMEWHERE ON THE BOARD')
                else:
                    player_obj.set_current_space_token_q(player_obj.get_start_space() + steps_to_move - 1)
                    player_obj.set_current_token_q_pos('SOMEWHERE ON THE BOARD')
            elif player_obj.get_current_token_q_pos() == 'SOMEWHERE ON THE BOARD' and 51 <= player_obj.get_token_q_step_count() <= 56:
                player_obj.set_current_space_token_q(post_move_space)
                player_obj.set_current_token_q_pos('IN HOME SQUARES')
            elif player_obj.get_current_token_q_pos() == 'IN HOME SQUARES':  # enters finishing square
                if player_obj.get_token_q_step_count() == 57:
                    player_obj.set_current_space_token_q(post_move_space)
                    player_obj.set_current_token_q_pos('E')
                    if player_obj.get_current_token_p_pos() == 'E' and player_obj.get_current_token_q_pos() == 'E':
                        player_obj.set_current_player_state('HAS WON AND FINISHED THE GAME')
                elif player_obj.get_token_q_step_count() > 57:  # bounce back case
                    over_step = player_obj.get_token_q_step_count() - 57
                    if player_obj == self._player_obj_dict['A']:
                        player_obj.set_current_space_token_q(player_obj.get_current_space_token_q() - (2 * over_step))
                    else:
                        player_obj.set_current_space_token_q(57 + player_obj.get_start_space() - over_step)
                else:
                    player_obj.set_current_space_token_q(post_move_space)

                if player_obj.get_current_token_p_pos() == 'E' and player_obj.get_current_token_q_pos() == 'E':
                    player_obj.set_current_player_state('HAS WON AND FINISHED THE GAME')
            elif player_obj.get_current_token_q_pos() == 'SOMEWHERE ON THE BOARD':
                if post_move_space > 56:
                    player_obj.set_current_space_token_q(post_move_space - 56)
                    player_obj.set_current_token_q_pos('SOMEWHERE ON THE BOARD')
                else:
                    player_obj.set_current_space_token_q(post_move_space)
                    player_obj.set_current_token_q_pos('SOMEWHERE ON THE BOARD')

        for player in self._player_obj_dict:  # handles kicking out an opponent token
            while player_obj != self._player_obj_dict[player]:
                if player_obj.get_current_space_token_p() > 0 and player_obj.get_current_space_token_p() == \
                        self._player_obj_dict[player].get_current_space_token_p() and self._player_obj_dict[
                    player].get_current_token_p_pos() == 'SOMEWHERE ON THE BOARD':
                    self._player_obj_dict[player].set_current_space_token_p(-1)
                    self._player_obj_dict[player].set_current_token_p_pos('H')
                if player_obj.get_current_space_token_p() > 0 and player_obj.get_current_space_token_p() == \
                        self._player_obj_dict[player].get_current_space_token_q() and self._player_obj_dict[
                    player].get_current_token_q_pos() == 'SOMEWHERE ON THE BOARD':
                    self._player_obj_dict[player].set_current_space_token_q(-1)
                    self._player_obj_dict[player].set_current_token_q_pos('H')
                if player_obj.get_current_space_token_q() > 0 and player_obj.get_current_space_token_q() == \
                        self._player_obj_dict[player].get_current_space_token_p() and self._player_obj_dict[
                    player].get_current_token_p_pos() == 'SOMEWHERE ON THE BOARD':
                    self._player_obj_dict[player].set_current_space_token_p(-1)
                    self._player_obj_dict[player].set_current_token_p_pos('H')
                if player_obj.get_current_space_token_q() > 0 and player_obj.get_current_space_token_q() == \
                        self._player_obj_dict[player].get_current_space_token_q() and self._player_obj_dict[
                    player].get_current_token_q_pos() == 'SOMEWHERE ON THE BOARD':
                    self._player_obj_dict[player].set_current_space_token_q(-1)
                    self._player_obj_dict[player].set_current_token_q_pos('H')
                break

    def play_game(self, players_list, turns_list):
        """Simulates the Ludo Game based on the players that are playing and the turns given"""
        for position in players_list:
            self._list_of_players.append(position)  # add players to the list of players

        for player in players_list:
            self._player_obj_dict[player] = (
                Player(player))  # creates the dictionary with player strings as keys and player objs as values

        # decision-making algorithm
        for turn in turns_list:
            current_player = self._player_obj_dict[turn[0]]  # gets the current player object who is taking the turn
            dice_roll = turn[1]  # gets the dice roll of the turn
            temp_copy_of_dict = dict(self._player_obj_dict)  # temporary copy of the current instance of the player dict
            del temp_copy_of_dict[turn[0]]  # deletes the current player from the temporary copy of the player dict
            list_of_other_players = []
            for other_player in temp_copy_of_dict.keys():
                list_of_other_players.append(
                    other_player)  # builds the list of opponents not playing this turn which will be used in the algorithm below

            if dice_roll == 6 and current_player.get_current_token_p_pos() == 'H':
                self.move_token(current_player, 'p', 0)  # case of token p being able to get to ready space
            elif dice_roll == 6 and current_player.get_current_token_q_pos() == 'H':
                self.move_token(current_player, 'q', 0)  # case of token q being able to get to ready space
            elif current_player.get_current_token_p_pos() == 'IN HOME SQUARES' and current_player.get_current_space_token_p() + dice_roll - current_player.get_start_space() + 1 == 57:
                self.move_token(current_player, 'p', dice_roll)  # case of token p being in home square and dice roll is
                # exactly what is needed to reach end square
            elif current_player.get_current_token_q_pos() == 'IN HOME SQUARES' and current_player.get_current_space_token_q() + dice_roll - current_player.get_start_space() + 1 == 57:
                self.move_token(current_player, 'q', dice_roll)  # case of token q being in home square and dice roll is
                # exactly what is needed to reach end square
            elif len(list_of_other_players) == 1 and current_player.get_current_space_token_p() >= 0 and (
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_p() or
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_q()):
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                else:
                    self.move_token(current_player, 'p',
                                    dice_roll)  # case of token p being able to move and kick out an opponent token
            elif len(list_of_other_players) == 2 and (current_player.get_current_space_token_p() >= 0 and (
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_p() or
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_q() or
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[1]].get_current_space_token_p() or
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[1]].get_current_space_token_q())):
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                else:
                    self.move_token(current_player, 'p',
                                    dice_roll)  # case of token p being able to move and kick out an opponent token
            elif len(list_of_other_players) == 3 and (current_player.get_current_space_token_p() >= 0 and (
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_p() or
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_q() or
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[1]].get_current_space_token_p() or
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[1]].get_current_space_token_q() or
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[2]].get_current_space_token_p() or
                    current_player.get_current_space_token_p() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[2]].get_current_space_token_q())):
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                else:
                    self.move_token(current_player, 'p',
                                    dice_roll)  # case of token p being able to move and kick out an opponent token
            elif len(list_of_other_players) == 1 and (
                    current_player.get_current_space_token_q() >= 0 and current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_p() or
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_q()):
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                else:
                    self.move_token(current_player, 'q',
                                    dice_roll)  # case of token q being able to move and kick out an opponent token
            elif len(list_of_other_players) == 2 and (current_player.get_current_space_token_q() >= 0 and (
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_p() or
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_q() or
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[1]].get_current_space_token_p() or
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[1]].get_current_space_token_q())):
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                else:
                    self.move_token(current_player, 'q',
                                    dice_roll)  # case of token q being able to move and kick out an opponent token
            elif len(list_of_other_players) == 3 and (current_player.get_current_space_token_q() >= 0 and (
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_p() or
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[0]].get_current_space_token_q() or
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[1]].get_current_space_token_p() or
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[1]].get_current_space_token_q() or
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[2]].get_current_space_token_p() or
                    current_player.get_current_space_token_q() + dice_roll ==
                    self._player_obj_dict[list_of_other_players[2]].get_current_space_token_q())):
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked and being able to move and kick out an opponent token
                else:
                    self.move_token(current_player, 'q',
                                    dice_roll)  # case of token q being able to move and kick out an opponent token
            elif dice_roll != 6 and current_player.get_current_token_p_pos() == 'H' and current_player.get_current_token_q_pos() != 'H':
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked
                else:
                    self.move_token(current_player, 'q', dice_roll)  # case when only token q can move
            elif dice_roll != 6 and current_player.get_current_token_q_pos() == 'H' and current_player.get_current_token_p_pos() != 'H':
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked
                else:
                    self.move_token(current_player, 'p', dice_roll)  # case when only token p can move
            elif current_player.get_token_p_step_count() > current_player.get_token_q_step_count():
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked
                else:
                    self.move_token(current_player, 'q',
                                    dice_roll)  # case of moving token q if it's further from the finishing square than p
            elif current_player.get_token_p_step_count() <= current_player.get_token_q_step_count():
                if current_player.get_current_space_token_p() == current_player.get_current_space_token_q() and current_player.get_current_space_token_p() > 0:
                    self.move_token(current_player, 'p', dice_roll)  # case of tokens being stacked
                    self.move_token(current_player, 'q', dice_roll)  # case of tokens being stacked
                else:
                    self.move_token(current_player, 'p',
                                    dice_roll)  # case of moving token p if it's further from the finishing square than q

        current_token_space_list = []
        for player_obj in self._player_obj_dict.values():  # build the  list of current token positions in string format
            if player_obj.get_current_token_p_pos() == 'SOMEWHERE ON THE BOARD':
                current_token_space_list.append(repr(player_obj.get_current_space_token_p()))
            elif player_obj.get_current_token_p_pos() == 'E':
                space = player_obj.get_current_space_token_p()
                current_token_space_list.append(player_obj.get_space_name(space))
            else:
                steps = player_obj.get_token_p_step_count()
                current_token_space_list.append(player_obj.get_space_name(steps))

            if player_obj.get_current_token_q_pos() == 'SOMEWHERE ON THE BOARD':
                current_token_space_list.append(repr(player_obj.get_current_space_token_q()))
            elif player_obj.get_current_token_q_pos() == 'E':
                space = player_obj.get_current_space_token_q()
                current_token_space_list.append(player_obj.get_space_name(space))
            else:
                space = player_obj.get_current_space_token_q()
                current_token_space_list.append(player_obj.get_space_name(space))

        return current_token_space_list


# tests
def main():
    # test case 0 -- output: [5, 16, H, H]
    players = ['A', 'D']
    turns = [('A', 6), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('D', 6), ('D', 1), ('D', 6), ('D', 1), ('D', 6),
             ('D', 6), ('D', 5), ('D', 5), ('D', 5), ('D', 2), ('A', 6)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_D = game.get_player_by_position('D')
    print(game.get_player_by_position('X'))  # should return "Player not found!"
    print(player_D.get_space_name(50))

    # test case 1 -- output: [1, 'H', 16, 'H', 31, 'H', 51, 'H']
    players = ['A', 'B', 'C', 'D']
    turns = [('A', 6), ('A', 1), ('B', 6), ('B', 2), ('C', 6), ('C', 3), ('D', 6), ('D', 4), ('D', 5)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_C = game.get_player_by_position('C')
    print(player_C.get_space_name(50))

    # test case 2 -- output: ['H', 'H', 'B6', 'H']
    players = ['A', 'B']
    turns = [('B', 6), ('B', 4), ('B', 5), ('B', 4), ('B', 4), ('B', 3), ('B', 4), ('B', 5), ('B', 4), ('B', 4),
             ('B', 5), ('B', 4), ('B', 1), ('B',
                                            4), ('B', 5), ('B', 5), ('B', 5)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(23))

    # test case 3 -- output: [28, 28, 'H', 'H']
    players = ['A', 'B']
    turns = [('A', 6), ('A', 3), ('A', 6), ('A', 3), ('A', 6), ('A', 5), ('A', 4), ('A', 6), ('A', 4)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(50))

    # test case 4 -- output: [33, 'H', 32, 'H']
    players = ['A', 'C']
    turns = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
             ('A', 6), ('A', 6), ('A', 4), ('A',
                                            6), ('A', 6), ('C', 6), ('C', 1), ('C', 3)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_C = game.get_player_by_position('C')
    print(player_C.get_space_name(51))

    # test case 5 -- output: ['E', 'E', 'R', 'H']
    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
             ('A', 6), ('A', 4), ('A', 6), ('A',
                                            4), ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('A', 4), ('A', 6),
             ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 6), ('B', 6), ('A', 6)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_A.get_space_name(49))

    # test case 6 -- output: [3, 'H', 17, 'H']

    players = ['A', 'B']
    turns = [('A', 6), ('A', 2), ('A', 2), ('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('B', 6), ('B', 3),
             ('A', 6), ('A', 3)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(55))

    # test case 7 -- output: ['A1', 'R', 'H', 'H']
    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
             ('A', 3), ('A', 5), ('A', 3), ('A',
                                            6)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(55))

    # test case 8 -- output: ['E', 13, 17, 'H']
    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
             ('A', 3), ('A', 5), ('A', 5), ('A',
                                            6), ('A', 5), ('A', 5), ('A', 3), ('B', 6), ('B', 3), ('A', 4)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(55))

    # test case 9 -- output: [16, 10, 'H', 'H']
    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 6), ('A', 5), ('A', 3), ('B', 6), ('B', 2), ('A', 2),
             ('A', 4)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(5))


if __name__ == '__main__':
    main()
