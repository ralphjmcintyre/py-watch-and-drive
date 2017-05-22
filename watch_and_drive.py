import pyinotify
import os

wm = pyinotify.WatchManager()

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        cmdstring = "gdrive upload %s" % (event.pathname)
        print "Creating:", os.system(cmdstring)

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
directory = '/tmp'
wdd = wm.add_watch(directory, mask, rec=True)

notifier.loop()
