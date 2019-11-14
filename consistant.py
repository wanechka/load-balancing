import hashlib #for md5 using

def hash(x): 
  y = hashlib.md5(x.encode()).hexdigest()
  y = int(y, 16)
  return y

def ch(client, servers:[]):
  client_id = hash(client)
  num = len(servers)
  serv_hashes = []
  for i in range(num):
    g = []
    g.append(servers[i])
    g.append(hash(servers[i]))
    serv_hashes.append(g)
  serv_hashes = sorted(serv_hashes, key = lambda x: -x[1], reverse = True)
  if client_id <= serv_hashes[0][1] or client_id > serv_hashes[num - 1][1]:
    return serv_hashes[0][0]
  for j in range(num - 2):
    if client_id == serv_hashes[j][1]:
      return serv_hashes[j][0]
    if client_id > serv_hashes[j][1]:
      if client_id <= serv_hashes[j + 1][1]:
        return serv_hashes[j + 1][0]

client = input()
servers = input().split()
print(ch(client, servers))
