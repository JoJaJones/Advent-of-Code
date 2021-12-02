RELATIVE = "2"
POSITION = "0"
IMMEDIATE = "1"

class IntCode:
    def __init__(self, data, input_val=None, debug=False):
        self.func_dict = {1: self.add, 2: self.mult, 3: self.get_input, 4: self.output,
                          5: self.jump_true, 6: self.jump_false, 7: self.less_than, 8: self.equals,
                          9: self.adjust_rel_base}
        self.memory = data
        self.active_idx = 0
        self.current_opcode = self.memory[self.active_idx]
        self.input_val = []
        if input_val is not None:
            self.input_val.append(input_val)
        elif type(input_val) == int:
            input_val = [input_val]


        self.output_val = None
        self.debug = debug
        self.relative_base = 0

    def get_idx(self, idx, position_mode = "0"):
        if position_mode == POSITION:
            return self.memory[idx]
        elif position_mode == IMMEDIATE:
            return idx
        elif position_mode == RELATIVE:
            return self.relative_base + self.memory[idx]

    def add(self):
        idx_one, idx_two, dest = self.load_indices(3)
        try:
            val_one = self.memory[idx_one]
            val_two = self.memory[idx_two]
        except:
            print(idx_one, len(self.memory))
            exit(1)

        self.memory[dest] = val_two + val_one
        self.active_idx += 4

    def mult(self):
        idx_one, idx_two, dest = self.load_indices(3)

        val_one = self.memory[idx_one]
        val_two = self.memory[idx_two]

        self.memory[dest] = val_one * val_two
        self.active_idx += 4

    def get_input(self):
        dest = self.load_indices(1)[0]
        if self.input_val is None or len(self.input_val) == 0:
            self.input_val = [{1:-2, 2:0, 3:1}[int(input("input: "))]]

        self.memory[dest] = self.input_val.pop(0)
        self.active_idx += 2

    def output(self):
        dest = self.load_indices(1)[0]

        self.active_idx += 2

        return self.memory[dest]

    def jump_true(self):
        bool_idx, dest = self.load_indices(2)
        if self.memory[bool_idx] != 0:
            self.active_idx = self.memory[dest]
        else:
            self.active_idx += 3

    def jump_false(self):
        bool_idx, dest = self.load_indices(2)

        if self.memory[bool_idx] == 0:
            self.active_idx = self.memory[dest]
        else:
            self.active_idx += 3

    def less_than(self):
        idx_one, idx_two, dest = self.load_indices(3)

        val_one = self.memory[idx_one]
        val_two = self.memory[idx_two]

        self.memory[dest] = 1 if val_one < val_two else 0
        self.active_idx += 4

    def equals(self):
        idx_one, idx_two, dest = self.load_indices(3)

        val_one = self.memory[idx_one]
        val_two = self.memory[idx_two]

        self.memory[dest] = 1 if val_one == val_two else 0
        self.active_idx += 4

    def adjust_rel_base(self):
        idx_one = self.load_indices(1)[0]
        val_one = self.memory[idx_one]

        self.relative_base += val_one
        self.active_idx += 2

    def load_parameter_modes(self, length=5):
        opcode = str(self.current_opcode)
        while len(opcode) < length:
            opcode = "0" + opcode
        opcode = opcode[:-2]
        modes = []
        while len(opcode) > 0:
            modes.append(opcode[-1])
            opcode = opcode[:-1]

        return modes

    def load_indices(self, num_to_load):
        modes = self.load_parameter_modes(num_to_load + 2)
        indices = []
        shift = 1
        while len(modes) > 0:
            indices.append(self.get_idx(self.active_idx + shift, modes.pop(0)))
            shift += 1

        self.expand_memory(max(indices))

        return indices

    def expand_memory(self, idx):
        while len(self.memory) < idx + 1:
            self.memory.append(0)

    def run(self, value=None):
        if value is not None:
            self.input_val.append(value)

        if self.debug:
            print(str(self.current_opcode)[-2:], self.active_idx)

        while self.current_opcode != 99:
            currop = int(str(self.current_opcode)[-2:])
            # print(currop)
            result = self.func_dict[currop]()
            self.current_opcode = self.memory[self.active_idx]
            if result is not None:
                return result
            if self.debug:
                print(str(self.current_opcode)[-2:], self.active_idx)

        return False

    def add_input(self, value):
        self.input_val.append(value)

    def run_program(self):
        res = self.run()
        while res:
            print(res)
            res = self.run()

    def get_pos_value(self, idx):
        return self.memory[idx]
