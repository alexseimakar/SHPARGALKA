print("Начало работы")
# Числа
def add_numbers(a, b):                     # Складывает два числа и возвращает результат. 2 + 3 = 5
    return a + b

def multiply_numbers(a, b):                # Умножает два числа и возвращает результат. 2 * 3 = 6
    return a * b

def divide_numbers(a, b):                  # Делит первое число на второе и возвращает результат. 6 / 3 = 2.0
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power_numbers(a, b):                   # Возводит первое число в степень второго числа и возвращает результат. 2 ** 3 = 8
    return a ** b

def is_even(number):                       # Проверяет, является ли число четным. 4 -> True
    return number % 2 == 0

def is_odd(number):                        # Проверяет, является ли число нечетным. 3 -> True
    return not is_even(number)

# Строки
def concatenate_strings(s1, s2):           # Объединяет две строки и возвращает результат. "hello" + " world" = "hello world"
    return s1 + s2

def string_length(s):                      # Возвращает длину строки. len("hello") = 5
    return len(s)

def reverse_string(s):                     # Возвращает строку в обратном порядке. "hello"[::-1] = "olleh"
    return s[::-1]

def capitalize_string(s):                  # Возвращает строку с первой заглавной буквой. "hello".capitalize() = "Hello"
    return s.capitalize()

def is_palindrome(s):                      # Проверяет, является ли строка палиндромом. "madam" -> True
    return s == s[::-1]

def count_substring(s, sub):               # Считает количество вхождений подстроки в строку. "hello world".count("l") = 3
    return s.count(sub)

# Списки
def list_sum(lst):                         # Возвращает сумму элементов списка. sum([1, 2, 3]) = 6
    return sum(lst)

def list_length(lst):                      # Возвращает длину списка. len([1, 2, 3]) = 3
    return len(lst)

def list_append(lst, item):                # Добавляет элемент в конец списка и возвращает измененный список. [1, 2, 3].append(4) = [1, 2, 3, 4]
    lst.append(item)
    return lst

def list_remove(lst, item):                # Удаляет первый найденный элемент из списка и возвращает измененный список. [1, 2, 3].remove(2) = [1, 3]
    lst.remove(item)
    return lst

def list_slice(lst, start, end):           # Возвращает срез списка от start до end. [1, 2, 3, 4][1:3] = [2, 3]
    return lst[start:end]

def list_sort(lst):                        # Сортирует список и возвращает его. sorted([3, 1, 2]) = [1, 2, 3]
    lst.sort()
    return lst

def list_reverse(lst):                     # Разворачивает список и возвращает его. [1, 2, 3][::-1] = [3, 2, 1]
    lst.reverse()
    return lst

# Кортежи
def tuple_sum(tpl):                        # Возвращает сумму элементов кортежа. sum((1, 2, 3)) = 6
    return sum(tpl)

def tuple_length(tpl):                     # Возвращает длину кортежа. len((1, 2, 3)) = 3
    return len(tpl)

def tuple_unpack(tpl):                     # Распаковывает кортеж в список. list((1, 2, 3)) = [1, 2, 3]
    return list(tpl)

def tuple_concatenate(tpl1, tpl2):         # Объединяет два кортежа и возвращает результат. (1, 2) + (3, 4) = (1, 2, 3, 4)
    return tpl1 + tpl2

def tuple_repeat(tpl, n):                  # Повторяет кортеж n раз и возвращает результат. (1, 2) * 2 = (1, 2, 1, 2)
    return tpl * n

def tuple_count(tpl, item):                # Считает количество вхождений элемента в кортеж. (1, 2, 2, 3).count(2) = 2
    return tpl.count(item)

# Множества
def set_union(s1, s2):                     # Возвращает объединение двух множеств. {1, 2} | {2, 3} = {1, 2, 3}
    return s1.union(s2)

def set_intersection(s1, s2):              # Возвращает пересечение двух множеств. {1, 2} & {2, 3} = {2}
    return s1.intersection(s2)

def set_difference(s1, s2):                # Возвращает разность двух множеств. {1, 2, 3} - {2} = {1, 3}
    return s1.difference(s2)

def set_symmetric_difference(s1, s2):      # Возвращает симметрическую разность двух множеств. {1, 2} ^ {2, 3} = {1, 3}
    return s1.symmetric_difference(s2)

def set_add(s, item):                      # Добавляет элемент в множество и возвращает измененное множество. {1, 2}.add(3) = {1, 2, 3}
    s.add(item)
    return s

def set_remove(s, item):                   # Удаляет элемент из множества и возвращает измененное множество. {1, 2, 3}.remove(2) = {1, 3}
    s.remove(item)
    return s

# Словари
def dict_keys(d):                          # Возвращает список ключей словаря. list({"a": 1, "b": 2}.keys()) = ["a", "b"]
    return list(d.keys())

def dict_values(d):                        # Возвращает список значений словаря. list({"a": 1, "b": 2}.values()) = [1, 2]
    return list(d.values())

def dict_items(d):                         # Возвращает список пар (ключ, значение) словаря. list({"a": 1, "b": 2}.items()) = [("a", 1), ("b", 2)]
    return list(d.items())

def dict_get(d, key, default=None):        # Возвращает значение по ключу, если ключ не найден, возвращает default. {"a": 1}.get("b", 0) = 0
    return d.get(key, default)

def dict_update(d1, d2):                   # Обновляет первый словарь парами из второго словаря. {"a": 1}.update({"b": 2}) = {"a": 1, "b": 2}
    d1.update(d2)
    return d1

def dict_merge(d1, d2):                    # Объединяет два словаря и возвращает результат. {**{"a": 1}, **{"b": 2}} = {"a": 1, "b": 2}
    return {**d1, **d2}

# Булевы значения
def is_true(b):                            # Проверяет, является ли значение True. True -> True
    return b is True

def is_false(b):                           # Проверяет, является ли значение False. False -> True
    return b is False

def logical_and(a, b):                     # Возвращает логическое И двух значений. True and False = False
    return a and b

def logical_or(a, b):                      # Возвращает логическое ИЛИ двух значений. True or False = True
    return a or b

def logical_not(a):                        # Возвращает логическое НЕ значения. not True = False
    return not a

# None
def is_none(o):                            # Проверяет, является ли значение None. None -> True
    return o is None

def coalesce(a, b):                        # Возвращает первое значение, если оно не None, иначе второе значение. None or 1 = 1
    return a if a is not None else b

# Комплексные числа
def complex_add(a, b):                     # Складывает два комплексных числа и возвращает результат. (1+2j) + (3+4j) = (4+6j)
    return a + b

def complex_multiply(a, b):                # Умножает два комплексных числа и возвращает результат. (1+1j) * (1+1j) = (1+1j)*(1+1j)
    return a * b

def complex_conjugate(a):                  # Возвращает сопряженное комплексное число. (1+2j).conjugate() = (1-2j)
    return a.conjugate()

def complex_abs(a):                        # Возвращает модуль комплексного числа. abs(3+4j) = 5.0
    return abs(a)

# Работа с API
import requests

def get_api_data(url):                     # Получает данные из API по указанному URL. get("https://jsonplaceholder.typicode.com/posts/1") -> {'userId': 1, 'id': 1, 'title': '...', 'body': '...'}
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get data from API. Status code: {response.status_code}")

def post_api_data(url, data):              # Отправляет данные на API по указанному URL. post("https://jsonplaceholder.typicode.com/posts", {"title": "foo", "body": "bar", "userId": 1}) -> {'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to post data to API. Status code: {response.status_code}")

# Работа с базой данных
import sqlite3

def create_db_connection(db_file):         # Создает подключение к базе данных SQLite. connect("example.db") -> <sqlite3.Connection object at 0x...>
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

def create_table(conn):                   # Создает таблицу в базе данных. execute("CREATE TABLE IF NOT EXISTS projects (...)")
    try:
        sql = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text
                                    ); """
        cursor = conn.cursor()
        cursor.execute(sql)
    except Exception as e:
        print(e)

def insert_project(conn, project):        # Вставляет проект в таблицу базы данных. execute("INSERT INTO projects VALUES (?, ?, ?)", project)
    sql = """INSERT INTO projects(name, begin_date, end_date)
             VALUES(?, ?, ?)"""
    cursor = conn.cursor()
    cursor.execute(sql, project)
    conn.commit()
    return cursor.lastrowid

def select_all_projects(conn):             # Выбирает все проекты из таблицы базы данных. execute("SELECT * FROM projects")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    rows = cursor.fetchall()
    return rows

def select_project_by_id(conn, project_id):# Выбирает проект по идентификатору из таблицы базы данных. execute("SELECT * FROM projects WHERE id=?", (project_id,))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects WHERE id=?", (project_id,))
    row = cursor.fetchone()
    return row

def update_project(conn, project):        # Обновляет проект в таблице базы данных. execute("UPDATE projects SET ... WHERE id=?", project)
    sql = """UPDATE projects
             SET name = ?,
                 begin_date = ?,
                 end_date = ?
             WHERE id = ?"""
    cursor = conn.cursor()
    cursor.execute(sql, project)
    conn.commit()

def delete_project(conn, project_id):     # Удаляет проект из таблицы базы данных. execute("DELETE FROM projects WHERE id=?", (project_id,))
    sql = "DELETE FROM projects WHERE id=?"
    cursor = conn.cursor()
    cursor.execute(sql, (project_id,))
    conn.commit()

def main():
    # Пример работы с API
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    api_data = get_api_data(api_url)
    print("API Data:", api_data)

    # Пример работы с базой данных
    database = "example.db"
    conn = create_db_connection(database)
    if conn is not None:
        create_table(conn)
        project = ("Cool App", "2021-01-01", "2021-01-31")
        project_id = insert_project(conn, project)
        print("Project ID:", project_id)
        projects = select_all_projects(conn)
        print("Projects:", projects)
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == "__main__":
    main()

print("Конец работы")