# Copyright (C) 2014 Ninbora [admin@ninbora.com]
# Licensed under MIT license [http://opensource.org/licenses/MIT]

class StringeManager:
  def __init__(self):
    self.addon = None
    # info
    self.seriesStart  =  1001 # Load Series Started
    self.seriesEnd    =  1002 # Added {0}/{1}.Load Series Ended
    self.episodeStart =  1003 # Load Episode Started
    self.episodeEnd   =  1004 # Added {0}/{1}. Load Episode Ended
    self.bundlesStart =  1005 # Load Bundles Start
    self.bundlesEnd   =  1006 # Added {0}/{1}. Load Bundles Ended
    self.packageStart =  1007 # Load Package Started
    self.packageEnd   =  1008 # Added {0}/{1}. Load Package Ended
    self.cleanLibrary =  1009 # Clean Library
    self.cleanCache   =  1010 # Clean Cache
    self.cleanLogs    =  1011 # Clean Logs
  def str(self,stringId):
    ss = self.addon.getLocalizedString(stringId)
    ss = ss.replace("\\n",'\n')
    return ss

sm = StringeManager()

# Convert to strings.xml :
#   Replace ".*?=[ ]*(\d+) # (.*)" with "  <string id="\1">\2</string>"
#   Replace ".*?#[ ]+(.*)"         with "  <!-- \1 -->"
