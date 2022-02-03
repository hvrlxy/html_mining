import pandas as pd


def find_keys_name(strings_dict, orig_name):
    if orig_name not in strings_dict.keys():
        return orig_name
    count = 1
    name = orig_name
    while name in strings_dict.keys():
        name = orig_name + str(count)
        count += 1
    return name

def extract_strings(head):
    strings_dict = {}

    def recursive_string(node):
        if node.name is None:
            return
        if node.string is not None and node.string.strip() != '':
            if node.has_attr('class'):
                strings_dict[find_keys_name(strings_dict, node['class'][0])] = node.string
                return
            else:
                strings_dict[find_keys_name(strings_dict, node.name)] = node.string
                return

        children = [child for child in node.contents if child != '\n' and child.name is not None]
        for child in children:
            recursive_string(child)

    recursive_string(head)
    return strings_dict

def convert_to_df(items_list):
    if len(extract_strings(items_list[0]).keys()) < 2:
        return None
    data_dict = [extract_strings(item) for item in items_list]
    data_df = pd.DataFrame(data_dict)
    return data_df

def convert_all_df(items_dict):
    df_dict = {}
    for name in items_dict.keys():
        print(name)
        convert_df = convert_to_df(items_dict[name])
        if convert_df is not None:
            print(name)
            df_dict[name] = convert_df

    return df_dict

def convert_to_excel(df_dict, file_name):
    writer = pd.ExcelWriter(file_name)
    for df_name in df_dict.keys():
        new_name = df_name.replace('[', '').replace(']', '')[:30]
        df_dict[df_name].to_excel(writer, new_name)

    writer.save()





