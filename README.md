# PDF to Speech Converter

## 📜 Opis projektu
Ten skrypt w Pythonie konwertuje pliki **PDF** na mowę za pomocą biblioteki **pyttsx3** (Text-to-Speech). Możesz dostosować prędkość, głośność oraz wybrać głos syntezatora.

## 🛠 Wymagania
Przed uruchomieniem projektu upewnij się, że masz zainstalowane wymagane biblioteki:

```bash
pip install pymupdf pyttsx3
```

## 🚀 Jak używać?
1. Uruchom skrypt:
   ```bash
   python main.py
   ```
2. Wprowadź ścieżkę do pliku PDF.
3. Skrypt odczyta tekst z PDF i odtworzy go głosowo.

## ⚙️ Konfiguracja

### Zmiana prędkości i głośności
Możesz dostosować prędkość oraz głośność, edytując parametry w skrypcie:

```python
speech_rate = 180  # Domyślnie: 150
speech_volume = 0.9  # Zakres: 0.0 - 1.0
```

### Wybór głosu
Aby sprawdzić dostępne głosy, użyj:

```python
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} ({voice.id})")
```

A następnie wybierz głos:

```python
engine.setProperty("voice", voices[1].id)  # Wybierz inny głos
```

## 🖥 Przykład działania
```
Enter the path to the PDF file: example.pdf
(tekst jest odczytywany przez syntezator mowy)
```

## 📜 Licencja
Projekt jest udostępniany na licencji **MIT** – możesz go dowolnie modyfikować i używać. 🙌

---
📌 Stworzony przez **Jakub Wilk**

