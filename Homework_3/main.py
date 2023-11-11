def list_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    diff_a_b = set(a) - set(b)
    diff_b_a = set(b) - set(a)
    return [intersection, union, diff_a_b, diff_b_a]


def char_count(text):
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def compare_dicts(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if len(dict1) != len(dict2):
            return False
        for key, value in dict1.items():
            if key not in dict2 or not compare_dicts(value, dict2[key]):
                return False
        return True
    elif isinstance(dict1, (list, set, tuple)) and isinstance(dict2, (list, set, tuple)):
        if len(dict1) != len(dict2):
            return False
        for item1, item2 in zip(dict1, dict2):
            if not compare_dicts(item1, item2):
                return False
        return True
    else:
        return dict1 == dict2


def build_xml_element(tag, content, **kwargs):
    attributes = " ".join([f'{key}="{value}"' for key, value in kwargs.items()])
    return f'<{tag} {attributes}>{content}</{tag}>'


def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if not value.startswith(prefix) or not value.endswith(suffix) or middle not in value:
                return False
    return True


def count_unique_and_duplicate_elements(lst):
    unique_set = set(lst)
    unique_count = len(unique_set)
    duplicate_count = len(lst) - unique_count
    return unique_count, duplicate_count


def set_operations(*sets):
    operations = {
        "|": lambda a, b: a | b,  # Union
        "&": lambda a, b: a & b,  # Intersection
        "-": lambda a, b: a - b,  # Difference A - B
    }

    result_dict = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            for op, operation_func in operations.items():
                key = f"{set1} {op} {set2}"
                result_dict[key] = operation_func(set1, set2)
    return result_dict


def loop(mapping):
    visited = set()
    current = mapping.get("start")
    result = []
    while current:
        if current in visited:
            break
        result.append(current)
        visited.add(current)
        current = mapping.get(current)
    return result


def count_positional_args(*args, **kwargs):
    return sum(1 for arg in args if arg in kwargs.values())


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = list_operations(list1, list2)
print(result)

text = "Ana has apples."
char_counts = char_count(text)
print(char_counts)

dict1 = {"a": 1, "b": [2, 3]}
dict2 = {"a": 1, "b": [2, 3]}
result = compare_dicts(dict1, dict2)
print(result)

dict1 = {"a": 1, "b": [2, 3]}
dict2 = {"a": 1, "b": [2, 3]}
result = compare_dicts(dict1, dict2)
print(result)

xml_element = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(xml_element)

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
result = validate_dict(rules, dictionary)
print(result)

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_count, duplicate_count = count_unique_and_duplicate_elements(my_list)
print(f"Unique count: {unique_count}, Duplicate count: {duplicate_count}")

set1 = {1, 2}
set2 = {2, 3}
result = set_operations(set1, set2)
print(result)

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping)
print(result)

result = count_positional_args(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
