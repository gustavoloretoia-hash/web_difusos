from flask import Flask, render_template, Response
import matplotlib.pyplot as plt
import numpy as np
import io

app = Flask(__name__)

propiedades = [

{"nombre":"Contradicción","formula":"A ∩ Ā = ∅","validez":"No válida","descripcion":"No se cumple en lógica difusa.","ejemplo":"min(0.5,0.5)=0.5 ≠ 0","aplicacion":"Evita decisiones absolutas en sistemas inteligentes."},

{"nombre":"Exclusión del tercero","formula":"A ∪ Ā = X","validez":"No válida","descripcion":"No siempre se obtiene el universo.","ejemplo":"max(0.5,0.5)=0.5 ≠ 1","aplicacion":"Permite manejar incertidumbre en clasificación de datos."},

{"nombre":"Idempotencia","formula":"A ∩ A = A","validez":"Válida","descripcion":"No cambia el conjunto.","ejemplo":"min(0.7,0.7)=0.7","aplicacion":"Evita redundancia en reglas difusas."},

{"nombre":"Doble negación","formula":"Ā̄ = A","validez":"Válida","descripcion":"Negar dos veces devuelve el original.","ejemplo":"1-(1-0.6)=0.6","aplicacion":"Permite consistencia en inferencias del sistema."},

{"nombre":"Conmutativa","formula":"A ∩ B = B ∩ A","validez":"Válida","descripcion":"El orden no importa.","ejemplo":"min(0.6,0.8)=min(0.8,0.6)","aplicacion":"Permite flexibilidad en reglas de decisión."},

{"nombre":"Asociativa","formula":"(A ∪ B) ∪ C = A ∪ (B ∪ C)","validez":"Válida","descripcion":"La agrupación no afecta.","ejemplo":"max(max(0.2,0.5),0.8)","aplicacion":"Optimiza el procesamiento de múltiples variables."},

{"nombre":"Distributiva","formula":"A ∩ (B ∪ C)","validez":"Válida","descripcion":"Permite reorganizar.","ejemplo":"min(0.7, max(0.5,0.9))","aplicacion":"Facilita modelado de reglas complejas."},

{"nombre":"Absorción","formula":"A ∪ (A ∩ B) = A","validez":"Válida","descripcion":"El conjunto absorbe.","ejemplo":"max(0.6, min(0.6,0.8))","aplicacion":"Reduce redundancia en inferencia difusa."},

{"nombre":"Absorción del complemento","formula":"A ∪ (Ā ∩ B)","validez":"Válida","descripcion":"Relaciona complemento.","ejemplo":"depende de μA y μB","aplicacion":"Mejora modelado de condiciones opuestas."},

{"nombre":"Leyes de De Morgan","formula":"(A ∪ B)' = A' ∩ B'","validez":"Válida","descripcion":"Relación entre operaciones.","ejemplo":"1 - max(μA, μB)","aplicacion":"Base en lógica difusa para sistemas inteligentes."},

{"nombre":"Conjunto vacío","formula":"A ∩ ∅ ≠ ∅","validez":"Válida","descripcion":"Difiere de lógica clásica.","ejemplo":"puede haber valores > 0","aplicacion":"Permite modelar incertidumbre residual."}

]

@app.route("/")
def home():
    return render_template("index.html", propiedades=propiedades)

# GRÁFICA GAUSSIANA
@app.route("/grafica/gaussiana")
def gaussiana():
    x = np.linspace(0,10,100)
    y = np.exp(-((x-5)**2)/2)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Función de Membresía Gaussiana")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return Response(img.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
    

 