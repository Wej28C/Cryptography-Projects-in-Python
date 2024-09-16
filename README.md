# Cryptography-Projects-in-Python
Welcome to my cryptography portfolio! This repository showcases various cryptographic techniques and algorithms implemented in Python. These projects were developed as part of my cryptography coursework, focusing on encryption, decryption, and data security methodologies.

## 📚 Topics Covered

Throughout these practicals, I've explored and implemented the following cryptographic concepts and techniques:

### 1. **Classical Encryption Techniques**
   - **Caesar Cipher**: A basic substitution cipher where each letter in the plaintext is shifted by a fixed number of positions.
   - **Affine Cipher**: A cipher that applies a linear transformation to encrypt letters, using two keys for more security.
   - **Vigenère Cipher**: A polyalphabetic cipher using a repeating key to apply variable shifts for each character.

### 2. **Block Cipher Modes**
   - **Electronic Codebook (ECB)**: Encrypts plaintext in fixed-size blocks independently, offering simplicity but potential vulnerabilities.
   - **Cipher Block Chaining (CBC)**: Enhances ECB security by XORing each plaintext block with the previous ciphertext block before encryption.

### 3. **Advanced Cryptographic Algorithms**
   - **Feistel Network**: Implemented symmetric encryption through Feistel rounds, ensuring diffusion and confusion.
   - **DES (Data Encryption Standard)**: Implemented the classic DES algorithm, applying multiple rounds of substitution and permutation on 64-bit blocks.

### 4. **Public Key Cryptography**
   - **RSA Algorithm**: Generated RSA keys and implemented both encryption and decryption. RSA ensures secure communication using large prime numbers.
   
### 5. **Hashing Functions**
   - **Davies-Meyer Hash Function**: Implemented a simple hash function based on block ciphers.
   - **SHA-256 Analysis**: Performed statistical tests on SHA-256 outputs to examine randomness using the Chi-square method.

### 6. **Mathematical Foundations**
   - **Miller-Rabin Primality Test**: Verified large numbers for primality using probabilistic methods.
   - **Elliptic Curve Cryptography**: Generated points on elliptic curves, a foundational concept for modern cryptography protocols.

### 7. **Error Detection & Correction**
   - **CRC8 with Error Correction**: Implemented cyclic redundancy checks to ensure error detection and correction.
   - **Parity Bit Error Detection**: Developed algorithms to encode data with parity bits and detect single-bit errors.

### 8. **Compression Techniques**
   - **Huffman Encoding**: Implemented a lossless compression algorithm, assigning shorter codes to more frequent characters.
   - **Run-Length Encoding (RLE)**: Compressed repeated data sequences, reducing file sizes efficiently.

### 9. **Birthday Paradox & Collision Simulation**
   - **Collision Detection Simulation**: Simulated the birthday paradox to evaluate the likelihood of hash collisions, crucial for security in hashing algorithms.

## 🛠 Technologies Used

- **Python**: Main language for all cryptographic implementations.
- **Matplotlib & Scipy**: Used for visualizing data and performing statistical tests, especially for frequency analysis and Chi-square tests.
- **Custom Classes**: Developed from scratch, covering both classical and modern cryptographic systems.

## 📈 Project Highlights

- **Feistel Network Visualization**: Displayed diffusion and confusion using graphical outputs.
- **Elliptic Curve Plotting**: Generated plots of elliptic curves for use in cryptographic key exchanges.
- **SHA-256 Distribution**: Compared the frequency of byte occurrences in SHA-256 outputs, confirming the robustness of the hash function.
## 🧠 Key Learnings
- Developed a deep understanding of both classical and modern cryptographic algorithms.
- Enhanced practical skills in Python, focusing on encryption, decryption, and data integrity.
- Gained proficiency in error detection, hashing, and compression techniques, key to building secure systems.
