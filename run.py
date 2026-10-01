from datetime import datetime
from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository
from configs.start_form import start_form


data_atual = datetime.now()
data_formatada = data_atual.strftime("%d-%m-%Y")

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)
hash_items = redis_conn.hgetall(data_formatada)
 
python_dict = {}
for key, value in hash_items.items():
    python_dict[key.decode('utf-8')] = value.decode('utf-8')

start_form.load_info(python_dict)

value = start_form.get_info('Uva')
print(value)


#redis_repository.insert_hash_ex(data_formatada, "banana", 3.12, 40)    
#redis_repository.insert_hash(data_formatada, "banana", 3.12 )    
#redis_repository.insert_hash(data_formatada, "Morango", 4.12)    
#redis_repository.insert_hash(data_formatada, "Uva", 12.12)