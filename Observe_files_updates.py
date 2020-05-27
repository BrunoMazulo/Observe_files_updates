import os
import win32file
import win32con
import pandas as pd

global contador
contador = 0

def atualizarsql():
  global contador
  if (contador == 3):
    print('Base no Servidor Atualizada!!')
    contador = 0

ACTIONS = {
  1 : "Updated"
}

FILE_LIST_DIRECTORY = 0x0001

path_to_watch = "."
hDir = win32file.CreateFile (
  path_to_watch,
  FILE_LIST_DIRECTORY,
  win32con.FILE_SHARE_READ,
  None,
  win32con.OPEN_EXISTING,
  win32con.FILE_FLAG_BACKUP_SEMANTICS,
  None
)

while 1:

  results = win32file.ReadDirectoryChangesW (
    hDir,
    1024,
    True,
     win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
     win32con.FILE_NOTIFY_CHANGE_SECURITY,
    None,
    None
  )
  for action, file in results:
    namepath = str(file)

  if "filename" in namepath:
    contador +=1
    atualizarsql()