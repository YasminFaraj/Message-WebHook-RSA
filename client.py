from rsa import gerar_chaves, rsa_encrypt, rsa_decrypt
import json

# gera chaves do cliente
e_cli, d_cli, n_cli = gerar_chaves()

# salva chave pública do cliente em arquivo
with open("chave_cliente.txt", "w") as f:
    json.dump({"e": e_cli, "n": n_cli}, f)

# le chave pública do servidor
with open("chave_servidor.txt", "r") as f:
    dados = json.load(f)
    e_srv = dados["e"]
    n_srv = dados["n"]

mensagem = input("[Cliente] Digite sua mensagem: ")
cifrada = rsa_encrypt(mensagem, e_srv, n_srv)
print("[Cliente] Mensagem criptografada:", cifrada)

# salva mensagem criptografada em arquivo
with open("mensagem_para_servidor.txt", "w") as f:
    json.dump({"mensagem": cifrada}, f)

# aguarda resposta do servidor
input("[Cliente] Pressione Enter quando a resposta estiver pronta...")

# le resposta criptografada
with open("resposta_do_servidor.txt", "r") as f:
    dados = json.load(f)
    resposta_cifrada = dados["mensagem"]
    resposta = rsa_decrypt(resposta_cifrada, d_cli, n_cli)
    print("[Cliente] Resposta decriptada:", resposta)
