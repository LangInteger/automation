 
import sys
import os
from datetime import datetime, timedelta
import markdown_to_json

def next_tuesday():
    today = datetime.today()
    next_tuesday = today + timedelta((1 - today.weekday()) % 7)
    return next_tuesday.strftime('%Y-%m-%d')

def process_input_string(input_string):
    changed_services = set()
    lines = input_string.split('\n')
    for line in lines:
        strip_line = line.strip()
        if strip_line.startswith("- [x]") and strip_line.endswith("service"):
            changed_services.add(strip_line.rsplit(None, 1)[-1])
    return changed_services

def merge_changes_to_file(input_string, directory, change):
    
    next_tuesday_date = next_tuesday()
    file_name = f'{next_tuesday_date}_changes.md'
    file_path = os.path.join(directory, file_name)
    print("file path is " + file_path)

    try:
        file = open(file_path, "x")
        file.close()
    except FileExistsError:
        print(f"The file '{file_path}' already exists.")
        
    service_changed = process_input_string(input_string)
    print("service changed: " + str(service_changed))
    with open(file_path, 'r+') as f:
        value = f.readlines()
        ast = markdown_to_json.CommonMark.DocParser().parse(value)
        dictionary = markdown_to_json.CMarkASTNester().nest(ast)
        print("already exist chagnes: " + dictionary)
        for service in service_changed:
            if service in dictionary:
                dictionary[service].append(change)
            else:
                dictionary[service] = [change]
        print("merged changes: " + str(dictionary))
        output_str = ""
        for key in sorted(dictionary.keys()):
            output_str += "# " + key + "\n"
            values_str = "\n".join(sorted(dictionary[key]))
            output_str += values_str + "\n"
        print("finally markdown: " + output_str)
        # Move the file pointer to the beginning of the file
        file.seek(0)
        f.write(output_str)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Usage: python script.py "input_string" "directory" "url" "title"')
        sys.exit(1)

    input_string = sys.argv[1]
    directory = sys.argv[2]
    pr_url = sys.argv[3]
    pr_title = sys.argv[4]

#     input_string = """
#     ### Summary
# What does this PR do?

# ### Does this close any open issues?
# Closes xx

# ### Screenshots
# Include any relevant screenshots here.

# ### Affected Services

# - [ ] demo_service
# - [x] a_service
# - [x] b_service

# ### Other Information
# Any other information that is important to this PR.
#     """
#     directory = "/Users/liulang/gitrepo/langinteger/automation"
#     pr_url = "https://api.github.com/repos/LangInteger/automation/pulls/9"
#     pr_title = "xx"

    last_slash_index = pr_url.rfind("/")
    pr_no = pr_url[last_slash_index + 1:]
    change = "- [{} {}]({})".format(pr_no, pr_title, pr_url)

    merge_changes_to_file(input_string, directory, change)