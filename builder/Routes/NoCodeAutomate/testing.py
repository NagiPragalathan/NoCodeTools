from .Tools import SetupTools
from .Stack_data import get_stack, json_to_dect
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import cv2
import os, json
import sys
import numpy as np
import traceback
from json2html import *
import threading
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


run = True


class Nocode_test:
    def __init__(self) -> None:
        pass
    def getpath(self,nested_dict, value, prepath=()):
        for k, v in nested_dict.items():
            path = prepath + (k,)
            if v == value:
                return path
            elif hasattr(v, 'items'):
                p = self.getpath(v, value, path)
                if p is not None:
                    return p
    def make_dict_to_table(self,input):
        html_File = open(str(os.path.abspath(os.getcwd())+"\\Document_Results\\Table_structure.html"),'w')
        html_format = json2html.convert(json = input)
        html_File.write(html_format)


    def make_xml(self,dict_data ):
        Xml_File = open(str(os.path.abspath(os.getcwd())+"\\Document_Results\\Testing_structure.xml"),'w')

        my_item_func = lambda x: 'list_item'
        xml = dicttoxml(dict_data, item_func = my_item_func)

        xml_format = parseString(xml).toprettyxml()
        Xml_File.write(xml_format)

    def take_video_rec(self):
        resolution = (1920, 1080)
        codec = cv2.VideoWriter_fourcc(*"XVID")
        filename = "Test_Video/Recording.avi"  # this linke take's screen_rec but the given path is already exits it's save else it's not take screenshot for example('folder/img.png') the folder if exist the screenshot will save else it's not save
        fps = 30.0
        out = cv2.VideoWriter(filename, codec, fps, resolution)
        while run:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            if cv2.waitKey(1) == ord('q'):
                break
        out.release()
        cv2.destroyAllWindows()


    def action(self,element,action):
        action_obj = ActionChains(self.copy_driver)

        if action == 'click':
            element.click()
        elif action == 'click_hold':
            action_obj.click_and_hold(on_element = element)
            action_obj.perform()
        elif action == 'context_click':
            action_obj.context_click(on_element = element)
            action_obj.perform()
        elif action == 'double_click':
            action_obj.double_click(on_element = element)
            action_obj.perform()

    def Make_test(self,path):
        # Create required folders
        folders = ['Test_Video','ScreenShots','Document_Results']
        try :
            for i in folders:
                current_path = os.path.join("/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1]),i)
                os.mkdir(current_path)
        except:
            print('files alresdy exists')
        global run
        # Make XML result of test output :
        self.make_xml(json_to_dect(json.loads(open(path,'r').read())))
        self.make_dict_to_table(json.loads(open(path,'r').read()))



        get_ids = ['id','name','class','xpath']
        list_data = ['ls_id_clk','ls_name_clk','ls_xpath_clk']

        orginal = get_stack(path)
        stack = get_stack(path)[1:]
        try :
            if orginal[0].get("auto_install") == "true":
                driver = SetupTools.install_selenium_tool(orginal[0].get("browser"))
            else:
                path = orginal[0].get('driver_path')
                driver : webdriver = webdriver.Chrome(path)
                self.copy_driver = driver
                driver.get(orginal[0].get('get'))
                if orginal[0].get('window') == 'maximize':
                    driver.maximize_window()
                    
        except:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(orginal[0].get('get'))
            if orginal[0].get('window') == 'maximize':
                driver.maximize_window()
        if orginal[0].get('screen_recorder') == 'true':            
            t1 = threading.Thread(target=self.take_video_rec)
            t1.start()
        for i in stack:
            time.sleep(1)
            for j in i.keys():
                try :
                    if j in list_data:
                        if j == 'ls_id_clk': # list id's excution line
                            for k in i.get(j):
                                Element = driver.find_element('id', k)
                                self.action(Element,'click')

                        elif j == 'ls_name_clk':
                            for k in i.get(j):
                                Element = driver.find_element('name', k)
                                self.action(Element,'click')

                        elif j == 'ls_xpath_clk':
                            for k in i.get(j):
                                Element = driver.find_element('name', k)
                                self.action(Element,'click')

                    if j in get_ids:
                        if ':' in i.get(j):
                            values = i.get(j).split(':')
                            at_splited = values[1].split('@')
                            element_id = values[0]
                            print(element_id)
                            # find element
                            Element = driver.find_element(j, element_id)
                                    # Select DropDown Methods
                            for k in range(1,len(values)):
                                if at_splited[0] == 'select_by_index':
                                    if 'data' in i.keys():
                                        Select(Element).select_by_index(int(i.get('data')))
                                    else :
                                        Select(Element).select_by_index(int(at_splited[1]))
                                elif at_splited[0] == 'select_by_value':
                                    if 'data' in i.keys():
                                        Select(Element).select_by_value(int(i.get('data')))
                                    else :
                                        Select(Element).select_by_value(int(at_splited[1]))
                                elif at_splited[0] == 'select_by_visible_text':
                                    if 'data' in i.keys():
                                        Select(Element).select_by_visible_text(int(i.get('data')))
                                    else :
                                        Select(Element).select_by_visible_text(int(at_splited[1]))

                                            # DeSelectDropSown Methods
                                elif at_splited[0] == 'deselect_all':
                                    Select(Element).deselect_all()
                                elif at_splited[0] == 'deselect_by_index':
                                    if 'data' in i.keys():
                                        Select(Element).deselect_by_index(int(i.get('data')))
                                    else :
                                        Select(Element).deselect_by_index(int(at_splited[1]))
                                elif at_splited[0] == 'deselect_by_value':
                                    if 'data' in i.keys():
                                        Select(Element).deselect_by_value(int(i.get('data')))
                                    else :
                                        Select(Element).deselect_by_value(int(at_splited[1]))
                                elif at_splited[0] == 'deselect_by_visible_text':
                                    if 'data' in i.keys():
                                        Select(Element).deselect_by_visible_text(int(i.get('data')))
                                    else :
                                        Select(Element).deselect_by_visible_text(int(at_splited[1]))
                                            # Input Filed Methods
                                # input box types...
                                if values[k] == 'sk':
                                    if 'data' in i.keys():
                                        Element.send_keys(i.get('data'))
                                elif values[k] == 'c&sk':
                                    if 'data' in i.keys():
                                        Element.clear()
                                        Element.send_keys(i.get('data'))
                                elif values[k] == 'click':
                                    self.action(Element,'click')
                                elif values[k] == 'click_hold':
                                    self.action(Element,'click_hold')
                                elif values[k] == 'context_click':
                                    self.action(Element,'context_click')
                                elif values[k] == 'double_click':
                                    self.action(Element,'double_click')

                                            # window's oprating methods
                                if values[k] == 'maximize' or i.get('window') == 'maximize':
                                    driver.maximize_window()
                                elif values[k] == 'minimize' or i.get('window') == 'minimize':
                                    driver.minimize_window()
                                
                                if type(i.get('set_window_position')) == list :
                                    pos = i.get('set_window_position')
                                    driver.set_window_position(pos[0],pos[1])

                                            # take Screenshot
                                if i.get('python_code') != None or i.get('python_script') != None :
                                    execute = i.get('python_code')
                                    exec(execute,{'driver':driver})
                                if i.get('python_code_path') != None or i.get('python_script_path') != None :
                                    if i.get('python_code_path') != None :
                                        if '@' in i.get('python_code_path'):
                                            execute = open(i.get('python_code_path').split('@')[0],'r').read()
                                            for j in range(1,len(i.get('python_code_path').split('@'))):
                                                execute = str(execute) + "\n" + i.get('python_code_path').split('@')[j]
                                        else:
                                            execute = open(i.get('python_code_path'),'r')
                                    elif i.get('python_script_path') != None :
                                        if '@' in i.get('python_code_path'):
                                            execute = open(i.get('python_code_path').split('@')[0],'r').read()
                                            for j in range(1,len(i.get('python_code_path').split('@'))):
                                                execute = str(execute) + "\n" + i.get('python_code_path').split('@')[j]
                                        else:
                                            execute = open(i.get('python_code_path'),'r')
                                    exec(execute,{'driver':driver})
                                if i.get('take') == "screenshot" :
                                    driver.save_screenshot('ScreenShots/pic.png') # this linke take's screenshot but the given path is already exits it's save else it's not take screenshot for example('folder/img.png') the folder if exist the screenshot will save else it's not save
                except BaseException as e:
                    if sys.argv[0] == 'Debug=true':
                        # print("".join(traceback.format_exception(e)).strip())
                        print("".join(traceback.format_exception_only(e)).strip())

        run = False
        if orginal[0].get('run_and_wait') == 'true' :
            input("\n\n\nPress 'ctrl' + 'c' to close server")



