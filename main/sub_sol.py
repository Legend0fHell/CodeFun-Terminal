from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys
import time
import colorama
import clipboard

def sub_prob():
    # USER INFORMATIONS
    sys.stdin = open('login.credential', 'r')
    user_handle = input()
    user_password = input()
    print(colorama.Fore.BLUE + "Username: " + colorama.Fore.CYAN + user_handle + colorama.Fore.RESET, end='\n')
    LOGIN_URL = 'https://codefun.vn/'
    SUBMIT_URL = 'https://codefun.vn/submit'
    opt = Options()
    browser = Chrome()
    browser.minimize_window()
    print(colorama.Fore.BLUE + 'Booting up a headless browser' + colorama.Fore.RESET, end='\r')
    browser.get(LOGIN_URL)
    print('                                                                   ', end='\r')
    print(colorama.Fore.BLUE + 'Logging you in...' + colorama.Fore.RESET, end='\r')
    # LOGGING IN 
        # Getting input fields

    try:
        browser_handle = browser.find_element_by_xpath('//*[@placeholder="Username"]')
        browser_password = browser.find_element_by_xpath('//*[@placeholder="Password"]')
        browser_submit = browser.find_element_by_xpath('//*[@type="submit"]')
    except Exception as error:
        print(colorama.Fore.RED + "Problem hooking to the site!" + colorama.Fore.RESET, end='\n')
        browser.close()
        return -1
    
    browser_handle.send_keys(user_handle)
    browser_password.send_keys(user_password)
    browser_submit.click()

    lmaoforlmao = 1
    while lmaoforlmao < 2: # Check if successfully login
        try:
            browser.find_element_by_xpath('//*[@class="panel panel-primary"]')
            break
        except:
            continue
    
    try: # Checking for an error message in the browser
        check_registration = browser.find_element_by_xpath('//*[@role="alert"]')
        print(colorama.Fore.RED + "Incorrect Login Credential!" + colorama.Fore.RESET, end='\n')
        browser.close()
        return -1
    except:
        print(colorama.Fore.GREEN + "Successfully logged in!" + colorama.Fore.RESET, end='\n')
        browser.get(SUBMIT_URL)
        while lmaoforlmao < 2: # Check if successfully having field
            try:
                browser.find_element_by_xpath('//*[@class="ace_text-input"]')
                break
            except:
                continue

        # Taking the solution as input
        problem_index = input()
        problem_file_path = input()
        print(colorama.Fore.BLUE + "Problem Code: " + colorama.Fore.CYAN + problem_index + colorama.Fore.RESET, end='\n')
        print(colorama.Fore.BLUE + "Solution File Path: " + colorama.Fore.CYAN + problem_file_path + colorama.Fore.RESET, end='\n')
        
        try:
            browser_problem_index = browser.find_element_by_xpath('//*[@placeholder="Pxxxxx"]')
            browser_problem_index.send_keys(problem_index)
        except:
            print(colorama.Fore.RED + "Problem hooking to the site!" + colorama.Fore.RESET, end='\n')
            browser.close()
            return -1
        
        browser_code_area = browser.find_element_by_xpath('//*[@class="ace_text-input"]')
        browser_code_submit_button = browser.find_element_by_xpath('//*[@type="submit"]')


        try:
            with open(problem_file_path, 'r') as sol:
                print(colorama.Fore.YELLOW + "Submiting solution..." + colorama.Fore.RESET, end='\r')

                solution_code = sol.read()
                sol_code = clipboard.copy(solution_code)

                actions = ActionChains(browser)
                actions.click(browser_code_area)

                actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)

                actions.click(browser_code_submit_button)
                actions.perform()

                problemTitle=browser.title
                while problemTitle == 'Submit - Codefun.VN': problemTitle=browser.title
                print(colorama.Fore.GREEN + "Sucessfully submitted the solution!" + colorama.Fore.RESET, end='\n')
                problemTitle=browser.title
                while lmaoforlmao < 2: # Check 
                    try:
                        print(colorama.Fore.YELLOW + problemTitle + " is being judged" + colorama.Fore.RESET, end='\r')
                        browser.find_element_by_xpath('//*[@class="submission-running"]')
                    except:
                        print(colorama.Fore.GREEN + problemTitle + " was judged successfully!" + colorama.Fore.RESET, end='\n')
                        break
                browser.maximize_window()
                time.sleep(10)
                return -1
                browser.close()
                

            
        except Exception as err:
            print(colorama.Fore.RED + "Problem reading file!" + colorama.Fore.RESET, end='\n')
            return -1
            browser.close()

        
