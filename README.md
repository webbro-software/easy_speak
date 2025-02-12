# **easy_speak**

`easy_speak` is a lightweight and efficient text-to-speech (TTS) package that allows you to convert text into speech and play it instantly without saving audio files. It provides a simple way to integrate speech synthesis into Python applications.

---

## **Installation**

To install `easy_speak`, run:

```sh
pip install easy_speak
```

For local development, install it in editable mode:

```sh
pip install -e .
```

---

## **Usage**

### **Basic Example**

```python
from easy_speak import easy_speak

# Convert text to speech and play it
easy_speak("Hello, welcome to easy_speak!")
```

### **Change Language**

```python
easy_speak("Hola, bienvenido a easy_speak!", lang="es")
```

---

## **Function Reference**

### **easy_speak(text, lang="en")**

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

MIT [License](./LICENSE).
