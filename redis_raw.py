"""Comandos Redis básico"""
import redis

def redis_conn():
    try:    
        r_conn = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
        print("Cliente criado")
        print("Testando conexão...")
        print(r_conn.ping())
        return r_conn
    except:
        print("Erro ao conectar")

def redis_set(chave_1, valor_1):
    r_conn = redis_conn()
    if r_conn.get(chave_1):
        print("Esse chave já existe...")
    else:
        print("Gravando...")
        r_conn.set(chave_1, valor_1)

def redis_hset(hash_name, campo, valor):
    r_conn = redis_conn()
    r_conn.hset(hash_name, campo, valor);

redis_hset("meuHash", "nome", "Pedro")
redis_hset("meuHash", "idade", 30)
redis_hset("meuHash", "cidade", "Fortaleza")
#redis_set("cheve_3", "valor_3")