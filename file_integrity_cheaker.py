import hashlib
import os

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a given file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return None

def save_hash(file_path, hash_file):
    """Save the hash of a file to a hash file."""
    file_hash = calculate_hash(file_path)
    if file_hash:
        with open(hash_file, 'w') as f:
            f.write(file_hash)
        print(f"Hash saved to {hash_file}")
    else:
        print("File not found.")

def verify_integrity(file_path, hash_file):
    """Verify the integrity of a file by comparing its hash with a saved hash."""
    try:
        with open(hash_file, 'r') as f:
            stored_hash = f.read().strip()
    except FileNotFoundError:
        print("Hash file not found.")
        return False
    
    current_hash = calculate_hash(file_path)
    if current_hash == stored_hash:
        print("File integrity verified. No changes detected.")
        return True
    else:
        print("WARNING: File integrity compromised!")
        return False

# Example Usage:
if __name__ == "__main__":
    file_to_check = "example.txt"  # Change this to your file
    hash_storage = "example_hash.txt"
    
    # Save hash
    save_hash(file_to_check, hash_storage)
    
    # Verify integrity
    verify_integrity(file_to_check, hash_storage)
