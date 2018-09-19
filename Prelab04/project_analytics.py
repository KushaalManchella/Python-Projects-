def get_component_count_by_project(project_id):
    import os
    with open('projects.txt','r') as projects:
        all_lines = projects.readlines()
        Resistors = []
        Inductors = []
        Capacitors = []
        Transistors = []
        ID_count = 0

        for line in all_lines:
            if project_id in line:     # Kind of sketchy.. Change later :
                ID_count += 1
                line_string = line
                list = line_string.split()
                #print(list[0])
                circuit_file = "circuit_"+list[0]+".txt"
                list_cir = circuit_file.split('\n')
                cwd = os.getcwd()
                circuit_dir = cwd + "/Circuits"
                #print(list_cir)
                #print(circuit_file)

                for circuit in list_cir:
                    circuit_dir = circuit_dir + "/" + circuit
                    with open(circuit_dir,'r') as circuits:
                        all_lines = circuits.readlines()
                        count = 0

                        for line in all_lines:
                            components = line.split(',')
                            if count == 1:
                                for i in components:
                                    if "R" in i and i not in Resistors:
                                        Resistors.append(i)
                                    elif "L" in i and i not in Inductors:
                                        Inductors.append(i)
                                    elif "C" in i and i not in Capacitors:
                                        Capacitors.append(i)
                                    elif "T" in i and i not in Transistors:
                                        Transistors.append(i)
                                break
                            if "Components:" in line:
                                count += 1
        if ID_count == 0:
            return None


    components = (len(Resistors),len(Inductors),len(Capacitors),len(Transistors))
    #print(components)
    return(components)

get_component_count_by_project("082D6241-40EE-432E-A635-65EA8AA374B6")

def get_component_count_by_student(student_name):
    import os, os.path
    cwd = os.getcwd()
    circuit_dir = cwd + "/Circuits"
    Resistors = []
    Inductors = []
    Capacitors = []
    Transistors = []
    student_check = 0
    with open('students.txt','r') as students:
        all_lines = students.readlines()
        count = 0
        student_id = -1
        for line in all_lines:
            count += 1
            if count > 2:
                line_string = line
                line_string = line_string.strip()
                student_list = line_string.split('|')
                #student_list[1] = student_list[1].split()
                #print(student_list)
                if student_name in student_list[0]:
                    #print(student_list[0])
                    student_id = student_list[1]
                    student_id = student_id.strip()
        path = circuit_dir
        circuit_files = os.listdir(path)
        for file in circuit_files:
            circuit_dir = circuit_dir + "/" + file
            with open(circuit_dir,'r') as file:
                circuit_dir = cwd + "/Circuits"
                all_lines = file.readlines()
                count = 0
                for line in all_lines:
                    count += 1
                    line_string = line
                    if count == 2:
                        line_string = line_string.strip('\n')
                        line_list = line_string.split(',')
                        i = 0
                        while i < len(line_list):
                            if student_id in line_list[i]:
                                #print(line_list)
                                #print(student_id)
                                student_check = 1
                            i += 1
                    if count == 5 and student_check == 1:
                        components = line.split(',')
                        #print(components)
                        for i in components:
                            if "R" in i and i not in Resistors:
                                Resistors.append(i)
                            elif "L" in i and i not in Inductors:
                                 Inductors.append(i)
                            elif "C" in i and i not in Capacitors:
                                Capacitors.append(i)
                            elif "T" in i and i not in Transistors:
                                Transistors.append(i)
                        student_check = 0

        if student_id == -1:
            return None
        components = (len(Resistors),len(Inductors),len(Capacitors),len(Transistors))
        #print(components)
        return(components)







#get_component_count_by_student("Alexander, Carlos")



def get_participation_by_student(student_name):
    import os, os.path
    cwd = os.getcwd()
    circuit_list = []
    project_list = []
    circuit_dir = cwd + "/Circuits"
    num_projects = 0
    # getting student id
    with open('students.txt','r') as students:
        all_lines = students.readlines()
        count = 0
        student_id = -1
        for line in all_lines:
            count += 1
            if count > 2:
                line_string = line
                line_string = line_string.strip()
                student_list = line_string.split('|')
                #print(student_list)
                if student_name in student_list[0]:
                    #print(student_list[0])
                    student_id = student_list[1]
                    student_id = student_id.strip()
    path = circuit_dir
    circuit_files = os.listdir(path)
    for filename in circuit_files:
        circuit_dir = circuit_dir + "/" + filename
        with open(circuit_dir,'r') as file:
            circuit_dir = cwd + "/Circuits"
            all_lines = file.readlines()
            count = 0
            for line in all_lines:
                count += 1
                if count == 2:
                    line= line.strip('\n')
                    line_list = line.split(',')
                    i = 0
                    while i < len(line_list):
                        if student_id in line_list[i]:
                            filename_temp = filename
                            filename_temp = filename_temp.strip("circuit_")
                            filename_temp = filename_temp.strip(".txt")
                            if filename_temp not in circuit_list:
                                circuit_list.append(filename_temp)
                        i += 1
    with open('projects.txt','r') as projects:
        all_lines = projects.readlines()
        count = 0
        for line in all_lines:
            count += 1
            if count > 3:
                line_string = line
                line_list = line_string.split()
                i = 0
                while i < len(circuit_list):
                    if circuit_list[i] == line_list[0]:
                        if line_list[1] not in project_list:
                            project_list.append(line_list[1])
                    i += 1

    #print(circuit_list)
    project_set = set(project_list)
    #print(project_set)
    return(project_set)


#get_participation_by_student("Alexander, Carlos")


def get_participation_by_project(project_id):
    import os, os.path
    cwd = os.getcwd()
    circuit_list = []
    id_list = []
    name_list = []
    # Go through projects.txt to get circuits in all of that projects
    with open('projects.txt','r') as projects:
        all_lines = projects.readlines()
        count = 0
        for line in all_lines:
            count += 1
            if count > 2:
                line_string = line
                line_list = line_string.split()
                if project_id == line_list[1]:
                    circuit_string = "circuit_" + line_list[0] +".txt"
                    circuit_list.append(circuit_string)
    i = 0
    # go through all circuits and take ids
    while i < len(circuit_list):
        circuit_dir = cwd + "/Circuits" + "/" + circuit_list[i]
        with open(circuit_dir,'r') as circuit_file:
            all_lines = circuit_file.readlines()
            count = 0
            for line in all_lines:
                count += 1
                if count == 2:
                    string = line

                    line_list = string.split(',')
                    for id in line_list:
                        if id not in id_list:
                            id = id.strip('\n')
                            id_list.append(id)
        i += 1
    # convert ids to names
    with open('students.txt','r') as students:
        all_lines = students.readlines()
        count = 0
        for line in all_lines:
            count += 1
            if count > 2:
                line_string = line
                line_string = line_string.strip()
                student_list = line_string.split('|')
                for id in id_list:
                    if id in student_list[1]:
                        name = student_list[0]
                        name = name.strip()
                        temp_list = name.split(',')
                        name = temp_list[0] + "," + temp_list[1]
                        name_list.append(name)


                #print(student_list)
                #print(line_list)



    name_set = set(name_list)
    #print(name_set)
    return(name_set)
    #print(line_list)
    #print(circuit_list)
    #print(id_list)



#get_participation_by_project("17A946D3-A1B0-4335-8808-8594D9FBD62C")

def get_project_by_component(components):
    component_list = list(components)
    circuit_list = []
    project_list = []

    i = 0
    while i < len(component_list):
        circuit_list.append([])
        project_list.append([])
        i += 1
    #print(project_list)
    proj_dict = {}
    #print(component_list)

    import os, os.path
    cwd = os.getcwd()
    circuit_dir = cwd + "/Circuits"
    path = circuit_dir
    circuit_files = os.listdir(path)
    for filename in circuit_files:
        circuit_dir = circuit_dir + "/" + filename
        with open(circuit_dir,'r') as file:
            circuit_dir = cwd + "/Circuits"
            all_lines = file.readlines()
            included = 0
            index = 0
            for comp in component_list:
                count = 0
                temp_string = ""
                for line in all_lines:
                    count += 1
                    if count == 5:
                        line_string = line
                        line_list = line_string.split(',')
                        i = 0
                        while i < len(line_list):
                            if comp in line_list[i]:
                                string = filename
                                string = string.strip("circuit_")
                                string = string.strip(".txt")
                                circuit_list[index].append(string)
                            i += 1
                index += 1





    with open('projects.txt','r') as projects:
        all_lines = projects.readlines()
        count = 0
        for line in all_lines:
            count += 1
            if count > 2:
                line_string = line
                line_list = line_string.split()
                ind1 = 0
                while ind1 < len(circuit_list):
                    ind2 = 0
                    while ind2 < len(circuit_list[ind1]):
                        if circuit_list[ind1][ind2] == line_list[0] and line_list[1] not in project_list[ind1]:
                            project_list[ind1].append(line_list[1])
                        ind2 += 1
                    ind1 += 1



        i = 0
        while i < len(component_list):
            proj_dict.update({ component_list[i]: set(project_list[i]) })
            i += 1



    #print(proj_dict)
    return(proj_dict)

#get_project_by_component({"T71.386","C407.660"})


#def get_student_by_component(components):
