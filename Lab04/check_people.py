def identify_access():
    import os, os.path
    cwd = os.getcwd()
    dir = cwd + "/Departments"
    path = dir
    room_list = []
    name_list = []
    each_name = []
    name_dict = {}
    department_files = os.listdir(path)
    for filename in department_files:
        dir = dir + "/" + filename
        file_list = []
        file_temp = filename.strip('.txt')
        room_list.append(file_temp)
        with open(dir,'r') as file:
            dir = cwd + "/Departments"
            all_lines = file.readlines()
            for line in all_lines:
                line_string = line
                line_string = line_string.strip('\n')
                file_list.append(line_string)
            name_list.append(file_list)


    #print(file_list)
    #print(name_list)    # a list of lists containing each name where each index is a room
    #print(room_list)    # each room
    """
    ######################################

    i = 0
    while i < len(name_list):
        j = 0
        while j < len(name_list[i]):
            if name_list[i][j] not in each_name:
                each_name.append(name_list[i][j])
            j += 1
        i += 1

    #######################################
    """

    for i in range(0, len(name_list)):
        for j in range(0, len(name_list[i])):
            if name_list[i][j] not in each_name:
                each_name.append(name_list[i][j])


    cor_room = []
    temp_room = []
    #print(each_name)


    for name in each_name:
        for i in range(0,len(name_list)):
            for j in range(0,len(name_list[i])):
                if name in name_list[i][j] and room_list[i] not in temp_room:
                    temp_room.append(room_list[i])
        cor_room.append(temp_room)
        temp_room = []

    #print(temp_room)


    for i in range(0, len(each_name)):
        cor_room[i] = sorted(cor_room[i])
        name_dict[each_name[i]] = cor_room[i]

    #print(name_dict)
    return(name_dict)

#identify_access()


def get_common(name1, name2):
    info = identify_access()
    if name1 not in info:
        return None
    if name2 not in info:
        return None

    name1_list = info[name1]
    name2_list = info[name2]
    common_list = []

    for i in range(0, len(name1_list)):
        for j in range(0, len(name2_list)):
            if name1_list[i] == name2_list[j]:
                if name1_list[i] not in common_list:
                    common_list.append(name1_list[i])


    common_list = sorted(common_list)

    #print(name1_list)
    #print(name2_list)
    print(common_list)
    common_set = set(common_list)
    return common_set


#get_common('Zenaida Blaisdell', 'Neomi Flournoy')

