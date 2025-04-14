from cryptography.fernet import Fernet

key = Fernet.generate_key()
cypher = Fernet(key)
wa = 10
phone = cypher.encrypt(str(wa).encode())
print(wa)
print(phone)