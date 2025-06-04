from rsa import gerar_chaves, rsa_encrypt, rsa_decrypt
import json

# gera chave do servidor
e_srv, d_srv, n_srv = gerar_chaves()

# salva chave publica
with open("chave_servidor.txt", "w", encoding="utf-8") as f:
    json.dump({"e": e_srv, "n": n_srv}, f)

input("[Servidor] Aguarde o cliente gerar a chave e pressione Enter...")

# le chave publica do cliente
with open("chave_cliente.txt", "r", encoding="utf-8") as f:
    dados = json.load(f)
    e_cli = dados["e"]
    n_cli = dados["n"]

# le mensagem criptografada
with open("mensagem_para_servidor.txt", "r", encoding="utf-8") as f:
    dados = json.load(f)
    print("[DEBUG] Dados recebidos:", dados)
    mensagem_cpt = dados["mensagem"]
    mensagem = rsa_decrypt(mensagem_cpt, d_srv, n_srv)
    print("[Servidor] Mensagem decriptada:", mensagem)

resposta = input("[Servidor] Digite sua resposta: ")
resposta_cpt = rsa_encrypt(resposta, e_cli, n_cli)
print("[DEBUG] Resposta cifrada:", resposta_cpt)

with open("resposta_do_servidor.txt", "w", encoding="utf-8") as f:
    json.dump({"mensagem": resposta_cpt}, f)

print("[Servidor] Resposta criptografada enviada.")
