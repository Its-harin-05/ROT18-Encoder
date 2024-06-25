<h1>ROT18-Encoder</h1>
This project is a simple web application built using Flask that provides an interface to encrypt and decrypt text using the ROT18 cipher. ROT18 combines ROT13 for letters and ROT5 for digits, shifting letters by 13 places and digits by 5 places.

<h2>Features</h2>

- **Encrypt/Decrypt Text:** Users can input text and get it encrypted/decrypted using ROT18.

- **CORS Support:** Enabled to allow cross-origin requests.
  
- **Web Interface:** A simple front-end to input and view results.

<h2>Requirements</h2>

- **Python 3.x**
  
- **Flask**
  
- **Flask-CORS**

<h2>Installation</h2>

1. Clone the repository to your local machine.

```bash
git clone https://github.com/Its-harin-05/ROT18-Encoder.git
```
```bash
cd ROT18-Encoder
```
2. Create a virtual environment and activate it.

```bash
python -m venv venv
```
```bash
source venv/bin/activate
```

3. Install the required packages.

```bash
pip install Flask Flask-CORS
```

<h2>Usage</h2>

1. Run the application:

```bash
python app.py
```
2. Open your browser and navigate:

```bash
http://localhost:5000
```
3. Enter the message you want to encrypt, and click on "Encrypt/Decrypt".

4. The encrypted message will be displayed.

<h2>Contribution</h2>
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.  
