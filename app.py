from flask import Flask, render_template, request
#dizionari delle parole
parole_sospette = {
    "scoperto": -3, "incredibile": -2, "mai visto": -3, "potere": -2,
    "segreto": -2, "conspiracy": -3, "rivelato": -2, "imminente": -2,
    "allarmante": -3, "indipendente": -1, "falso": -3, "truffa": -3,
    "non veritiero": -3, "esclusiva": -2, "senza prova": -3
} 

parole_rassicuranti = {
    "studio": 2, "documentato": 2, "verificato": 2, "autorizzato": 2,
    "certificato": 3, "scientifico": 3, "approvato": 2, "ufficiale": 2,
    "comunicazione": 1, "analisi": 2, "dati": 2, "conferma": 2,
    "pubblicato": 2, "approfondito": 2, "indipendente": 1, "trasparente": 2
}

app = Flask(__name__)

#funzione per analizzare punteggio titolo
def analizza_notizia(titolo):
    punteggio = 0
    #converte titolo in minuscolo e separa in parole
    parole = titolo.lower().split()

    #calcolo punteggio
    for parola in parole:
        if parola in parole_sospette:
            punteggio += parole_sospette[parola]
        if parola in parole_rassicuranti:
            punteggio += parole_rassicuranti[parola]
    return punteggio

#funzione per classificare notizia
def classifica_notizia(punteggio):
    if punteggio <= -6:
        return "Fake News"
    elif punteggio > -6 and punteggio < 6:
        return "Notizia Dubbia"
    else:
        return "Notizia Affidabile"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        titolo = request.form["titolo"]
        punteggio = analizza_notizia(titolo)
        classificazione = classifica_notizia(punteggio)
        return render_template("index.html", titolo=titolo, punteggio=punteggio, classificazione=classificazione)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
