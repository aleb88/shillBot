import codecs
import os

from workers.basic_worker import *

worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")
worker.run()
