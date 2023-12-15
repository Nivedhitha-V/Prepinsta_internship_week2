positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']
print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
print(positions)

if positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']:
    print("You Win!")

while True:
    print("\n#### Always enter the values less than 7 ####")
    print("Press 'q' to quit")

    pos = input("Enter position of piece: ")

    if pos.lower() == 'q':
        print("You Lose")
        break

    else:
        pos = int(pos)

        if pos < 0 or pos > 6:
            print("Invalid Move")
            continue

        elif positions[pos] == '-':
            print("Invalid Move")
            continue

    pos2 = 0

    if positions[pos] == 'G':
        if pos + 1 <= 6 and positions[pos + 1] == '-':
            pos2 = pos + 1
        elif pos + 2 <= 6 and positions[pos + 2] == '-' and positions[pos + 1] == 'B':
            pos2 = pos + 2
        else:
            print("Invalid Move")
            continue

    elif positions[pos] == 'B':
        if pos - 1 >= 0 and positions[pos - 1] == '-':
            pos2 = pos - 1
        elif pos - 2 >= 0 and positions[pos - 2] == '-' and positions[pos - 1] == 'G':
            pos2 = pos - 2
        else:
            print("Invalid Move")
            continue

    positions[pos], positions[pos2] = positions[pos2], positions[pos]

    print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
    print(positions)

    if positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']:
        print("You Win!")
        break

