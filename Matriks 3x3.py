matriks_a = [[5, 7, 2],[8, 1, 9],[4, 6, 3]]
matriks_b = [[2, 4, 9],[3, 6, 7],[5, 8, 1]]
print("Matriks A:")
for baris in matriks_a:
    print(baris)
print("\nmatriks B:")
for baris in matriks_b:
    print(baris)
hasil_perkalian = [[matriks_a[i][j] * matriks_b[i][j] for j in range(3)] for i in range(3)]
print("\nhasil perkalian matriks a dan matriks b:")
for baris in hasil_perkalian:
    print(baris)