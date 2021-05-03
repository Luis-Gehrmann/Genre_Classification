# Genre_Classification
A machine learning-project to determine the Genre of a given song

Ansatz: Der Nutzer gibt dem Programm ein beliebig langes Soundfile im wav-Format als Input.
Von diesem wird die Länge durch die "soundfile-Library" ermittelt und entsprechend der Länge wird der Song anschließend mithilfe der "pydub-Library" in n 3-Sekunden-Abschnitte aufgeteilt.
Für jeden dieser Abschnitte werden mithilfe der "librosa-library" (eventuell zusätzlich weitere) musikalische Eigenschaften, wie Tempo, oder Harmonieren isoliert und separiert gespeichert.
Für jeden Abschnitt resultiert ein Array an isolierten Eigenschaften, aufgrund dessen ein fertig trainiertes ML-Modell predictions über das Gerne machen kann.
Zuletzt wird das Genre als Output ausgewählt, welches für die meisten Abschnitte von dem ML-Algorithmus vorausgesagt wurde.

Das Stammverzeichnis enhält das Notebook Slicing, welches in der Trainingsphase des Neuronalen Netzwerks genutzt wird, um die Traininssongs in 3 Sekundenabschnitte zu zerschneiden. Dies hielten wir für sinnvoll, um eine große Masse einheitlicher Trainingsdaten zu erzeugen. Des Weiteren ist hier das Frontend im ZIP File angehängt
Das Notebook TrainModel wird dafür verwendet, dass neuronale Netzwerk, sowie ein Dictionary und den Scaler für die Normalisierung zu erzeugen.
In dem Ordner Backend ist das Backend mit der Flask Route zur Konvertierung und Bestimmung von Genre aus dem hochgeladenen Songs.
