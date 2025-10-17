
# Инструкция по запуску и проверке

## 1. Подготовка окружения

1. Убедитесь, что установлен **Python 3.8 или выше**:  
   ```bash
   python --version


2. Установите библиотеку **Jinja2**, которая используется для шаблонизации:

   ```bash
   pip install Jinja2
   ```

---

## 2. Подготовка входных данных

Создайте файл `data.json` в корне проекта со следующим примерным содержимым:

```json
{
 "debtor_name": "Viktor Pereira de Guzman",
 "total_amount": 2382,
 "extension_amount": 499,
 "currency": "PHP",
 "due_date": "2025-09-30",
 "days_overdue": 12,
 "payment_methods": ["GCash", "PayMaya", "Bank Transfer"],
 "callback_number": "+63 960 000-00-00",
 "language": "en-PH",
 "company_name": "MoneyDog",
 "assistant_name": "Mariel",
 "timezone": "Asia/Manila"
}
```

---

## 3. Генерация промпта

Запустите команду:

```bash
python prompt_builder.py --input data.json --output final_prompt.md
```

или (в зависимости от системы):

```bash
python3 prompt_builder.py --input data.json --output final_prompt.md
```

После успешного выполнения появится сообщение о создании файла, а в папке проекта появится `final_prompt.md`.

---

## 4. Проверка результата

1. Откройте файл `final_prompt.md` в любом текстовом редакторе и убедитесь, что значения из `data.json` подставлены корректно.


---

---
Примечание - добавил валидацию, чтобы были все параметры в json.
---