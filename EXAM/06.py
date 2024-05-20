K = int(input())
L = int(input())
M = int(input())
N = int(input())

changes = 0

for i in range(K, 9):
    for j in range(9, L-1, -1):
        for k in range(M, 9):
            for l in range(9, N-1, -1):
                if (i % 2 == 0 and j % 2 != 0) and (k % 2 == 0 and l % 2 != 0) and (i != k or j != l):
                    if changes <= 6:
                        print(f"{i}{j} - {k}{l}")
                        changes += 1
                    else:
                        break
                elif i == k and j == l:
                    print("Cannot change the same player.")

    if changes > 6:
        break
