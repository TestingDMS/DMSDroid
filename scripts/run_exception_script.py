import os

Q_testing_dir = r"G:\QRS\result\qtesting"
Monkey_dir = r'G:\QRS\\result\Monkey'
comb_dir = r"G:\QRS\result\comb"
ses_dir = r"G:\QRS\result\ses1"
DIR = ses_dir


def get_SQtesting_Monkey_StoatCrashes(DIR):
    statics_exception_file = os.path.join(DIR, 'exception_result.txt')
    ret = {}
    for dir in os.listdir(DIR):
        if dir.endswith('sesout'):
            # process
            print(dir)
            file_path = os.path.join(os.path.join(DIR, dir), 'log.txt')
            exception_file = os.path.join(os.path.join(DIR, dir), 'exception.txt')
            exception_ret_file = os.path.join(os.path.join(DIR, dir), 'exception_ret.txt')

            # logcat
            exception_info = []
            with open(file_path, "r", encoding='UTF-8') as log_file:
                for line in log_file.readlines():
                    if 'Exception' in line.strip():
                        exception_info.append(line)
            with open(exception_file, 'w', encoding='utf-8') as ret_file:
                for line in exception_info:
                    ret_file.write(line)
                    ret_file.write("\n")

            pid_set = {}
            with open(exception_file, "r", encoding='UTF-8') as ret_file:
                for line in ret_file.readlines():
                    if len(line.strip()) > 31:
                        # if 'Exception' in line.strip():
                        if line.strip()[25:30] not in pid_set.keys():
                            pid_set.update({line.strip()[25:30]: [line.strip()]})
                        else:
                            pid_set[line.strip()[25:30]].append(line.strip())
            with open(exception_ret_file, 'w', encoding='utf-8') as ret_file:
                for key in pid_set.keys():
                    for line in pid_set[key]:
                        for words in line.split(" "):
                            if "Exception" in words:
                                if words not in ret.keys():
                                    ret.update({words: 1})
                                else:
                                    ret[words] += 1
                        ret_file.write(line)
                    ret_file.write("\n")
    with open(statics_exception_file, 'w', encoding='utf-8') as ret_file:
        for key in ret.keys():
            ret_file.write(key + " " + str(ret[key]))
            ret_file.write("\n")

def get_Sapienz(DIR):
    statics_exception_file = os.path.join(DIR, 'exception_result.txt')
    ret = {}
    for dir in os.listdir(DIR):
        if len(dir.split(".")) == 1:
            # process
            print(dir)
            file_path = os.path.join(os.path.join(DIR, dir), 'log.txt')
            exception_file = os.path.join(os.path.join(DIR, dir), 'exception.txt')
            exception_ret_file = os.path.join(os.path.join(DIR, dir), 'exception_ret.txt')

            # logcat
            exception_info = []
            with open(file_path, "r", encoding='UTF-8') as log_file:
                for line in log_file.readlines():
                    if 'Exception' in line.strip():
                        exception_info.append(line)
            with open(exception_file, 'w', encoding='utf-8') as ret_file:
                for line in exception_info:
                    ret_file.write(line)
                    ret_file.write("\n")
            pid_set = {}
            with open(exception_file, "r", encoding='UTF-8') as ret_file:
                for line in ret_file.readlines():
                  # if 'Exception' in line.strip():
                    if '(' in line.strip() and ')' in line.strip():
                         key = line[line.find('('):line.find(')')+1]
                         #print(key)
                         if key not in pid_set.keys():
                            pid_set.update({key: [line.strip()]})
                         else:
                            pid_set[key].append(line.strip())
            with open(exception_ret_file, 'w', encoding='utf-8') as ret_file:
                for key in pid_set.keys():
                    for line in pid_set[key]:
                        for words in line.split(":"):
                            if "Exception" in words:
                                if words not in ret.keys():
                                    ret.update({words: 1})
                                else:
                                    ret[words] += 1
                        ret_file.write(line)
                    ret_file.write("\n")
    ret_new = {}
    for key in ret.keys():
        if " " in key:
            for words in key.split(" "):
                if "Exception" in words:
                    if words in ret_new.keys():
                        ret_new[words] += ret[key]
                    else:
                        ret_new.update({words: ret[key]})
                    break
    with open(statics_exception_file, 'w', encoding='utf-8') as ret_file:
        for key in ret_new.keys():
            ret_file.write(key + " " + str(ret_new[key]))
            ret_file.write("\n")

#get_SQtesting_Monkey_StoatCrashes(SQ_testing_dir)
#get_SQtesting_Monkey_StoatCrashes(stoat_dir)
get_SQtesting_Monkey_StoatCrashes(DIR)
# get_Sapienz(Sapienz_dir)
