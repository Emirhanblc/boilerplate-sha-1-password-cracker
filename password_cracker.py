import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Parolaların bulunduğu dosyayı oku
    with open("top-10000-passwords.txt", "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f]

    # Eğer tuzlama (salting) isteniyorsa:
    if use_salts:
        with open("known-salts.txt", "r", encoding="utf-8") as f:
            salts = [line.strip() for line in f]
            
        for password in passwords:
            for salt in salts:
                # 1. Tuzu başa ekleyerek dene (salt + password)
                prepended = salt + password
                if hashlib.sha1(prepended.encode()).hexdigest() == hash:
                    return password
                
                # 2. Tuzu sona ekleyerek dene (password + salt)
                appended = password + salt
                if hashlib.sha1(appended.encode()).hexdigest() == hash:
                    return password

    # Tuzlama istenmiyorsa sadece parolaları dene:
    else:
        for password in passwords:
            if hashlib.sha1(password.encode()).hexdigest() == hash:
                return password

    # Hiçbir eşleşme bulunamazsa:
    return "PASSWORD NOT IN DATABASE"