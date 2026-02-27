from src.example import *

def run_example():
    print("Числа:")
    print("add_numbers(2, 3):", add_numbers(2, 3))
    print("multiply_numbers(2, 3):", multiply_numbers(2, 3))
    print("divide_numbers(6, 3):", divide_numbers(6, 3))
    try:
        print("divide_numbers(6, 0):", divide_numbers(6, 0))
    except ValueError as e:
        print("divide_numbers(6, 0):", e)
    print("power_numbers(2, 3):", power_numbers(2, 3))
    print("is_even(4):", is_even(4))
    print("is_odd(3):", is_odd(3))

    print("\nСтроки:")
    print('concatenate_strings("hello", " world"):', concatenate_strings("hello", " world"))
    print('string_length("hello"):', string_length("hello"))
    print('reverse_string("hello"):', reverse_string("hello"))
    print('capitalize_string("hello"):', capitalize_string("hello"))
    print('is_palindrome("madam"):', is_palindrome("madam"))
    print('count_substring("hello world", "l"):', count_substring("hello world", "l"))

    print("\nСписки:")
    lst = [1, 2, 3]
    print("list_sum([1, 2, 3]):", list_sum(lst))
    print("list_length([1, 2, 3]):", list_length(lst))
    print('list_append([1, 2, 3], 4):', list_append(lst.copy(), 4))
    print('list_remove([1, 2, 3], 2):', list_remove(lst.copy(), 2))
    print('list_slice([1, 2, 3, 4], 1, 3):', list_slice([1, 2, 3, 4], 1, 3))
    print('list_sort([3, 1, 2]):', list_sort([3, 1, 2].copy()))
    print('list_reverse([1, 2, 3]):', list_reverse([1, 2, 3].copy()))

    print("\nКортежи:")
    tpl = (1, 2, 3)
    print("tuple_sum((1, 2, 3)):", tuple_sum(tpl))
    print("tuple_length((1, 2, 3)):", tuple_length(tpl))
    print("tuple_unpack((1, 2, 3)):", tuple_unpack(tpl))
    print('tuple_concatenate((1, 2), (3, 4)):', tuple_concatenate((1, 2), (3, 4)))
    print('tuple_repeat((1, 2), 2):', tuple_repeat((1, 2), 2))
    print('tuple_count((1, 2, 2, 3), 2):', tuple_count((1, 2, 2, 3), 2))

    print("\nМножества:")
    s1 = {1, 2}
    s2 = {2, 3}
    print("set_union({1, 2}, {2, 3}):", set_union(s1, s2))
    print("set_intersection({1, 2}, {2, 3}):", set_intersection(s1, s2))
    print("set_difference({1, 2, 3}, {2}):", set_difference({1, 2, 3}, {2}))
    print("set_symmetric_difference({1, 2}, {2, 3}):", set_symmetric_difference({1, 2}, {2, 3}))
    print('set_add({1, 2}, 3):', set_add(s1.copy(), 3))
    print('set_remove({1, 2, 3}, 2):', set_remove({1, 2, 3}.copy(), 2))

    print("\nСловари:")
    d = {"a": 1, "b": 2}
    print('dict_keys({"a": 1, "b": 2}):', dict_keys(d))
    print('dict_values({"a": 1, "b": 2}):', dict_values(d))
    print('dict_items({"a": 1, "b": 2}):', dict_items(d))
    print('dict_get({"a": 1}, "b", 0):', dict_get({"a": 1}, "b", 0))
    print('dict_update({"a": 1}, {"b": 2}):', dict_update(d.copy(), {"b": 2}))
    print('dict_merge({"a": 1}, {"b": 2}):', dict_merge({"a": 1}, {"b": 2}))

    print("\nБулевы значения:")
    print("is_true(True):", is_true(True))
    print("is_false(False):", is_false(False))
    print("logical_and(True, False):", logical_and(True, False))
    print("logical_or(True, False):", logical_or(True, False))
    print("logical_not(True):", logical_not(True))

    print("\nNone:")
    print("is_none(None):", is_none(None))
    print("coalesce(None, 1):", coalesce(None, 1))

    print("\nКомплексные числа:")
    print("complex_add(1+2j, 3+4j):", complex_add(1+2j, 3+4j))
    print("complex_multiply(1+1j, 1+1j):", complex_multiply(1+1j, 1+1j))
    print("complex_conjugate(1+2j):", complex_conjugate(1+2j))
    print("complex_abs(3+4j):", complex_abs(3+4j))

    print("\nРабота с API:")
    try:
        api_data = get_api_data("https://jsonplaceholder.typicode.com/posts/1")
        print("get_api_data('https://jsonplaceholder.typicode.com/posts/1'):", api_data)
    except Exception as e:
        print("get_api_data error:", e)

    print("\nРабота с базой данных:")
    database = "example.db"
    conn = create_db_connection(database)
    if conn is not None:
        create_table(conn)
        project = ("Cool App", "2021-01-01", "2021-01-31")
        project_id = insert_project(conn, project)
        print("insert_project(conn, ('Cool App', '2021-01-01', '2021-01-31')):", project_id)
        projects = select_all_projects(conn)
        print("select_all_projects(conn):", projects)
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == "__main__":
    run_example()
