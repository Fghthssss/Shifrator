# Marte

[English](#english) | [Русский](#русский)

---

## 🔍 Навигация / Navigation

- [🚀 Быстрый старт / Quick Start](#-быстрый-старт--quick-start)
- [⭐ Особенности / Features](#-особенности--features)
- [📥 Установка / Installation](#-установка--installation)
- [📦 Зависимости / Dependencies](#-зависимости--dependencies)
- [🔧 Использование / Usage](#-использование--usage)
- [💡 Примеры / Examples](#-примеры--examples)
- [⚠️ Примечания / Notes](#️-примечания--notes)

---

## Русский

### 🚀 Быстрый старт

**Marte** - это инструмент для криптографических преобразований, реализующий многоуровневое шифрование с использованием нескольких алгоритмов.

### ⭐ Особенности

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

### 📥 Установка

```bash
git clone https://github.com/Fghthssss/Shifrator
cd Shifrator
```

### 📦 Зависимости

```bash
pip install cryptography pycrypto
```

### 🔧 Использование

#### CLI режим

```bash
python marte.py
```

#### Использование в коде

```python
from marte import transform

# Шифрование
encrypted = transform("Текст", вес, уровень, ключ, "1")

# Дешифрование
decrypted = transform(encrypted, вес, уровень, ключ, "2")
```

#### Прямое использование

```bash
# Шифрование
python -c "from marte import transform; print(transform('Ваш текст', 100, 200, 300, '1'))"

# Дешифрование  
python -c "from marte import transform; print(transform('BASE64_ТЕКСТ', 100, 200, 300, '2'))"
```

### 💡 Примеры

#### 📤 Шифрование (Translate):
1. Выберите метод `1`
2. Введите текст для шифрования
3. Укажите параметры:
   - Weight (вес)
   - Level (уровень) 
   - Key (ключ)

#### 📥 Дешифрование (Untranslate):
1. Выберите метод `2`
2. Введите зашифрованный текст
3. Укажите те же параметры, что использовались при шифровании

### ⚠️ Примечания

Параметры `Weight`, `Level` и `Key` должны быть целыми числами и должны совпадать при шифровании и дешифровании для успешного восстановления данных.

---

## English

### 🚀 Quick Start

**Marte** is a cryptographic transformation tool that implements multi-layer encryption using several algorithms.

### ⭐ Features

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

### 📥 Installation

```bash
git clone https://github.com/Fghthssss/Shifrator
cd Shifrator
```

### 📦 Dependencies

```bash
pip install cryptography pycrypto
```

### 🔧 Usage

#### CLI Mode

```bash
python marte.py
```

#### Usage in Code

```python
from marte import transform

# Encryption
encrypted = transform("Text", weight, level, key, "1")

# Decryption
decrypted = transform(encrypted, weight, level, key, "2")
```

#### Direct Usage

```bash
# Encryption
python -c "from marte import transform; print(transform('Your text', 100, 200, 300, '1'))"

# Decryption
python -c "from marte import transform; print(transform('BASE64_ENCRYPTED_TEXT', 100, 200, 300, '2'))"
```

### 💡 Examples

#### 📤 Encryption (Translate):
1. Select method `1`
2. Enter text to encrypt
3. Specify parameters:
   - Weight
   - Level
   - Key

#### 📥 Decryption (Untranslate):
1. Select method `2`
2. Enter encrypted text
3. Specify the same parameters used during encryption

### ⚠️ Notes

The `Weight`, `Level`, and `Key` parameters must be integers and must match during encryption and decryption for successful data recovery.

### 🔒 Security Notice

This tool is for educational purposes. Use professional cryptographic libraries for production systems.

---

## 🔄 Быстрая навигация / Quick Navigation

- [⬆️ Наверх / Back to Top](#marte)
- [🚀 Быстрый старт / Quick Start](#-быстрый-старт--quick-start)
- [⭐ Особенности / Features](#-особенности--features)
- [📥 Установка / Installation](#-установка--installation)
- [🔧 Использование / Usage](#-использование--usage)
- [💡 Примеры / Examples](#-примеры--examples)
- [⚠️ Примечания / Notes](#️-примечания--notes)
