'''
Напишіть функцію get_fullname на Python, яка приймає ім'я, прізвище та, опціонально, друге ім'я 
(або по батькові) та повертає рядок з повним іменем користувача.

Задачі:

    Створіть функцію get_fullname, яка приймає три аргументи: first_name, last_name та middle_name. 
    Зробіть middle_name необов'язковим аргументом зі значенням за замовчуванням "".

    Якщо middle_name передано, функція повинна повертати повне ім'я у форматі 
    'first_name middle_name last_name'.

    Якщо middle_name не передано, функція повинна повертати повне ім'я у форматі 'first_name last_name'.
    Для формування повного імені використовуйте f-рядок.

Очікуваний результат:

Функція повертає рядок з повним іменем користувача, залежно від того, чи передано друге ім'я.

Підказки:

    Використовуйте умовну конструкцію if для перевірки, чи middle_name не порожній.
    Для створення рядка з повним іменем використовуйте f-рядок для вставки значень змінних.


'''
variable = 1
variable = "one"

# first_name, last_name, middle_name
# John Doe Alice -> John Alice Doe
# Jane Doe -> Jane Doe
def get_fullname(first_name: str, last_name: str, middle_name: str='') -> str | None:
    """
    Recieves first name, last name and middle name of a person and returns full name

    If middle name is not provided, returns full name without it

    - first_name: First name of a person
    - last_name: Last name of a person
    - middle_name: Middle name of a person (Optional)
    """
    if middle_name:
        return f'{first_name} {middle_name} {last_name}'
    return f'{first_name} {last_name}'

# get_fullname(1, 1, 1)
print(get_fullname("John", "Doe", "Alice"))
print(get_fullname("Jane", "Doe")) # Ctrl L - to clean terminal
print(get_fullname("Petro", "Ivanovych", "Zaliznyak"))

sum([1, 2, 3])