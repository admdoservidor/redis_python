import os
from dotenv import load_dotenv
import redis

def redis_conn():
    try:    
        return redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    except redis.RedisError as erro:
        print(f"Erro ao acessar chave: {erro}")
        return 0

def is_key_exists(key):
    r_conn = redis_conn()
    try:
        return r_conn.exists(key)
    except redis.RedisError as erro:
        print(f"Erro ao acessar chave: {erro}")
        return 0

def redis_hkey_exists(hash_name, valor):
    r_conn = redis_conn()
    try:
        return r_conn.hexists(hash_name, valor)
    except redis.RedisError as erro:
        print(f"Erro ao acessar chave: {erro}")
        return 0
        
def redis_set(chave, valor):
    r_conn = redis_conn()
    if is_key_exists(chave):
        print("Esse chave já existe...")
    else:
        print("Gravando...")
        r_conn.set(chave, valor)

def redis_get(key):
    r_conn = redis_conn()
    if is_key_exists(key):
        print(f"Chave acessada: {r_conn.get(key)}")
    else:
        print(f"Chave não exite!")

def redis_delete(key):
    r_conn = redis_conn()
    if (is_key_exists(key)):
        r_conn.delete(key)
        print(f"Chave deletada: {key}")
    else:
        print(f"Chave não existe: {key}")

def redis_hset(hash_name, campo, valor):
    r_conn = redis_conn()
    if (is_key_exists(hash_name)):
        r_conn.hset(hash_name, campo, valor)
        print(f"Hash criado: {hash_name}")
    else:
        print(f"Hash já existe: {hash_name}")

def redis_hget(hash_name, campo):
    r_conn = redis_conn()
    if(is_key_exists(hash_name) and redis_hkey_exists(hash_name, campo)):
        print(f"Hash acessada: {hash_name}: {r_conn.hget(hash_name, campo)}")
    else:
        print(f"Hash não exite!")

def redis_hdel(hash_name, key):
    r_conn = redis_conn()
    if (is_key_exists(hash_name)):
        r_conn.delete(hash_name, key)
        print(f"Key deletada: {key}")
    else:
        print(f"Hash ou key não existe: {key}")

    
#redis_set("chave_2", "valor_2")
#redis_get("chave_2")
#redis_delete("chave_2")
redis_hget("meuHash", "nome")
#redis_hget("meuHash", "idade")
#redis_hget("meuHash", "cidade")
#redis_hset("meuHash", "nome", "Pedro")
#redis_hset("meuHash", "idade", 20)
#redis_hset("nossoHash", "cidade", "Fortaleza")
#redis_hdel("nossoHash", "cidade")