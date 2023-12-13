import sys
import subprocess
import hashlib

def calculate_hash(file_path, algorithm):
    hasher = hashlib.new(algorithm)
    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def extract_owner_info(file_path):
    try:
        # Redirect stderr to /dev/null to suppress warnings
        result = subprocess.check_output(["exiftool", "-Creator", "-Software", file_path], stderr=subprocess.DEVNULL)
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return "Owner/Creator information not available"

def main():
    file_path = input("Enter the file path: ")
    md5_hash = calculate_hash(file_path, "md5")
    sha1_hash = calculate_hash(file_path, "sha1")
    sha256_hash = calculate_hash(file_path, "sha256")
    digital_signature = calculate_hash(file_path, "sha256")  # For simplicity, using SHA-256 as digital signature
    owner_info = extract_owner_info(file_path)

    print(f"MD5: {md5_hash}")
    print(f"SHA-1: {sha1_hash}")
    print(f"SHA-256: {sha256_hash}")
    print(f"Digital Signature: {digital_signature}")
    print(f"Owner/Creator: {owner_info}")

if __name__ == "__main__":
    main()
