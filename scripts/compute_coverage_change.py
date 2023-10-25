import csv
import os

Monkey_dir = 'G:\QRS\\result\Monkey'
Qtesting_dir = 'G:\QRS\\result\qtesting'
ses_dir = 'G:\QRS\\result\ses1'
ses2_dir = 'G:\QRS\\result\ses2'
comb_dir = 'G:\QRS\\result\comb'
DIR = ses2_dir
def read_txt_file(txtfile):
    with open(txtfile) as file:
        data = file.read()
        return data

def write_csv_file(data, csvfile, app_name):
    with open(csvfile, 'a', newline='') as file:
        rows = [[app_name] + line.split('% ') for line in data.splitlines()]
        writer = csv.writer(file)
        writer.writerows(rows)

if __name__ == '__main__':
    res_file = os.path.join('G:\QRS\\result\\ses2_c.csv')
    for apk_dir_name in os.listdir(DIR):
        if apk_dir_name.endswith('sesout'):
            app_dir = os.path.join(DIR, apk_dir_name)
            cresult_file = os.path.join(app_dir, 'cresult.txt')
            txt_data = read_txt_file(cresult_file)
            write_csv_file(txt_data, res_file, apk_dir_name)

