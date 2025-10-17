# Marte

[English](#english) | [Русский](#русский)

---

## 🔍 Навигация / Navigation

### 📑 Быстрое меню / Quick Menu
- **⚡ Быстрый старт / Quick Start**
  - [Установка / Installation](#установка-installation)
  - [CLI использование / CLI Usage](#cli-использование-cli-usage)
  - [Пример кода / Code Example](#использование-в-коде-usage-in-code)

- **📚 Разделы / Sections**
  - [Особенности / Features](#особенности-features)
  - [Установка / Installation](#установка-installation)
  - [Зависимости / Dependencies](#зависимости-dependencies)
  - [Использование / Usage](#использование-usage)
  - [Примеры / Examples](#примеры-работы-examples)
  - [Примечания / Notes](#примечание-note)

- **🔧 Практическое использование / Practical Usage**
  - [CLI режим / CLI Mode](#cli-режим-cli-mode)
  - [Использование в коде / Code Integration](#использование-в-коде-usage-in-code)
  - [Прямое использование / Direct Usage](#прямое-использование-direct-usage)

---

## Русский

**Marte** - это инструмент для криптографических преобразований, реализующий многоуровневое шифрование с использованием нескольких алгоритмов.

### 📋 Содержание
1. [Особенности](#особенности)
2. [Установка](#установка)
3. [Зависимости](#зависимости)
4. [Использование](#использование)
5. [Примеры работы](#примеры-работы)
6. [Примечания](#примечание)

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

pip install cryptography pycrypto

### 🚀 Использование

#### CLI режим

python marte.py

#### Использование в коде

from marte import transform

# Шифрование
encrypted = transform("Текст", вес, уровень, ключ, "1")

# Дешифрование
decrypted = transform(encrypted, вес, уровень, ключ, "2")

#### Прямое использование

# Шифрование
python -c "from marte import transform; print(transform('Ваш текст', 100, 200, 300, '1'))"

# Дешифрование  
python -c "from marte import transform; print(transform('BASE64_ТЕКСТ', 100, 200, 300, '2'))"

### 💡 Примеры работы

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

### ⚠️ Примечание

Параметры `Weight`, `Level` и `Key` должны быть целыми числами и должны совпадать при шифровании и дешифровании для успешного восстановления данных.

---

## English

**Marte** is a cryptographic transformation tool that implements multi-layer encryption using several algorithms.

### 📋 Navigation
1. [Features](#features)
2. [Installation](#installation)
3. [Dependencies](#dependencies)
4. [Usage](#usage)
5. [Examples](#examples)
6. [Notes](#note)

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

git clone https://github.com/Fghthssss/Shifrator
cd Shifrator

### 📦 Dependencies

pip install cryptography pycrypto

### 🚀 Usage

#### CLI Mode

python marte.py

#### Usage in Code

from marte import transform

# Encryption
encrypted = transform("Text", weight, level, key, "1")

# Decryption
decrypted = transform(encrypted, weight, level, key, "2")

#### Direct Usage

# Encryption
python -c "from marte import transform; print(transform('Your text', 100, 200, 300, '1'))"

# Decryption
python -c "from marte import transform; print(transform('BASE64_ENCRYPTED_TEXT', 100, 200, 300, '2'))"


### 💡 Examples

#### 📤 Encryption (Translate):
1. Select method `1`
2. Enter text to encrypt
3. Specify parameters:
   - Weight
   - Level
   - Key

####
