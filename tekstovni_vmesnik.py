from model import *

def input_promt_fixed(question, input_text, fail_text, choice_list):
    """Poenostva nadzor nad vhodnimi podatki iz konzole. Vprašanje / pričakovani odgovori / opomba, če vnos ni ustrezen / seznam ustreznih vnosov """
    while True:
        print(question)
        choice = input(f"{input_text}: ")
        if choice in choice_list:
            return choice
        else:
            print(fail_text)

def show_field_vanila(cell):
    print(" ------- ")
    print(f"| {cell.cells[7]} {cell.cells[8]} {cell.cells[9]} |")
    print(f"| {cell.cells[4]} {cell.cells[5]} {cell.cells[6]} |")
    print(f"| {cell.cells[1]} {cell.cells[2]} {cell.cells[3]} |")
    print(" ------- ")

def show_field_ultimate(cells_list):
    print(" " + "-" * 23 + " ")
    print(f"| {cells_list[7].cells[7]} {cells_list[7].cells[8]} {cells_list[7].cells[9]} | {cells_list[8].cells[7]} {cells_list[8].cells[8]} {cells_list[8].cells[9]} | {cells_list[9].cells[7]} {cells_list[9].cells[8]} {cells_list[9].cells[9]} |")
    print(f"| {cells_list[7].cells[4]} {cells_list[7].cells[5]} {cells_list[7].cells[6]} | {cells_list[8].cells[4]} {cells_list[8].cells[5]} {cells_list[8].cells[6]} | {cells_list[9].cells[4]} {cells_list[9].cells[5]} {cells_list[9].cells[6]} |")
    print(f"| {cells_list[7].cells[1]} {cells_list[7].cells[2]} {cells_list[7].cells[3]} | {cells_list[8].cells[1]} {cells_list[8].cells[2]} {cells_list[8].cells[3]} | {cells_list[9].cells[1]} {cells_list[9].cells[2]} {cells_list[9].cells[3]} |")
    print(" " + "-" * 23 + " ")
    print(f"| {cells_list[4].cells[7]} {cells_list[4].cells[8]} {cells_list[4].cells[9]} | {cells_list[5].cells[7]} {cells_list[5].cells[8]} {cells_list[5].cells[9]} | {cells_list[6].cells[7]} {cells_list[6].cells[8]} {cells_list[6].cells[9]} |")
    print(f"| {cells_list[4].cells[4]} {cells_list[4].cells[5]} {cells_list[4].cells[6]} | {cells_list[5].cells[4]} {cells_list[5].cells[5]} {cells_list[5].cells[6]} | {cells_list[6].cells[4]} {cells_list[6].cells[5]} {cells_list[6].cells[6]} |")
    print(f"| {cells_list[4].cells[1]} {cells_list[4].cells[2]} {cells_list[4].cells[3]} | {cells_list[5].cells[1]} {cells_list[5].cells[2]} {cells_list[5].cells[3]} | {cells_list[6].cells[1]} {cells_list[6].cells[2]} {cells_list[6].cells[3]} |")
    print(" " + "-" * 23 + " ")
    print(f"| {cells_list[1].cells[7]} {cells_list[1].cells[8]} {cells_list[1].cells[9]} | {cells_list[2].cells[7]} {cells_list[2].cells[8]} {cells_list[2].cells[9]} | {cells_list[3].cells[7]} {cells_list[3].cells[8]} {cells_list[3].cells[9]} |")
    print(f"| {cells_list[1].cells[4]} {cells_list[1].cells[5]} {cells_list[1].cells[6]} | {cells_list[2].cells[4]} {cells_list[2].cells[5]} {cells_list[2].cells[6]} | {cells_list[3].cells[4]} {cells_list[3].cells[5]} {cells_list[3].cells[6]} |")
    print(f"| {cells_list[1].cells[1]} {cells_list[1].cells[2]} {cells_list[1].cells[3]} | {cells_list[2].cells[1]} {cells_list[2].cells[2]} {cells_list[2].cells[3]} | {cells_list[3].cells[1]} {cells_list[3].cells[2]} {cells_list[3].cells[3]} |")
    print(" " + "-" * 23 + " ")

class vanila_2:
    def __init__(self):
        self.game = Cell()
        self.num_turns = 0
        self.turn = input_promt_fixed("Bi prvi igralec imel križce ali krožce?", "X/O", "Žal je bil vnos neustrezen.", ["X", "O"])
        self.bad_choice = False
    
    def check_bad_move(self):
        if self.bad_choice:
            print("To polje je že zasedeno.")
            self.bad_choice = False
    
    def make_move(self):
        inp = int(input_promt_fixed(f"Igralec {self.turn} je na potezi.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))
        if self.game.mark_field(inp, self.turn):
            self.turn = self.game.sign_switch(self.turn)
            self.num_turns += 1
        else:
            self.bad_choice = True

    def main_game(self):
        print("Polja so številčena kot številčna tipkovnica.")
        while not self.game.check_win() and self.num_turns < 9:
            show_field_vanila(self.game)
            self.check_bad_move()
            self.make_move()
            
    def end_game(self):
        show_field_vanila(self.game)
        if self.game.check_win():
            print(f"Čestitke {self.game.sign_switch(self.turn)}!")
        else:
            print("Igra je neodločena.")
        input("Ko željite zaključiti, pritisnite ENTER.")

def start_vanila_2():
    game = vanila_2()
    game.main_game()
    game.end_game()

class vanila_1:
    def __init__(self):
        self.game = Cell()
        self.num_turns = 0
        self.player_mark = input_promt_fixed("Želite imeti križce ali krožce?", "X/O", "Žal je bil vnos neustrezen.", ["X", "O"])
        self.player_turn = "y" == input_promt_fixed("Želite biti prvi?", "y/n", "Žal je bil vnos neustrezen.", ["y", "n"])
        self.current_mark = self.player_mark if self.player_turn else self.game.sign_switch(self.player_mark)
        self.bad_choice = False
        self.dif = input_promt_fixed("Izberite težavnostno stopnjo. Večje kot je število, težje bo.", "(1 - 4)", "Žal je bil vnos neustrezen.", ["1", "2", "3", "4"])
        self.bot = Bot(self.player_mark, not self.player_turn)
        if self.dif == "1":
            self.bot_generator = self.bot.vanila_dif_1(self.game)
        elif self.dif == "2":
            self.bot_generator = self.bot.vanila_dif_2(self.game)
        elif self.dif == "3":
            self.bot_generator = self.bot.vanila_dif_3(self.game)
        elif self.dif == "4":
            self.bot_generator = self.bot.vanila_dif_4(self.game)
    
    def check_bad_move(self):
        if self.bad_choice:
            print("To polje je že zasedeno.")
            self.bad_choice = False
    
    def make_move(self):
        if self.player_turn:
            show_field_vanila(self.game)
            inp = int(input_promt_fixed(f"Ste na potezi.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))
        else:
            inp = next(self.bot_generator)

        if self.game.mark_field(inp, self.current_mark):
            self.player_turn = not self.player_turn
            self.current_mark = self.game.sign_switch(self.current_mark)
            self.num_turns += 1
        else:
            self.bad_choice = True

    def main_game(self):
        print("Polja so številčena kot številčna tipkovnica.")
        while not self.game.check_win() and self.num_turns < 9:
            self.check_bad_move()
            self.make_move()
    
    def end_game(self):
        show_field_vanila(self.game)
        if self.game.check_win() and not self.player_turn:
            print("Čestitke!")
        elif self.game.check_win() and self.player_turn:
            print("Žal ste izgubili. Več sreče prihodnjič.")
        else:
            print("Igra je neodločena.")
        input("Ko željite zaključiti, pritisnite ENTER.")

def start_vanila_1():
    game = vanila_1()
    game.main_game()
    game.end_game()

class ultimate_2:
    def __init__(self):
        self.master_cell = Cell()
        self.cell1 = Cell()
        self.cell2 = Cell()
        self.cell3 = Cell()
        self.cell4 = Cell()
        self.cell5 = Cell()
        self.cell6 = Cell()
        self.cell7 = Cell()
        self.cell8 = Cell()
        self.cell9 = Cell()
        self.game = ["&", self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8, self.cell9]
        self.turn = input_promt_fixed("Bi prvi igralec imel križce ali krožce?", "X/O", "Žal je bil vnos neustrezen.", ["X", "O"])
        self.num_master_turns = 0
        self.bad_choice = False

    def pre_game(self):
        print("Polja so številčena kot številčna tipkovnica.")
        show_field_ultimate(self.game)
        self.inp_cell = int(input_promt_fixed(f"Za začetek sme {self.turn} izbrati poljubno celico.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))
        self.inp_space = int(input_promt_fixed(f"{self.turn} naj izbere še polje v celici {self.inp_cell}.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))
        self.game[self.inp_cell].mark_field(self.inp_space, self.turn)
        self.inp_cell = self.inp_space
        self.turn = self.master_cell.sign_switch(self.turn)

    def check_bad_move(self):
        if self.bad_choice:
            print("To polje je že zasedeno.")
            self.bad_choice = False

    def move_in_small_cell(self, current_cell):
        self.inp_space = int(input_promt_fixed(f"{self.turn} naj izbere polje v celici {self.inp_cell}.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))
        if current_cell.mark_field(self.inp_space, self.turn):
            if current_cell.check_win():
                self.master_cell.mark_field(self.inp_cell, self.turn)
                self.num_master_turns += 1
                current_cell.print_sign_graphic(self.turn)
            elif current_cell.check_draw():
                self.master_cell.mark_field(self.inp_cell, "+")
                self.num_master_turns += 1
                current_cell.Draw_graphic()
            self.inp_cell = self.inp_space
            self.turn = self.master_cell.sign_switch(self.turn)
        else:
            self.bad_choice = True
    
    def move_in_big_cell(self):
        print(f"Ta cell je že zaključeno. {self.turn} lahko gre kamorkoli.")
        self.inp_cell = int(input_promt_fixed(f"{self.turn} naj izbere poljubno celico.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))

    def make_move(self):
        current_cell = self.game[self.inp_cell]
        if self.master_cell.cells[self.inp_cell] == ".":
            self.move_in_small_cell(current_cell)
        else:
            self.move_in_big_cell()
    
    def main_game(self):
        while not self.master_cell.check_win() and self.num_master_turns < 9:
            show_field_ultimate(self.game)
            self.check_bad_move()
            self.make_move()
    
    def end_game(self):
        show_field_ultimate(self.game)
        if self.master_cell.check_win():
            print(f"Čestitke {self.master_cell.sign_switch(self.turn)}!")
        else:
            print("Igra je neodločena.")
        input("Ko željite zaključiti, pritisnite ENTER.")

def start_ultimate_2():
    game = ultimate_2()
    game.pre_game()
    game.main_game()
    game.end_game()

class ultimate_1:
    def __init__(self):
        self.master_cell = Cell()
        self.cell1 = Cell()
        self.cell2 = Cell()
        self.cell3 = Cell()
        self.cell4 = Cell()
        self.cell5 = Cell()
        self.cell6 = Cell()
        self.cell7 = Cell()
        self.cell8 = Cell()
        self.cell9 = Cell()
        self.game = ["&", self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8, self.cell9]
        self.num_master_turns = 0
        self.player_mark = input_promt_fixed("Želite imeti križce ali krožce?", "X/O", "Žal je bil vnos neustrezen.", ["X", "O"])
        self.player_turn = "y" == input_promt_fixed("Želite biti prvi?", "y/n", "Žal je bil vnos neustrezen.", ["y", "n"])
        self.master_bot = Bot(self.player_mark, not self.player_turn)
        self.bad_choice = False
        self.current_mark = self.player_mark if self.player_turn else self.master_cell.sign_switch(self.player_mark)

    def pre_game(self):
        print("Celice in polja so številčena kot številčna tipkovnica.")
        if self.player_turn:
            show_field_ultimate(self.game)
            self.inp_cell = int(input_promt_fixed(f"Za začetek smete {self.player_mark} izbrati poljubno celico.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))
            self.inp_space = int(input_promt_fixed(f"Sedaj {self.player_mark} izberite še polje v celici {self.inp_cell}.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))
        else:
            self.inp_cell = self.master_cell.random_free()
            self.inp_space = self.game[self.inp_cell].random_free()
        self.game[self.inp_cell].mark_field(self.inp_space, self.current_mark)
        self.last_inp_cell = self.inp_cell
        self.inp_cell = self.inp_space
        self.current_mark = self.master_cell.sign_switch(self.current_mark)
        self.player_turn = not self.player_turn
    
    def show_robot_info_and_field(self):
        if self.player_turn:
            print(f"Računalnik je v celici {self.last_inp_cell} izbral polje {self.inp_cell}.")
            show_field_ultimate(self.game)

    def check_bad_move(self):
        if self.bad_choice:
            if self.player_turn:
                print("To polje je že zasedeno.")
            self.bad_choice = False

    def move_in_small_cell(self, current_cell):
        if self.player_turn:
            self.inp_space = int(input_promt_fixed(f"{self.player_mark} izberite polje v celici {self.inp_cell}.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))
        else:
            self.inp_space = self.master_bot.ultimate_incell_move(self.game, self.inp_cell)
        if current_cell.mark_field(self.inp_space, self.current_mark):
            if current_cell.check_win():
                self.master_cell.mark_field(self.inp_cell, self.current_mark)
                self.num_master_turns += 1
                current_cell.print_sign_graphic(self.current_mark)
            elif current_cell.check_draw():
                self.master_cell.mark_field(self.inp_cell, "+")
                self.num_master_turns += 1
                current_cell.Draw_graphic()
            self.last_inp_cell = self.inp_cell
            self.inp_cell = self.inp_space
            self.current_mark = self.master_cell.sign_switch(self.current_mark)
            self.player_turn = not self.player_turn
        else:
            self.bad_choice = True

    def move_in_big_cell(self):
        if self.player_turn:
            print("Lahko greste kamorkoli.")
            self.inp_cell = int(input_promt_fixed(f"{self.player_mark} izberite poljubno celico.", "(1 - 9)", "Žal je bil vnos neustrezen.", [str(i) for i in range(1, 10)]))
        else:
            self.inp_cell = self.master_cell.random_free()

    def make_move(self):
        current_cell = self.game[self.inp_cell]
        if self.master_cell.cells[self.inp_cell] == ".":
            self.move_in_small_cell(current_cell)
        else:
            self.move_in_big_cell()

    def main_game(self):
        while not self.master_cell.check_win() and self.num_master_turns < 9:
            self.show_robot_info_and_field()
            self.check_bad_move()
            self.make_move()

    def end_game(self):
        print(f"Računalnik je v celici {self.last_inp_cell} izbral polje {self.inp_cell}.")
        show_field_ultimate(self.game)
        if self.master_cell.check_win() and not self.player_turn:
            print("Čestitke!")
        elif self.master_cell.check_win() and self.player_turn:
            print("Žal ste izgubili. Več sreče prihodnjič.")
        else:
            print("Igra je neodločena.")
        input("Ko željite zaključiti, pritisnite ENTER.")

def start_ultimate_1():
    game = ultimate_1()
    game.pre_game()
    game.main_game()
    game.end_game()