import subprocess
import sys
from time import sleep

from loggingConfig import setupLogging
logger = setupLogging()

#TODO: Add step to remove all sandbox mood files including the .dat backups
#TODO: Add way of maybe checking if the verification process was started or not? No idea if this is possible or not tho
if __name__ == '__main__':
    try:
        logger.info(f"We are now attemtping to initiate the steam verification process for Wargame: Red Dragon!")
        logger.info("Your steam client will open on the screen and the process should start, if not start it manually.")
        sleep(2)
        subprocess.run(['start', "steam://validate/251060"], shell=True)
    except Exception as e:
        logger.info(f"An error occurred: {e}")
