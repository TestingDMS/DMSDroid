import os
import subprocess
import time


def get_package_and_activity(apk_apth):
    package_cmd = 'aapt dump badging ' + apk_apth + ' | findstr package:'
    console_pipe = subprocess.Popen(package_cmd, shell=True, stdout=subprocess.PIPE)
    out, err = console_pipe.communicate()
    package_name = out.decode().strip().split(" ")[1].split("'")[1]

    activity_cmd = 'aapt dump badging ' + apk_apth + ' | findstr launchable-activity:'
    console_pipe = subprocess.Popen(activity_cmd, shell=True, stdout=subprocess.PIPE)
    out, err = console_pipe.communicate()
    if "7_" in apk_apth:
        activity_name = "org.isoron.uhabits/.activities.intro.IntroActivity"
    elif "9_" in apk_apth:
        activity_name = "org.tasks/net.openid.appauth.RedirectUriReceiverActivity"
    else:
        activity_name = out.decode().strip().split(" ")[1].split("'")[1]
    return package_name, activity_name

if __name__ == '__main__':
    apk_dir = r'G:\QRS\apks2'
    output_dir = r'G:\QRS\apks2'
    apk_list = os.listdir(apk_dir)
    apk_list.sort()
    for filename in apk_list:
        if len(filename.split(".")) == 2 and filename.split(".")[1] == "apk":
            apk_apth = apk_dir + '/' + filename
            droidbot_out = output_dir+'/'+filename.split(".")[0]
            package_name, activity_name = get_package_and_activity(apk_apth)

            outdir = output_dir + '/' + filename.split(".")[0] + "_sesout"
            if not os.path.exists(outdir):
                os.makedirs(outdir)
                print("creating ok")

            # os.system("adb reboot")
            time.sleep(10)
            # clean coverage.ec
            os.system("adb -s emulator-5554 shell rm /mnt/sdcard/coverage.ec")
            # uninstall apk
            os.system('adb -s emulator-5554 uninstall ' + package_name)
            # install apk
            os.system('adb -s emulator-5554 install ' + apk_apth)
            print("prepare work finish!")
            log_file = open(outdir + '/log.txt', 'w+')
            crash_file = open(outdir + '/crash.txt', 'w+')
            os.system('adb -s emulator-5554 logcat -c')
            save_pipe = subprocess.Popen(args='adb -s emulator-5554 logcat -v threadtime', stdin=None, stdout=log_file,
                                         stderr=crash_file, shell=True)
            os.system("adb -s emulator-5554 shell am start -n " + package_name + r"/" + activity_name)

            # start the Qtesting task
            sestesting_pipe = subprocess.Popen(
                args=f'droidbot -d emulator-5554 -a {apk_apth} -o {droidbot_out} -timeout 3600  -random -is_emulator',
                # stdin=subprocess.PIPE,
                # stdout=subprocess.PIPE,
                # stderr=subprocess.PIPE,
                shell=True,
                cwd=r'G:\QRS\result\ses'
            )

            # real time get coverage.ec file
            time_count = 0
            while time_count < 7200:
                time.sleep(60)
                # log = stoat_pipe.stdout.read()
                # stoat_pipe.stdout.close()
                # print(log.decode())
                os.system('adb -s emulator-5554 shell am broadcast -a edu.gatech.m3.emma.COLLECT_COVERAGE')
                os.system('adb -s emulator-5554 pull /data/data/' + package_name + r'/files/coverage.ec ' + outdir + '/' + str(
                    time_count) + '_coverage.ec')
                time_count = time_count + 60
                print("time explore: ", time_count)
            os.system('adb -s emulator-5554 pull /data/data/' + package_name + r'/files/coverage.ec ' + outdir + '/' + str(
                time_count) + '_coverage.ec')
            sestesting_pipe.terminate()
            sestesting_pipe.kill()
            save_pipe.terminate()
            save_pipe.kill()
            crash_file.close()
            log_file.close()
            # uninstall apk
            os.system('adb uninstall ' + package_name)