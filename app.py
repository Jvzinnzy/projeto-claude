from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__) 

@app.route("/")
def homepage():
    redes = {
        "GitHub": "https://github.com/Jvzinnzy",
        "Instagram": "https://www.instagram.com/nunes_.ths/",
        "Linkedin": "https://www.linkedin.com/in/jo%C3%A3o-vitor-nunes-pereira/",
    }
    perfil = buscar_perfil()
    print("Seja Bem vindo!")
    return render_template("main.html", redes=redes, perfil=perfil)

def buscar_perfil():
    print("Se rodar isso deu certo aqui então ")
    reposta = requests.get("https://api.github.com/users/Jvzinnzy")
    print(reposta.status_code)
    dados = reposta.json()
    return dados

@app.route("/sobre")
def descricao():
    return "Olá, me chamo João Vitor e estou aprendendo as mecânicas básicas do Flask!"

@app.route("/projetos")
def get_projetos():
    #vai pegar os meus projetos e retornar em Json
    projetos = {
        "nome": "lista",
        "tempo": "12m",
        "descrição": "O programa vai retornar..."
    }

    return jsonify(projetos)

# Ponto de entrada do programa
if __name__ == "__main__":
    print("Seu programa está rodando!") 
    app.run(debug=True)  # Aqui é onde você coloca o run()

