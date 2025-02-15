import os
import hashlib

def find_duplicate_files(directory):
    file_hashes = {}
    # Итеративное углубление с использованием стека
    stack = [directory]
    
    while stack:
        current_dir = stack.pop()
        try:
            for entry in os.scandir(current_dir):
                if entry.is_dir():
                    stack.append(entry.path)
                elif entry.is_file():
                    file_hash = hash_file(entry.path)
                    if file_hash in file_hashes:
                        print(f"Найдены дублирующиеся файлы: {entry.path} и {file_hashes[file_hash]}")
                        return
                    file_hashes[file_hash] = entry.path
        except PermissionError:
            # Пропускаем файлы и директории, доступ к которым ограничен
            continue

def hash_file(file_path):
    """Вычисление хеша файла для сравнения содержимого"""
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

if __name__ == "__main__":
    directory = 'C:\\Users\\UnnamedUser\\Documents'
    find_duplicate_files(directory)
