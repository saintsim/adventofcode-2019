#!/usr/bin/env python3

from src.day7 import part1
from src.day7 import amplifier_controller as amp


def amplification(input):
    range_from = 5
    range_to = 9+1
    phase_settings = part1.get_phase_setting_combinations(range_from, range_to)  # range needs +1
    max_result = 0
    for setting in phase_settings:
        print('Phase: ' + str(setting))
        user_input = 0
        # amp_name, input, initial_inputs
        ampA = amp.AmplifierController('ampA', list(input), [setting[0], user_input])
        ampB = amp.AmplifierController('ampB', list(input), [setting[1]])
        ampC = amp.AmplifierController('ampC', list(input), [setting[2]])
        ampD = amp.AmplifierController('ampD', list(input), [setting[3]])
        ampE = amp.AmplifierController('ampE', list(input), [setting[4]])

        output_to_give_to_next = []
        while True:
            finished = True
            for amp_instance in [ampA, ampB, ampC, ampD, ampE]:
                if len(output_to_give_to_next):
                    amp_instance.add_inputs(list(output_to_give_to_next))
                    output_to_give_to_next = []
                amp_instance.start()
                if len(amp_instance.outputs):
                    output_to_give_to_next = list(amp_instance.outputs)
                    amp_instance.outputs = []
            for amp_instance in [ampA, ampB, ampC, ampD, ampE]:
                # print(amp_instance.amp_name + ' -> state: ' + amp_instance.state)
                if amp_instance.state != 'finished':
                    finished = False
            # print('===')
            if finished is True:
                result = output_to_give_to_next[-1]
                break

        if result > max_result:
            print('Phase: ' + str(setting) + ' , gives: ' + str(result))
            max_result = result
    return max_result


if __name__ == '__main__':
    with open('input', 'r') as file:
        input = file.readlines()[0]
        print('Result: ' + str(amplification(list(map(int, input.split(","))))))
