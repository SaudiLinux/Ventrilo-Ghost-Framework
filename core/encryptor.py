from cryptography.fernet import Fernet
import os

class GhostEncryptor:
    def __init__(self, key_path="ghost.key"):
        self.key_path = key_path
        self.key = self._get_key()
        self.cipher = Fernet(self.key)

    def _get_key(self):
        if os.path.exists(self.key_path):
            with open(self.key_path, "rb") as f: return f.read()
        key = Fernet.generate_key()
        with open(self.key_path, "wb") as f: f.write(key)
        return key

    def encrypt_data(self, data):
        return self.cipher.encrypt(data.encode()).decode()

    def encrypt_file(self, file_path):
        with open(file_path, "rb") as f:
            enc_data = self.cipher.encrypt(f.read())
        with open(file_path + ".ghost", "wb") as f: f.write(enc_data)
        os.remove(file_path) # مسح الأثر الجنائي
        print(f"[🛡️] تم التشفير وحذف الأصل: {file_path}")