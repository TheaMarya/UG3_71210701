kal = input("Masukkan kalimat: ")

# Membuat list dari setiap kata dalam kalimat
k_list = kal.split()

# Menghitung jumlah munculannya setiap kata
memunculkan = {}

for k in k_list:
    if k in memunculkan:
        memunculkan[k] += 1
    else:
        memunculkan[k] = 1

# Memunculkan output
print("Jumlah munculnya setiap kata:")

for k, total in memunculkan.items():
    print(f"{k} = {total}")

print(f"Total kata = {len(k_list)}")
print(f"Kata unik = {len(memunculkan)}")