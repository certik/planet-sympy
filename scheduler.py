#! /usr/bin/env python

import os
import subprocess
import time

def job(silence_error=False):
    print("Launching job (./update.sh)...")
    result = subprocess.Popen("./update.sh")
    text = result.communicate()[0]
    returncode = result.returncode
    if not silence_error:
        if returncode != 0:
            raise Exception("Return code is non zero.")
    print("Job finished.")

print("Docker environment variables:")
if os.environ.get("DEPLOY_TOKEN"):
    deploy_token_display = "<non-emtpy deploy token>"
else:
    deploy_token_display = "<empty>"
print("DEPLOY_TOKEN =", deploy_token_display)
print("Running job()")
job()
