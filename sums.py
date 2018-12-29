#!/usr/bin/python3
# coding: utf-8

def find_positions_for_sum(iterable, expected_sum):
    
    iterable.sort()
    size = len(iterable)

    for position_reversed in reversed(range(size)):
        high_number = iterable[position_reversed]

        if high_number > expected_sum:
            continue

        elif high_number == expected_sum:
            return [position_reversed]

        else:
            for position in range(position_reversed):
                
                low_number = iterable[position]
                summed = low_number + high_number
                
                if summed < expected_sum:
                    continue
                elif summed > expected_sum:
                    return None
                else:
                    return [position, position_reversed]


if __name__ == '__main__':
    lista = [4, 1, 3, 10, 5, 7]
    print(lista)
    result = find_positions_for_sum(lista, 8)
    print(lista)
    print("Result:", result)
