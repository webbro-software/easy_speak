# **easy_speech**

`easy_speech` is a simple and efficient text-to-speech (TTS) package that converts text into speech and plays it instantly without saving audio files.

---

## **Installation**

To install `easy_speech`, run:

```sh
pip install easy_speech
```

For local development, install it in editable mode:

```sh
pip install -e .
```

---

## **Usage**

### **Basic Example**

```python
from easy_speech import easy_speech

# Convert text to speech and play it
easy_speech("Hello, welcome to easy_speech!")
```

### **Change Language**

```python
easy_speech("Hola, bienvenido a easy_speech!", lang="es")
```

---

## **Function Reference**

### **easy_speech(text, lang="en")**

Converts the given text into speech and plays it immediately.

#### **Parameters:**

- `text` (str): The text to be converted into speech.
- `lang` (str, optional): The language code (default is `"en"`).

#### **Returns:**

None (plays the speech instantly).

---

## **Contributing**

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Add new feature"
   ```
4. Push the changes:
   ```sh
   git push origin feature-name
   ```
5. Open a pull request.

Feel free to report issues and suggest improvements! 🚀

---

## **License**

MIT License.
