import numpy as np

# Define the modulo values
mod_2 = 2
mod_7 = 7
mod_31 = 31

# Create the generating matrix G
G = np.zeros((19, 10), dtype=int)

# Identity matrix for data bits
G[:10, :10] = np.eye(10, dtype=int)

# Calculate parity bit for modulo 2
G[10, :10] = np.ones(10, dtype=int) % mod_2

# Calculate bits for modulo 7
G[11, :10] = np.array([i % mod_7 for i in range(1, 11)])

# Calculate bits for modulo 31
G[14, :10] = np.array([i % mod_31 for i in range(1, 11)])

# Calculate parity bits for modulo 7 and modulo 31
for i in range(3):
    G[11 + i, 10:14] = [int(x) for x in list(format((mod_7 - sum(G[11:14, i]) % mod_7) % mod_7, '03b'))]
    G[14 + i, 14:] = [int(x) for x in list(format((mod_31 - sum(G[14:18, i]) % mod_31) % mod_31, '05b'))]

print("Generating Matrix G:")
print(G)