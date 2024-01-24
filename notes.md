- BIAS:
  metrica che misura quanto distanti sono le nostre previsioni da quelle corrette.
  In pratica definisce quanto il nostro modello sia adatto allo scopo.
  Alto livello di bias può portare ad underfitting cioè un'eccessiva semplificazione del modello quindi all'underfitting dove si presta troppa poca attenzione ai dati di addestramento non riuscendo cosi a catturare a pieno il comportamento desiderato
- VARIANZA:
  descrive la variabilità delle previsioni del modello per dati diversi, esprime quando sia influenzato dai dati in input.
  Una varianza troppo alta è sitomo di overfitting dove il modello memorizza il comportamento dei dati in input e non riesce ad adattarsi a dati nuovi e quindi non generalizza

L'obbiettivo è avere entrambe le metriche più basse possibile
Non è proprio corretto dirlo ma solitamente bias e varianza hanno una proporzionalità inversa.
Il termine corretto è trade-off dove il comportamento di bias e varianza dipende molto dai dati

- ALTO BIAS E BASSA VARIANZA: il modello presenterà underfitting, quindi è troppo semplice e dobbiamo complicarlo magari passando da una regressione linare a una regressione linare polinomiale alzando il grado del polinomio
- BASSO BIAS E ALTA VARIANZA: il modello presenterà overfitting, quindi memorizzerà il comportamento dei dati di input e non sarà in grado di generalizzare con dati nuovi, la soluzione è semplificare il modello

Per riconoscere l'overfitting basta confrontare l'errore sul set di test con quello di train, se quello di test è molto più grande è presente overfitting

SOLUZIONI OVERFITTING:

- Diminuire la complessità del modello (rischio però di perdere l'apprendimento di comportamenti dettagliati)
- Regolarizzazione
