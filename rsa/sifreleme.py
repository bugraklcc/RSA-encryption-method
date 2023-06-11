import timeit


def rsa_encryption(M, e, n):
  return pow(M, e, n)


def rsa_decryption(C, d, n):
  return pow(C, d, n)


def private_key_calculation(p, q, e):
  return pow(e, -1, (p - 1) * (q - 1))


# Verilen parametreler
p = 557
q = 569
n = p * q
e = 186737
d = private_key_calculation(p, q, e)
M = 9999
C = rsa_encryption(M, e, n)

# Gizli anahtar hesaplama süresi ölçümü
private_key_calculation_time = timeit.timeit(
  lambda: private_key_calculation(p, q, e), number=1000000)

# Şifreleme süresi ölçümü
encryption_time = timeit.timeit(lambda: rsa_encryption(M, e, n),
                                number=1000000)

# Deşifreleme süresi ölçümü
decryption_time = timeit.timeit(lambda: rsa_decryption(C, d, n),
                                number=1000000)

if private_key_calculation_time < 1:
  private_key_calculation_seconds = round(private_key_calculation_time, 6)
else:
  private_key_calculation_minutes = int(private_key_calculation_time // 60)
  private_key_calculation_seconds = round(private_key_calculation_time % 60)

if encryption_time < 1:
  encryption_seconds = round(encryption_time, 6)
else:
  encryption_minutes = int(encryption_time // 60)
  encryption_seconds = round(encryption_time % 60)

if decryption_time < 1:
  decryption_seconds = round(decryption_time, 6)
else:
  decryption_minutes = int(decryption_time // 60)
  decryption_seconds = round(decryption_time % 60)

print("Gizli Anahtar Hesaplama Süresi: {} dakika {:02d} saniye".format(
  private_key_calculation_minutes, int(private_key_calculation_seconds)))
print("Şifreleme Süresi: {} dakika {:02d} saniye".format(
  encryption_minutes, int(encryption_seconds)))
print("Deşifreleme Süresi: {} dakika {:02d} saniye".format(
  decryption_minutes, int(decryption_seconds)))