import os
from Crypto.Cipher import AES

class AESCipherECB:
    def __init__(self, key):
        # AES-128을 위해 16바이트 길이의 고정 키 설정
        self.key = key.encode('utf-8')

    # 파일 복호화
    def decrypt_file(self, encrypted_file_path, output_file_path):
        with open(encrypted_file_path, "rb") as f:
            encrypted_data = f.read()
        
        # AES-128/ECB 복호화 설정
        cipher = AES.new(self.key, AES.MODE_ECB)
        
        # 복호화 및 패딩 제거
        decrypted_data = self.unpad(cipher.decrypt(encrypted_data))
        
        # 복호화된 데이터 저장
        with open(output_file_path, "wb") as f:
            f.write(decrypted_data)
        print(f"복호화 완료: '{encrypted_file_path}' → '{output_file_path}'")

    # 패딩 제거 함수
    def unpad(self, s):
        return s[:-s[-1]]  # PKCS5/7 패딩 제거

# 모든 .dex 파일 복호화 수행
def decrypt_all_dex_files(directory, key):
    aes = AESCipherECB(key)
    for filename in os.listdir(directory):
        if filename.endswith(".dex"):
            encrypted_file_path = os.path.join(directory, filename)
            output_file_path = os.path.join(directory, f"decrypted_{filename}")
            aes.decrypt_file(encrypted_file_path, output_file_path)

# 고정된 AES-128/ECB 키 설정
key = "dbcdcfghijklmaop"  # 16바이트 키

# 현재 디렉토리에서 모든 .dex 파일 복호화
decrypt_all_dex_files(os.getcwd(), key)
