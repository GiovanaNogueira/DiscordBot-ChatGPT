from flask import Flask, request, render_template
import json
import uuid

app = Flask(__name__)

@app.route("/")
def home():
  return "Página incial"
  
@app.route('/logs')
def list():
  lista = []
  try:
    with open("db.json", "r") as arq:
      lista = json.loads(arq.read())
      print(lista)
      if(len(lista)==0):
        return "Não há log na lista"
  except Exception as e:
    return {"message": str(e)}, 400

  return lista, 200

@app.route('/logs', methods=["POST"])
def create():
  lista = []
  body = request.json
  body["_id"] = str(uuid.uuid4())
  with open("db.json", "r+") as arq:
    lines = arq.read()
    lista = json.loads(lines)
    lista.append(body)
    arq.seek(0)
    arq.write(json.dumps(lista))
    arq.truncate()
    return body, 201

  return {"message": "Não foi possível criar o registro"}, 400
  
@app.route('/logs/<id>')
def read(id):
  lista = []
  with open("db.json") as arq:
    lista = json.loads(arq.read())
    for i in range(len(lista)):
      if lista[i]["_id"] == id:
        return lista[i], 200
       
  return {"message": "Log não encontrado"}, 404


@app.route('/logs/<id>', methods=["PUT"])
def update(id):
  lista=[]
  body = request.json
  with open("db.json", "r+") as arq:
    lista = json.loads(arq.read())
    for i in range(len(lista)):
      if lista[i]["_id"] == id:
        lista[i]["_id"] = id
        for key, value in body.items():
          lista[i][key] = value
        
    arq.seek(0)
    arq.write(json.dumps(lista))
    arq.truncate()
  return {"message": "Log atualizado com sucesso"}, 200
  

@app.route('/logs/<id>', methods=["DELETE"])
def delete(id):
  lista=[]
  with open("db.json", "r+") as arq:
    lista = json.loads(arq.read())
    for log in lista:
      if (log['_id']==id):
        lista.remove(log)
        print("deletado")
    
    arq.seek(0)
    arq.write(json.dumps(lista))
    arq.truncate()

  return {"message": "Log deletado com sucesso"}, 200

app.run(host='0.0.0.0', port=81)