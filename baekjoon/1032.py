n_files = int(input())
first_name = input()
for i in range(n_files-1):
    file_name = input()
    for j in range(len(file_name)):
        if first_name[j] == file_name[j]:
            first_name = first_name.replace(first_name[j], file_name[j])
        else:
            first_name = first_name.replace(first_name[j], '?')


print(first_name)
# out = ""
