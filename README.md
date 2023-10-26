# DmsDroid Prototype
DmsDroid is an automated testing tool based on reinforcement learning and data manipulations to find deep-hidden bugs in Android apps. DmsDroid leverages extracting data manipulations functions from the app under test and using funvtional semantics of data manipulations sequence in execution trace to guide the test exploration which can improve the testing effectiveness in bug finding.So far, DmsDroid has found 7 previously unknown bugs, all of which have been confirmed by the app developers and five have already been fixed.

# Update
All the source code of DmsDroid is also publicly available for facilitating the development of automated testing. 

# Getting Started
## Virtual Machine Requirements
* Python: 3.8
* Android SDK: API 23 (make sure adb and aapt commands are available)
* Linux: Ubantu 16.04
* [UiAutomator2](https://github.com/openatx/uiautomator2): 2.16.3 (pip install uiautomator2== 2.16.3)
## Android Emulator (AVD) Requirements
* System images: Android 7.0 x86_64 (Marshmallow)
* RAM: 2048M
* SD card: 512M

The above version of the software has been tested in our experiment and can run successfully. In addition, please start the emulator before running DmsDroid (you can see this [link](https://stackoverflow.com/questions/43275238/how-to-set-system-images-path-when-creating-an-android-avd) for how to creating and using [avdmanager](https://developer.android.com/studio/command-line/avdmanager)). 

<!-- ## Subject Requirements([video tutorial](https://1drv.ms/u/s!AhrQLCaSmZgwamuImvbWUv_1pek?e=fiWDdt))
IccDroid can test both on open-source and closed-source apps:
* Closed-source apps: the users can directly run “python main.py apk_path” to test the apk.
* Open-source apps: If users want to obtain code coverage and dataflow information, the app under test should be instrumented with [plugins/Jacoco](https://github.com/androidAppGuard/IccDroid/tree/main/plugins/jacoco) and [plugins/dataflow/DataFlowAnalysis.java](https://github.com/androidAppGuard/IccDroid/tree/main/plugins/dataflow) files first, and built as an apk file. Then users can run “python main.py apk_path” to test the apk (the detailed process is in the [video tutorial](https://1drv.ms/u/s!AhrQLCaSmZgwamuImvbWUv_1pek?e=fiWDdt)).  -->

## Settings
Before running DmsDroid, please update the [configure.py](https://github.com/androidAppGuard/IccDroid/blob/main/IccDroid/configure.py) as follows:
```python
  # Dataflow Server info
  SERVER_HOST = "127.0.0.1"
  SERVER_PORT = 9999

  # Device info
  DEVICE_ID = "emulator-5554"
  DEVICE_SCREEN_HEIGHT = 1920
  DEVICE_SCREEN_WIDTH = 1020

  # Time Setting(s)
  STAGE_ONE_TIME = 3600 # (Graph Enhancement Exploration time)
  STAGE_TWO_TIME = 3600 # (ICC-Guided Exploration time)

```
Other configuration information of the configure.py can be selected according to user customization or default configuration.

## Running
For applications that require permission or login, you should install apk on the emulator and grant the permissions or login the account begore testing. Then you start IccDroid by:
```shell
  # enter workspace of IccDroid
  cd /opt/IccDroid 
  # start testing
  python main.py apk_path
```
## Output
The output contents are placed in folder ``<apk_dir>/<apk_name>`` and contain coverage and log directory:
* coverage -- These files in the folder are used to calculate the final code coverage. (code coverage is recorded every 2 seconds)

* log -- The folder contains two types of files:
	* crash_event_X: record the event sequence triggered the ``crash X``. 
	* crash_log_X: record the exception stack log of crash ``crash X``.

# Detailed Description
In order to better reproduce IccDroid, we provide the app’s ``Link``, ``Version``, ``Strategy`` and the revealed bugs.
## 12 Real-world Target Apps
| APK Name              | Executable Lines of Codes | Version                 | Catagory  |GIthub Link|
|-----------------------|---------------------------|-------------------------|-----------|---|
| Book catalogues       | 75241                     | v5.1.0                  | Education | <https://github.com/eleybourn/Book-Catalogue> |
| Amaze File Manager    | 60325                     | v3.8.5                  | Tool      | <https://github.com/TeamAmaze/AmazeFileManager> |
| K9 Mail               | 93455                     | v6.4                    | Sociality | <https://github.com/thundernest/k-9> |
| AnyMemo               | 30661                     | v10.11.7                | Education | <https://github.com/helloworld1/AnyMemo> |
| Budget Watch          | 9863                      | v0.21.5                 | Finance   | <https://github.com/brarcher/budget-watch> |
| Catima Loyalty        | 11547                     | v2.21.2                 | Finance   | <https://github.com/CatimaLoyalty/Android> |
| Uhabits               | 10296                     | v2.1.1                  | Record    | <https://github.com/iSoron/uhabits> |
| Runnerup              | 40001                     | v2.5.0.7                | Health    | <https://github.com/jonasoreland/runnerup> |
| Track and Graph       | 16991                     | v3.0.1                  | Health    | <https://github.com/SamAmco/track-and-graph> |
| PhonographPlus        | 43261                     | v0.6.3                  | Music     | <https://github.com/chr56/Phonograph_Plus> |
| GrowTracker           | 15339                     | v3                      | Record    | <https://github.com/7LPdWcaW/GrowTracker-Android> |
| Notally               | 1559                      | v5.2                    | Music     | <https://github.com/OmGodse/Notally> |


## Revealed Bugs
| APK Name           | Issue State | Cause | Details |
|--------------------|-------------|---|---|
| GrowTracker        | Confirmed   | IndexoutOfbound | <https://github.com/7LPdWcaW/GrowTracker-Android/issues/266> |
| AnyMemo            | Waiting     | NullPointer | https://github.com/helloworld1/AnyMemo/issues/532 |
| K9 Mail            | Fixed       | com.fsck.k9.preferences.SettingsImportExportException | <https://github.com/thundernest/k-9/issues/7154> |
| Uhabits            | Fixed       | ClassNotFoundException | <https://github.com/iSoron/uhabits/issues/1758> |
| PhonographPlus     | Fixed       | IllegalArgumentException | <https://github.com/chr56/Phonograph_Plus/issues/95> |
| Track and Graph    | Fixed       | ConcurrentModificationException | <https://github.com/SamAmco/track-and-graph/issues/227> |
| Amaze File Manager | Confirmed   | StringIndexOutOfBoundsException | <https://github.com/TeamAmaze/AmazeFileManager/issues/3885> |
| Amaze File Manager | Fixed       | NullPointerException | <https://github.com/TeamAmaze/AmazeFileManager/issues/3886> |

Our survey is available on ：https://docs.google.com/spreadsheets/d/1UaH4rHI-q57wxs6ZY4yd80ruaTdfFsKWt0nhmoxJukE/edit?pli=1#gid=255339191
