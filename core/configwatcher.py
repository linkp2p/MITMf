#!/usr/bin/env python2.7

# Copyright (c) 2014-2016 Marcello Salvati
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA
#

from mitmflib.watchdog.observers import Observer
from mitmflib.watchdog.events import FileSystemEventHandler
from configobj import ConfigObj

class ConfigWatcher(FileSystemEventHandler, object):

    @property
    def config(self):
        return ConfigObj("./config/mitmf.conf")

    def on_modified(self, event):
        self.on_config_change()

    def start_config_watch(self):
        observer = Observer()
        observer.schedule(self, path='./config', recursive=False)
        observer.start()

    def on_config_change(self):
        """ We can subclass this function to do stuff after the config file has been modified"""
        pass
