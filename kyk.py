from ast import Break, main
from signal import signal
import time
from selenium import webdriver
from selenium.common.exceptions import *

# ! Kyk.py
# * Usage Guide
# * install driver from: https://chromedriver.chromium.org/
# * set browser path where you downloaded the chrome driver .
# * login your account
# * python kyk.py
# * if you want to end session just press ctrl + c
# * dependencies : pip3 install selenium
url = "https://wifi.gsb.gov.tr/"


def logout():
    print(":) Trying to logut wifi.gsb.gov.tr ...")

    driver.execute_script(
        "document.getElementsByName('servisUpdateForm:j_idt136')[0].click();"
    )

    driver.get("https://google.com")

    if driver.title == "Google":
        print(":( Logout failed . Login and logout manually !")

    print(":) Logout success byee .")
    driver.quit()
    exit(0)


def succ(i, terror):
    a = ((i - terror) / i) * 100
    return a


def main():
    print(
        """
         __ __             __
        / //_/   __  __   / /__       ____    __  __
       / ,<     / / / /  / //_/      / __ \  / / / /
      / /| |   / /_/ /  / ,<    _   / /_/ / / /_/ /
     /_/ |_|   \__, /  /_/|_|  (_) / .___/  \__, /
              /____/              /_/      /____/
        """
    )

    print("Melih Isbilen | Github.com/melihi | melih.ninja | 2022")
    path = "/home/aeruginosa/Tools/chromedriver"
    timeout = 300
    username = "y0ur_t0p_s3cr3t_us3rn4m3"
    password = "y0ur_t0p_s3cr3t_p4ssw0rd"
    while True:
        try:
            global driver
            driver = webdriver.Chrome(path)
            driver.set_page_load_timeout(timeout)
            driver.minimize_window()
            print(":) Driver started !")
            driver.get(url + "login.html")

            if driver.title == "Giriş":
                print(":) I am trying to filling input values and login your account !")
                driver.execute_script(
                    "document.forms['f']['j_username'].value = \"" + username + '";'
                )
                driver.execute_script(
                    "document.forms['f']['j_password'].value = \"" + password + '";'
                )
                driver.execute_script(
                    "document.getElementsByName('submit')[0].click();"
                )
                driver.get(url)
                if driver.title != "Giriş":
                    print(":) Login success !")
                    break
            else:
                print(":) You alread logged in !")
                break

        except WebDriverException as e:
            print(":( Unkown Webdriver error .\n", e)
            driver.quit()
            print("\n:( Restarting driver ...")
        except KeyboardInterrupt:
            exit(0)
        except:
            print(":( Unkown error . Something bad happened ...")
            driver.quit()
            print("\n:( Restarting driver ...")

    driver.execute_script("window.open('http://melih.ninja');")
    i = 0
    terror = 0
    while True:
        try:
            driver.get(url)
            if driver.title == "Giriş":

                print("\n:( Your session ended unexpectedly ...  Exiting ")
                driver.quit()
                break
        except TimeoutException:
            print(":( Time out error \n")
            terror += 1
        except KeyboardInterrupt:
            logout()
        except WebDriverException as e:
            print(
                ":( WebDriverException . Something bad happened ... Restarting webdriver ...\n",
                e,
                end="\n",
            )
            driver.quit()
            driver = webdriver.Chrome(path)
            driver.set_page_load_timeout(timeout)
            driver.get(url)
        except:
            print(
                ":( Unknown error . Something bad happened ... Restarting webdriver ...\n",
                end="\n",
            )
            driver.quit()
            driver = webdriver.Chrome(path)
            driver.set_page_load_timeout(timeout)
            driver.get(url)

        i += 1
        print(
            "Total request : %d  | Timeout Error : %d | Succes rate : %.2f "
            % (i, terror, succ(i, terror)),
            end="\r",
        )
        time.sleep(5)


main()
