# 🎮 Nickname Generator

Простой и мощный генератор никнеймов на Python.

## 📋 Описание

Этот проект генерирует случайные никнеймы в разных стилях:
- **Simple** - базовые комбинации (например: `FastTiger`)
- **Numbers** - с цифрами (например: `FastTiger42`)
- **Underscores** - с подчёркиваниями (например: `Fast_Tiger`)

## 🚀 Быстрый старт

### Требования
- Python 3.6+
- Никаких внешних зависимостей!

### Использование

```python
from main import generate_nickname

# Генерируем никнейм в простом стиле
nickname = generate_nickname('simple')
print(nickname)  # Пример: FastTiger

# С числами
nickname = generate_nickname('numbers')
print(nickname)  # Пример: FastTiger42

# С подчёркиваниями
nickname = generate_nickname('underscores')
print(nickname)  # Пример: Fast_Tiger

### 📄 Лицензия
- MIT License

### 👤 Автор
- arturchikgg
