q = int(input())                      # Quantidade de frascos, 1 <= q <= 100
T = float(input())                    # Taxa de vibranium, 0.01 <= T <= 1.00
C = int(input())                      # Constante do solvente, 0 <= C <= 1000
n = int(input())                      # Constante da PA, 1 <= n <= 100

V_p = 0
for i in range(1, q + 1):   
    V_i = T * i + T * C               # Vibranium no frasco i
    V_p += V_i                        # Soma parcial de Vibranium
    print(f"{i} {V_i:.2f} {V_p:.2f}")
print(f"{V_p:.2f}")


PA_n = 0
m = 0
while PA_n <= (V_p - n):              # PA_n não pode ultrapassar V_p
    m += 1
    PA_n += n
    print(PA_n)
print(m)
print("BATERIA DE TESTES TERMINADA")
