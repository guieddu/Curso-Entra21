# bits
# Bytes
# KB
# MB

gb = int(input("Digite o valor em GB:"))

bits = gb * (1024 ** 3) * 8
bytes = gb * (1024 ** 3)
kb = gb * (1024 **2)
mb = gb * (1024)

print(f"GB para Bits: {bits}")
print(f"GB para Bytes: {bytes}")
print(f"GB para Kb: {kb}")
print(f"GB para Mb: {mb}")