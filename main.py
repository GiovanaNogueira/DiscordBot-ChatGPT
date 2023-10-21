import discord
import requests as req
from bs4 import BeautifulSoup
import os
import json


TOKEN = os.environ['discord_bot_token']
intents = discord.Intents.all() 
client = discord.Client(intents = intents)
API_Key = os.environ['api_key']


def chatApi(user_msg):
  headers = {
    "Authorization" : f"Bearer {API_Key}",
    "Content-Type": "application/json"
  }
  link = "https://api.openai.com/v1/chat/completions"
  id_modelo = "gpt-3.5-turbo"
  body = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": user_msg}]
  }
  body_json = json.dumps(body)
  requisicao = req.post(link, headers = headers, data = body_json)
  
  resposta_chat = requisicao.json()
  mensagem = resposta_chat["choices"][0]["message"]["content"]
  return mensagem

def busca():
  resp = req.get("https://www.cbctc.puc-rio.br/Paginas/Contato/ContatoFaleConosco.aspx")
  if resp.status_code == 200:
      parsed_html = BeautifulSoup(resp.text, "html.parser")
      lista = parsed_html.find_all("li", {"class":"default-list__item"})
      contatos = lista[1].text + "\n" + lista[2].text
      return contatos
  else:
    return "Não foi possível"


@client.event
async def on_ready():
  print(f"{client.user} tá rodando")

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
    
  user_msg = msg.content.lower()
  if "contatos puc" in user_msg:
    resposta = busca()
    await msg.author.send(resposta)

  else:
    resposta = chatApi(user_msg)
    await msg.author.send(resposta)
    
  req_body = {
    "authorName": msg.author.name, 
    "msgContent": msg.content,
    "createAt": str(msg.created_at)
  }
  
  response_post = req.post("https://atividade-07-discord-bot-system-logs-giovananogueira.eng4431-20232.repl.co/logs", json = req_body)

  if response_post.status_code ==201:
    print("\nLog registrado com sucesso\n")
  else:
    print("Erro ao registrar log\n")
    
  print(msg.content)


client.run(TOKEN)