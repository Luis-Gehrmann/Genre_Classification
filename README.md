# Genre_Classification
A machine learning-project to determine the Genre of a given song

Ansatz: Der Nutzer gibt dem Programm ein beliebig langes Soundfile im wav-Format als Input.
Von diesem wird die Länge durch die "soundfile-Library" ermittelt und entsprechend der Länge wird der Song anschließend mithilfe der "pydub-Library" in n 3-Sekunden-Abschnitte aufgeteilt.
Für jeden dieser Abschnitte werden mithilfe der "librosa-library" (eventuell zusätzlich weitere) musikalische Eigenschaften, wie Tempo, oder Harmonieren isoliert und separiert gespeichert.
Für jeden Abschnitt resultiert ein Array an isolierten Eigenschaften, aufgrund dessen ein fertig trainiertes ML-Modell predictions über das Gerne machen kann.
Zuletzt wird das Genre als Output ausgewählt, welches für die meisten Abschnitte von dem ML-Algorithmus vorausgesagt wurde.

Für die Entwicklung werden zwei Programme benötigt. In Programm 1 wird ein Neuronales Netz auf die korrekte Genrebestimmung trainiert.
In Programm 2 wird das entwickelte Neuronale Netz für die Prediction eines eingegebenen Soundfiles genutzt
