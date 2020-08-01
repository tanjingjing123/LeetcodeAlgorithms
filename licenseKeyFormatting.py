def licenseKeyFormat(S, K):
    arr = []
    S = S.replace('-', '').upper()
    rem = len(S) % K
    if rem != 0:
        arr.append(S[:rem])
    for i in range(rem, len(S), K):
        arr.append(S[i:i+K])
    return '-'.join(arr)

S = "5F3Z-2e-9-w"
K = 4
print(licenseKeyFormat(S, K))
