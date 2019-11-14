import hashlib

def hash(x):
  y = hashlib.md5(x.encode()).hexdigest()
  y = int(y, 16)
  return y

def rv(client, servers: []):
    max_hash = hash(client + servers[0])
    max_hash_serv = servers[0]
    for i in range(len(servers)):
        if hash(client + servers[i]) > max_hash:
            max_hash = hash(client + servers[i])
            max_hash_serv = servers[i]
    return max_hash_serv


client = input()
servers = input().split()
print(rv(client, servers))
