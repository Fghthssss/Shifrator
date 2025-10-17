# Marte

[English](#english) | [Русский](#русский)

---

## Русский

**Marte** - это инструмент для криптографических преобразований, реализующий многоуровневое шифрование с использованием нескольких алгоритмов. Программа последовательно применяет AES, 3DES, DES и Blowfish для обеспечения повышенной безопасности данных.

### Особенности

- Многоуровневое шифрование (AES → 3DES → DES → Blowfish)
- Поддержка симметричных алгоритмов шифрования:
  - AES (CBC mode)
  - 3DES (Triple DES)
  - DES
  - Blowfish
- Динамическая генерация ключей на основе пользовательских параметров
- Сжатие данных с использованием zlib
- Кодирование в base64 для удобства передачи
- Сериализация данных с помощью marshal

### Установка

git clone https://github.com/your-username/marte.git
cd marte

### Зависимости

pip install cryptography pycrypto

### Использование

python marte.py

#### Пример работы:

1. **Шифрование (Translate):**
   - Выберите метод `1`
   - Введите текст для шифрования
   - Укажите параметры:
     - Weight (вес)
     - Level (уровень) 
     - Key (ключ)

2. **Дешифрование (Untranslate):**
   - Выберите метод `2`
   - Введите зашифрованный текст
   - Укажите те же параметры, что использовались при шифровании

### Примечание

Параметры `Weight`, `Level` и `Key` должны быть целыми числами и должны совпадать при шифровании и дешифровании для успешного восстановления данных.

---

## English

**Marte** is a cryptographic transformation tool that implements multi-layer encryption using several algorithms. The program sequentially applies AES, 3DES, DES, and Blowfish to provide enhanced data security.

### Features

- Multi-layer encryption (AES → 3DES → DES → Blowfish)
- Support for symmetric encryption algorithms:
  - AES (CBC mode)
  - 3DES (Triple DES)
  - DES
  - Blowfish
- Dynamic key generation based on user parameters
- Data compression using zlib
- Base64 encoding for easy transmission
- Data serialization using marshal

### Installation

git clone https://github.com/Fghthssss/Shifrator
cd Shifrator

### Dependencies

pip install cryptography pycrypto

### Usage

python marte.py

#### Example:

1. **Encryption (Translate):**
   - Select method `1`
   - Enter text to encrypt
   - Specify parameters:
     - Weight
     - Level
     - Key

2. **Decryption (Untranslate):**
   - Select method `2`
   - Enter encrypted text
   - Specify the same parameters used during encryption

### Note

The `Weight`, `Level`, and `Key` parameters must be integers and must match during encryption and decryption for successful data recovery.

### Security Notice

This tool is for educational purposes. Use professional cryptographic libraries for production systems.

