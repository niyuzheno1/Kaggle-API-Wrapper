import json
import zipfile
import os
import time
from subprocess import Popen, PIPE
def unzipall(ZipFiles):
  if ZipFiles is None:
    ZipFiles = os.listdir()
  for file in ZipFiles:
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall()
    zip_ref.close()
def DownloadCompetitionFromKaggle(competition_name):
  curpath = os.getcwd()
  dirpath = os.path.join("/content/gdrive/MyDrive/", competition_name) 
  if not os.path.isdir(dirpath):
    os.mkdir(dirpath)
  else:
    print("WARNING: the directory for our competition data has existed")
  cmds = "kaggle competitions download -c {}".format(competition_name)
  os.chdir(dirpath)
  os.system(cmds)
  os.chdir(curpath)
  return 
def WorkingFromKaggleDirectory(competition_name):
  dirpath = os.path.join("/content/gdrive/MyDrive/", competition_name) 
  os.chdir(dirpath)
  return "Success"
def SubmitToKaggleCompetition(competition_name, list_of_file, message ):
  lfiles = ' '.join(list_of_file)
  cmds = "kaggle competitions submit -c  {} -f {} -m {}".format(competition_name, lfiles, message)
  os.system(cmds)
  return "Success"
def ShowAllCompetitions():
  print(os.popen('kaggle competitions list').read())

def ShowHistoryOfSubmission(competition_name):
  cmds = "kaggle competitions submissions -c {}".format(competition_name)
  print(os.popen(cmds).read())

def SubmitAndReveal(competition_name, list_of_file, message):
  SubmitToKaggleCompetition(competition_name, list_of_file, message)
  time.sleep(1)
  ShowHistoryOfSubmission(competition_name)

def ListDataSetByKeyword(keyword):
  command = ['kaggle', 'datasets', 'list', '-s', "\"{}\"".format(keyword)]
  with Popen(command,
           stdout=PIPE, stderr=PIPE) as p:
    output, errors = p.communicate()
  lines = output.decode('utf-8' , errors='ignore').splitlines()
  print("\n".join(lines))

def DownloadDataset(dataset, namedir):
  curpath = os.getcwd()
  dirpath = os.path.join("/content/gdrive/MyDrive/", namedir) 
  if namedir is not None and not os.path.isdir(dirpath):
    os.mkdir(dirpath)
  else:
    print("WARNING: the directory for our dataset has existed or no input has been made")
  cmds = "kaggle datasets download -d {}".format(dataset)
  os.chdir(dirpath)
  os.system(cmds)
  os.chdir(curpath)
  return 
def CreateNewDataSet(dataset):
  curpath = os.getcwd()
  dirpath = os.path.join("/content/gdrive/MyDrive/", dataset) 
  print("Visit https://github.com/Kaggle/kaggle-api/wiki/Dataset-Metadata")
  if dataset is not None and not os.path.isdir(dirpath):
    os.mkdir(dirpath)
  else:
    print("WARNING: the directory for our dataset has existed or no input has been made")
    if dataset is None:
      print("SORRY your requests won't be processed further")
      return
    if os.path.isfile(os.path.join(dirpath, "dataset-metadata.json")):
      print("SORRY your requests won't be processed further")
      return
  cmds = "kaggle datasets init -p {}".format(dirpath)
  os.chdir(dirpath)
  os.system(cmds)
  os.chdir(curpath)
  print("")
  return 
def CreateNewDataSetOnline(dataset):
  curpath = os.getcwd()
  dirpath = os.path.join("/content/gdrive/MyDrive/", dataset) 
  if not os.path.isfile(os.path.join(dirpath, "dataset-metadata.json")):
    print("SORRY your requests won't be processed further")
    return
  print(dirpath)
  cmds = "kaggle datasets create -p {}".format(dirpath)
  os.chdir(dirpath)
  print(os.popen(cmds).read())
  os.chdir(curpath)
  print("")
  return 
def RenewDataSetOnline(dataset, message):
  curpath = os.getcwd()
  dirpath = os.path.join("/content/gdrive/MyDrive/", dataset) 
  if not os.path.isfile(os.path.join(dirpath, "dataset-metadata.json")):
    print("SORRY your requests won't be processed further")
    return
  print(dirpath)
  cmds = "kaggle datasets version -p {} -m \"{}\"".format(dirpath, message)
  os.chdir(dirpath)
 
  print(os.popen(cmds).read())
  os.chdir(curpath)
  print("")
  return 
def ListNotebookByKeyword(keyword):
  command = ['kaggle', 'kernels', 'list', '-s', "\"{}\"".format(keyword)]
  with Popen(command,
           stdout=PIPE, stderr=PIPE) as p:
    output, errors = p.communicate()
  lines = output.decode('utf-8' , errors='ignore').splitlines()
  print("\n".join(lines))
def DownloadANotebook(kernel, namedir):
  curpath = os.getcwd()
  dirpath = os.path.join("/content/gdrive/MyDrive/", namedir) 
  if namedir is not None and not os.path.isdir(dirpath):
    os.mkdir(dirpath)
  else:
    print("WARNING: the directory for our dataset has existed or no input has been made")
  print(dirpath)
  return
  cmds = "kaggle kernels pull -k {} -p {}".format(dataset, dirpath)
  os.chdir(dirpath)
  os.system(cmds)
  os.chdir(curpath)
  return 
