def print_formatted(number):
    padding = len(bin(number)[2:])
    for i in range(1, number+1):
        decimal = str(i)
        octo = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        padded_d = f"{' '*(padding-len(decimal))}{decimal}"
        padded_o = f"{' '*(padding-len(octo))}{octo}"
        padded_h = f"{' '*(padding-len(hexa))}{hexa}"
        padded_b = f"{' '*(padding-len(binary))}{binary}"
        print(padded_d, padded_o, padded_h, padded_b)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
