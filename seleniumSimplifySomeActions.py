from selenium.webdriver.common import By
import time



def findCheck(target, query, wait = 0.5, command = By.CSS_SELECTOR):
    
    if wait:
        time.sleep(wait)

    try:
        target.find_element(command, query)
    except:
        return False


def findCheckRepeat(target, query, max_tries=3, max_time=None, delay=0.5, wait=None, command=By.CSS_SELECTOR):
    
    curr_time = None
    curr_try = 0
    finished = False

    if max_time:
        max_time = time.time() + max_time

    if wait:
        time.sleep(wait)

    while not finished:

        if findCheck(target, command, query, wait=None, command=command) != False:
            return True


        # ends of loop
        if max_time:
            if time.time() >= max_time:
                finished = True


        if max_tries:
            
            curr_try += 1
            if curr_try >= max_tries:
                finished = True


        if not max_time and not max_tries:
            finished = True

        time.sleep(delay)

    return False



