import re
import os
import subprocess

Q_testing_dir = r"G:\QRS\result\qtesting"
Monkey_dir = r'G:\QRS\\result\Monkey'
comb_dir = r"G:\QRS\result\comb"
ses2_dir = r"G:\QRS\result\ses2"
DIR = ses2_dir

package_dict = {
    '1': 'com.eleybourn.bookcatalogue',
    '2': 'com.amaze.filemanager',
    '3': 'com.fsck.k9.debug',
    '4': 'protect.budgetwatch',
    '5': 'org.runnerup.debug',
    '6': 'org.liberty.android.fantastischmemodev',
    '7': 'org.isoron.uhabits',
    '8': 'me.hackerchick.catima.debug',
    '9': 'org.tasks',
    '10': 'dev.corruptedark.diditakemymeds',
    '11': 'com.samco.trackandgraph.debug',
    '12': 'player.phonograph.plus.checkout.debug',
    '13': 'me.anon.grow.debug',
    '14': 'com.omgodse.notally.debug'
}

def get_SQtesting_Monkey_StoatCrashes(DIR):
    for dir in os.listdir(DIR):
        if dir.endswith('sesout'):
            # process
            print(dir)
            file_path = os.path.join(os.path.join(DIR, dir), 'log.txt')
            crash_file = os.path.join(os.path.join(DIR, dir), 'crash.txt')
            crash_ret_file = os.path.join(os.path.join(DIR, dir), 'crash_pid.txt')
            crash_final_file = os.path.join(os.path.join(DIR, dir), 'crash_ret.txt')
            package_name = package_dict[dir.split("_")[0]]

            # logcat
            crash_info = []
            with open(file_path, "r", encoding='UTF-8') as log_file:
                for line in log_file.readlines():
                    if package_name in line.strip():
                        crash_info.append(line)
            with open(crash_file, 'w', encoding='utf-8') as ret_file:
                for line in crash_info:
                    ret_file.write(line)
                    ret_file.write("\n")
            pid_set = {}
            with open(crash_file, "r", encoding='UTF-8') as ret_file:
                for line in ret_file.readlines():
                    if len(line.strip()) > 52 :
                        # if 'Exception' in line.strip():
                        if line.strip()[33:51] not in pid_set.keys():
                            pid_set.update({line.strip()[33:51]: [line.strip()]})
                        else:
                            pid_set[line.strip()[33:51]].append(line.strip())
            with open(crash_ret_file, 'w', encoding='utf-8') as ret_file:
                for key in pid_set.keys():
                    for line in pid_set[key]:
                        ret_file.write(line)
                    ret_file.write("\n")

            # filter no Error
            array_info = []
            with open(crash_ret_file, "r", encoding='UTF-8') as log_file:
                for line in log_file.readlines():
                    # if re.match(r"^\d{2}-\d{2} (\d{2}:){2}\d{2}.\d{3}([ ]{1,} \d{1,}){2}[ ]{1,}E",line.strip()):
                    if len(line.strip()) > 32 and line.strip()[31] == "E":
                        array_info.append(line)
            with open(crash_final_file, 'w', encoding='utf-8') as ret_file:
                for line in array_info:
                    ret_file.write(line)
                    ret_file.write("\n")

def get_sapienz(DIR):
    for dir in os.listdir(DIR):
        if len(dir.split(".")) == 1:
            # process
            print(dir)
            file_path = os.path.join(os.path.join(DIR, dir), 'log.txt')
            crash_file = os.path.join(os.path.join(DIR, dir), 'crash.txt')
            crash_ret_file = os.path.join(os.path.join(DIR, dir), 'crash_pid.txt')
            crash_final_file = os.path.join(os.path.join(DIR, dir), 'crash_ret.txt')
            package_name = package_dict[dir.split("_")[0]]

            # logcat
            crash_info = []
            with open(file_path, "r", encoding='UTF-8') as log_file:
                for line in log_file.readlines():
                    if package_name in line.strip():
                        crash_info.append(line)
            with open(crash_file, 'w', encoding='utf-8') as ret_file:
                for line in crash_info:
                    ret_file.write(line)
                    ret_file.write("\n")
            pid_set = {}
            with open(crash_file, "r", encoding='UTF-8') as ret_file:
                for line in ret_file.readlines():
                    if len(line.strip()) > 52 :
                        # if 'Exception' in line.strip():
                        if line.strip()[2:10] not in pid_set.keys():
                            pid_set.update({line.strip()[2:10]: [line.strip()]})
                        else:
                            pid_set[line.strip()[2:10]].append(line.strip())
            with open(crash_ret_file, 'w', encoding='utf-8') as ret_file:
                for key in pid_set.keys():
                    for line in pid_set[key]:
                        ret_file.write(line)
                    ret_file.write("\n")

            array_info = []
            with open(crash_ret_file, "r", encoding='UTF-8') as log_file:
                for line in log_file.readlines():
                    # if re.match(r"^\d{2}-\d{2} (\d{2}:){2}\d{2}.\d{3}([ ]{1,} \d{1,}){2}[ ]{1,}E",line.strip()):
                    if len(line.strip()) > 1 and line.strip()[0] == "E":
                        array_info.append(line)
            with open(crash_final_file, 'w', encoding='utf-8') as ret_file:
                for line in array_info:
                    ret_file.write(line)
                    ret_file.write("\n")
#get_SQtesting_Monkey_StoatCrashes(DIR)
# get_sapienz(DIR)

# def Sapienz(DIR):
#     for dir in os.listdir(DIR):
#         if len(dir.split(".")) == 1:
#             # process
#             file_path = os.path.join(os.path.join(DIR, dir), 'logcat.txt')
#             crash_file = os.path.join(os.path.join(DIR, dir), 'crash.txt')
#             crash_ret_file = os.path.join(os.path.join(DIR, dir), 'crash_ret.txt')
#
#             pid_set = {}
#             print(file_path)
#             with open(file_path, "r", encoding='UTF-8') as log_file:
#                 for line in log_file.readlines():
#                     # if re.match(r"^\d{2}-\d{2} (\d{2}:){2}\d{2}.\d{3}([ ]{1,} \d{1,}){2}[ ]{1,}E",line.strip()):
#                     if len(line.strip()) > 1 and line.strip()[0] == "E":
#                         # if 'Exception' in line.strip():
#                         if line.strip()[2:17] not in pid_set.keys():
#                             pid_set.update({line.strip()[2:17]: [line.strip()]})
#                         else:
#                             pid_set[line.strip()[2:17]].append(line.strip())
#
#                 with open(crash_file, 'w', encoding='utf-8') as ret_file:
#                     for key in pid_set.keys():
#                         for line in pid_set[key]:
#                             ret_file.write(line)
#                         ret_file.write("\n")
#
#                 crash_dict = {}
#                 with open(crash_file, "r", encoding='UTF-8') as ret_file:
#                     for line in ret_file.readlines():
#                         key_array = line.strip()[2:10]
#                         key_str = ""
#                         for elem in key_array:
#                             key_str += elem
#                         if key_str not in crash_dict.keys():
#                             crash_dict.update({key_str: line})
#                 with open(crash_ret_file, 'w', encoding='utf-8') as ret_file:
#                     for key in crash_dict.keys():
#                         for line in crash_dict[key]:
#                             ret_file.write(line)
#                         ret_file.write("\n")
#
#
# def SQ_testing_Monkey_Stoat(DIR):
#     for dir in os.listdir(DIR):
#         if len(dir.split(".")) == 1:
#             # process
#             file_path = os.path.join(os.path.join(DIR, dir), 'logcat.txt')
#             crash_file = os.path.join(os.path.join(DIR, dir), 'crash.txt')
#             crash_ret_file = os.path.join(os.path.join(DIR, dir), 'crash_ret.txt')
#
#             pid_set = {}
#             print(file_path)
#             with open(file_path, "r", encoding='UTF-8') as log_file:
#                 for line in log_file.readlines():
#                     # if re.match(r"^\d{2}-\d{2} (\d{2}:){2}\d{2}.\d{3}([ ]{1,} \d{1,}){2}[ ]{1,}E",line.strip()):
#                     if len(line.strip()) > 32 and line.strip()[31] == "E":
#                         # if 'Exception' in line.strip():
#                         if line.strip()[25:31] not in pid_set.keys():
#                             pid_set.update({line.strip()[25:31]: [line.strip()]})
#                         else:
#                             pid_set[line.strip()[25:31]].append(line.strip())
#
#                 with open(crash_file, 'w', encoding='utf-8') as ret_file:
#                     for key in pid_set.keys():
#                         for line in pid_set[key]:
#                             ret_file.write(line)
#                         ret_file.write("\n")
#
#                 crash_dict = {}
#                 with open(crash_file, "r", encoding='UTF-8') as ret_file:
#                     for line in ret_file.readlines():
#                         key_array = line.strip()[33:51]
#                         key_str = ""
#                         for elem in key_array:
#                             key_str += elem
#                         if key_str not in crash_dict.keys():
#                             crash_dict.update({key_str: line})
#                 with open(crash_ret_file, 'w', encoding='utf-8') as ret_file:
#                     for key in crash_dict.keys():
#                         for line in crash_dict[key]:
#                             ret_file.write(line)
#                         ret_file.write("\n")
get_SQtesting_Monkey_StoatCrashes(DIR)

