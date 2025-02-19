from cryptography.fernet import Fernet

class AdvancedEncryptionTool:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        print("[+] Encryption Key Generated. Save this key to decrypt later!")
        print(self.key.decode())

    def encrypt_data(self, data):
        encrypted = self.cipher.encrypt(data.encode())
        print("\n[+] Encrypted Data:")
        print(encrypted.decode())
        return encrypted

    def decrypt_data(self, encrypted_data):
        decrypted = self.cipher.decrypt(encrypted_data).decode()
        print("\n[+] Decrypted Data:")
        print(decrypted)
        return decrypted

if __name__ == "__main__":
    tool = AdvancedEncryptionTool()
    
    data = input("Enter data to encrypt: ")
    encrypted_data = tool.encrypt_data(data)
    
    decrypt_option = input("Do you want to decrypt the data? (yes/no): ")
    if decrypt_option.lower() == "yes":
        tool.decrypt_data(encrypted_data)
