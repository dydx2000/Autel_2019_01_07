#!/usr/bin/python
# -*- coding: utf-8 -*-
from logger import logger
from Initial import InitialDevice
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
import random
class CameraTest:
    def __init__(self,InitialDevice = InitialDevice.InitialDevice()):
       self.InitalDevice = InitialDevice
       self.logger = logger.Logger(path="./CameraTest.log")
       #self.InitalDevice.startApp()
       pass

    def GoToCameraMainWindow(self):
        try:
            self.InitalDevice.GoToCameraInterface()
        except Exception as e:
            self.logger.logger.warn(e)
        else:
            pass

    def ExittoStartInterface(self):
        try:
           self.InitalDevice.ExittoStartInterface()
        except Exception as e:
            self.logger.logger.warn(e)
        else:
            pass

    def ExitTest(self):
        self.InitalDevice.closeApp()


    def SwitchtoRecordMode(self):
        try:
            self.InitalDevice.GoToCameraInterface()
            sleep(0.5)
        except:
            self.logger.logger.warn("Go to camera interface error***")
        else:
            if self.checkSDisFullWithPopSDFullDialog():
                self.CancelFormatSDCardWithPopSDFullDialog()
            try:
                SwitchtoRecordModel = self.InitalDevice.driver.find_element_by_accessibility_id(
                    "Btn console switch video norma")
            except:
                try:
                    SwitchtoRecordModel1 = self.InitalDevice.driver.find_element_by_accessibility_id(
                        "Btn console switch photo norma")
                except:
                    self.logger.logger.warn("Can not find the switch control button***")
                else:
                    SwitchtoRecordModel1.click()
            else:
                pass
    def doCaptureInCaptureMode(self):
        self.SwitchtoCaptureMode()
        #sleep(1.5)
        try:
            CaptureControlElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console photo normal")
        except:
            self.logger.logger.warn(
                "Can not find capture control button in Capture Mode***")
            try:
                CaptureInBusyControlElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console shoot waiting")
            except:
                self.logger.logger.warn(
                    "Can not find capture control button in Capture Mode***")
            else:
                try:
                    CaptureInBusyControlElement.click()
                    sleep(0.5)
                except:
                    self.logger.logger.warn(
                        "Do capture in Capture Mode error***")
                else:
                    try:
                        checkSDCardFullElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            "SD card is full")
                    except:
                        pass
                    else:
                        self.logger.logger.warn(
                            "SD card is full!!!")
                        self.FormatSDcardWithCameraSetting()
                        try:
                            CaptureControlElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "Btn console photo normal")
                        except:
                            self.logger.logger.warn(
                                "Can not find capture control button in Capture Mode***")
                            try:
                                CaptureInBusyControlElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    "Btn console shoot waiting")
                            except:
                                self.logger.logger.warn(
                                    "Can not find capture control button in Capture Mode***")
                            else:
                                try:
                                    CaptureInBusyControlElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Do capture in Capture Mode error***")
                                else:
                                    pass
                        else:
                            try:
                                CaptureControlElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Do capture in Capture Mode error***")
                            else:
                                pass
        else:
            try:
                CaptureControlElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Do capture in Capture Mode error***")
            else:
                try:
                    checkSDCardFullElement = self.InitalDevice.driver.find_element_by_accessibility_id("SD card is full")
                except:
                    pass
                else:
                    self.logger.logger.warn(
                        "SD card is full!!!")
                    self.FormatSDcardWithCameraSetting()
                    try:
                        CaptureControlElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            "Btn console photo normal")
                    except:
                        self.logger.logger.warn(
                            "Can not find capture control button in Capture Mode***")
                        try:
                            CaptureInBusyControlElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "Btn console shoot waiting")
                        except:
                            self.logger.logger.warn(
                                "Can not find capture control button in Capture Mode***")
                        else:
                            try:
                                CaptureInBusyControlElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Do capture in Capture Mode error***")
                            else:
                                pass
                    else:
                        try:
                            CaptureControlElement.click()
                        except:
                            self.logger.logger.warn(
                                "Do capture in Capture Mode error***")
                        else:
                            pass

    def StopTimelapseCaptureInCaptureMode(self):
        # while True:
        #     try:
        #         CaptureControlElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console shoot waiting")
        #     except:
        #         break
        #     else:
        #         sleep(0.1)
        # if interval == "2S":
            while True:
                try:
                     CaptureControlElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console photo interval")
                except Exception as e:
                        # self.logger.logger.warn(
                        #     "Can not find stop timelapse capture control button in Capture Mode***")
                        #print e
                        try:
                            CaptureControlElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "Btn console photo normal")
                        except:
                            try:
                                RecordControlElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "Btn console video normal")
                            except:
                                sleep(0.2)
                            else:
                                break
                        else:
                            break
                else:
                    try:
                        CaptureControlElement.click()
                    except:
                        # self.logger.logger.warn(
                        #     "Stop timelapse capture in Capture Mode error***")
                        pass
                    else:
                        sleep(0.5)
                        try:
                            CaptureControlElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console photo normal")
                        except:
                            pass
                        else:
                            break
        # else:
        #     try:
        #         CaptureControlElement = self.InitalDevice.driver.find_element_by_accessibility_id(
        #             "Btn console photo interval")
        #     except:
        #         self.logger.logger.warn(
        #             "Can not find stop timelapse capture control button in Capture Mode***")
        #     else:
        #         try:
        #             CaptureControlElement.click()
        #         except:
        #             self.logger.logger.warn(
        #                 "Stop timelapse capture in Capture Mode error***")
        #         else:
        #             sleep(0.5)
            

    def SwitchtoCaptureMode(self):
        try:
            self.InitalDevice.GoToCameraInterface()
            sleep(1)
        except:
            self.logger.logger.warn(
                "Go to camera interface  in Capture Mode error***")
        else:
            if self.checkSDisFullWithPopSDFullDialog():
                self.CancelFormatSDCardWithPopSDFullDialog()
            try:
                SwitchtoRecordModel = self.InitalDevice.driver.find_element_by_accessibility_id(
                    "Btn console switch photo norma")
            except:
                try:
                    SwitchtoRecordModel1 = self.InitalDevice.driver.find_element_by_accessibility_id(
                        "Btn console switch video norma")
                except Exception as e:
                    pass
                else:
                    SwitchtoRecordModel1.click()
            else:
                pass



    def setManualExposureModeInCaptureMode(self):
        self.SwitchtoCaptureMode()
        sleep(0.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except Exception as e:
            pass
        else:
            pass
        try:
            el2 = self.InitalDevice.driver.find_element_by_accessibility_id("MANUAL")
        except:
            try:
                SelectExpModeElement = self.InitalDevice.driver.find_element_by_accessibility_id("AUTO")
            except Exception as e:
                self.logger.logger.warn(
                    "Can not find exposure setting item in Capture Mode***")
            else:
                SelectExpModeElement.click()
                sleep(0.5)
                try:
                    ManualExpModeElement= self.InitalDevice.driver.find_element_by_accessibility_id("MANUAL")
                except Exception as e:
                    self.logger.logger.warn(
                        "Can not find the MANUAL exposure setting in Capture Mode***")
                else:
                    try:
                        ManualExpModeElement.click()
                    except:
                        self.logger.logger.warn(
                            "Set Manual Exposure Mode In Capture Mode Error***")
                    else:
                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                {"x": 333,
                                                                 "y": 187})
        else:
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})
    def setAutoExposureModeInCaptureMode(self):
        self.SwitchtoCaptureMode()
        sleep(0.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except Exception as e:
            self.logger.logger.warn(
                "Can not find Bottom Set Bar Element in capture mode***")
        else:
            pass
        try:
            el2 = self.InitalDevice.driver.find_element_by_accessibility_id("AUTO")
        except:
            try:
                SelectExpModeElement = self.InitalDevice.driver.find_element_by_accessibility_id("MANUAL")
            except:
                pass
            else:
                SelectExpModeElement.click()
                sleep(0.5)
                try:
                    AutoExpModeElement= self.InitalDevice.driver.find_element_by_accessibility_id("AUTO")
                except Exception as e:
                    self.logger.logger.warn(
                        "Can not find exposure setting item in Capture Mode***")
                else:
                    try:
                        AutoExpModeElement.click()
                    except:
                        self.logger.logger.warn(
                            "Set Auto Exposure Mode In Capture Mode Error***")
                    else:
                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                {"x": 333,
                                                                 "y": 187})

        else:
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})

    def setShutterInCaptureMode(self,shutter):
        ##select shutter setting
        self.SwitchtoCaptureMode()
        sleep(0.5)
        self.setManualExposureModeInCaptureMode()
        sleep(0.5)
        CurrentShutter = self.GetCurrentShutter()
        try:
           shutterSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("SHUTTER")
        except Exception as e:
            pass
        else:
            shutterSettingElement.click()
            sleep(1.5)
        try:
            if shutter.find("/") != -1:
                ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter)
                if not ShutterElement.is_displayed():
                    raise AttributeError
            else:
                ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter+"\"")
                if not ShutterElement.is_displayed():
                    raise AttributeError
        except:
            if shutter.__contains__("/"):
                shutterlist = shutter.split("/")
                shutterValue = float(shutterlist[0])/float(shutterlist[1])
            else:
                shutterValue = float(shutter.replace("\"", ""))
            if CurrentShutter !=None:
                if CurrentShutter.__contains__("/"):
                    CurrentShutterlist = CurrentShutter.split("/")
                    currentShutterValue = float(CurrentShutterlist[0])/float(CurrentShutterlist[1])
                else:
                    currentShutterValue = float(CurrentShutter.replace("\"", ""))
                if shutterValue == currentShutterValue:
                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                    return
                elif shutterValue > currentShutterValue:
                    swiptimes = 0
                    while True:
                        try:
                            shuttersliderElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left', "element": shuttersliderElement})
                            sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Can not find shutter slider Element***")
                        else:
                            try:
                                if shutter.find("/")!= -1:
                                    ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter)
                                    if not ShutterElement.is_displayed():
                                        raise AttributeError
                                else:
                                    ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter + "\"")
                                    if not ShutterElement.is_displayed():
                                        raise AttributeError
                            except:
                                swiptimes = swiptimes + 1
                                if swiptimes > 15:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                                    self.logger.logger.warn(
                                        "Set shutter to %s\" error***"%shutter)
                                    break
                                pass
                            else:
                                ShutterElement.click()
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                break
                else:
                    swiptimes = 0
                    while True:
                        try:
                            shuttersliderElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right', "element": shuttersliderElement})
                            sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Can not find shutter slider Element***")
                        else:
                            try:
                                if shutter.find("/") != -1:
                                    ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter)
                                    if not ShutterElement.is_displayed():
                                        raise AttributeError
                                else:
                                    ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter + "\"")
                                    if not ShutterElement.is_displayed():
                                        raise AttributeError
                            except:
                                swiptimes = swiptimes + 1
                                if swiptimes > 15:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                                    self.logger.logger.warn(
                                        "Set shutter to %s in capture mode error***" % shutter)
                                    break
                            else:
                                ShutterElement.click()
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                break
            else:
                self.logger.logger.warn(
                    "Can not get current shutter***")
        else:
            try:
                ShutterElement.click()
            except:
                self.logger.logger.warn(
                    "Set shutter to %s in capture mode error***" % shutter)
            else:
                self.InitalDevice.driver.execute_script("mobile: tap",
                                                        {"x": 333,
                                                         "y": 187})




    def setISOInCaptureMode(self,ISO):
        ##select shutter setting
        self.SwitchtoCaptureMode()
        sleep(1.5)
        self.setManualExposureModeInCaptureMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn(
                "Can not find Bottom Set Bar Element in capture mode***")
        else:
            CurrentISO = self.GetCurrentISOSetting()
            if CurrentISO !=None:
                CurrentISOValue = int(CurrentISO)
                ISOValue = int(ISO)
                try:
                    ISOSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("ISO")
                except Exception as e:
                    self.logger.logger.warn(
                        "Can not find ISO setting item in capture  mode***")
                else:
                    ISOSettingElement.click()
                    sleep(1.5)
                if ISOValue > CurrentISOValue:
                    try:
                        shuttersliderElement = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                    except:
                        self.logger.logger.warn(
                            "Can not find ISO value swip bar in capture  mode***")
                    else:
                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                {'direction': 'left', "element": shuttersliderElement})
                        sleep(1.5)
                        try:
                            ISOElement = self.InitalDevice.driver.find_element_by_accessibility_id(ISO)
                            if not ISOElement.is_displayed():
                                raise AttributeError
                        except:
                            self.logger.logger.warn(
                                "Can not find ISO value setting item in capture  mode***")
                        else:
                            try:
                                ISOElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Set ISO to %s in capture  mode error***" % ISO)
                            else:
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                elif ISOValue < CurrentISOValue:
                    try:
                        shuttersliderElement = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                    except:
                        self.logger.logger.warn(
                            "Can not find ISO value swip bar in capture  mode***")
                    else:
                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                {'direction': 'right', "element": shuttersliderElement})
                        sleep(1.5)
                        try:
                            ISOElement = self.InitalDevice.driver.find_element_by_accessibility_id(ISO)
                            if not ISOElement.is_displayed():
                                raise AttributeError
                        except:
                            self.logger.logger.warn(
                                "Can not find ISO setting value item in capture  mode***")
                        else:
                            try:
                                ISOElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Set ISO to %s in capture  mode error***" % ISO)
                            else:
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                else:
                    # exit setting interface
                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
            else:
                self.logger.logger.warn(
                    "Can not get current ISO setting in capture  mode***")

    def GetCurrentTimelapse(self):
        iSTimelapse2sExist = self.InitalDevice.checkUIElementExist(" 2S")
        iSTimelapse5sExist = self.InitalDevice.checkUIElementExist(" 5S")
        iSTimelapse7sExist = self.InitalDevice.checkUIElementExist(" 7S")
        iSTimelapse10sExist = self.InitalDevice.checkUIElementExist(" 10S")
        iSTimelapse20sExist = self.InitalDevice.checkUIElementExist(" 20S")
        iSTimelapse30sExist = self.InitalDevice.checkUIElementExist(" 30S")
        iSTimelapse60sExist = self.InitalDevice.checkUIElementExist(" 60S")
        if iSTimelapse2sExist:
            return " 2S"
        if iSTimelapse5sExist:
            return " 5S"
        if iSTimelapse7sExist:
            return " 7S"
        if iSTimelapse10sExist:
            return " 10S"
        if iSTimelapse20sExist:
            return " 20S"
        if iSTimelapse30sExist:
            return " 30S"
        if iSTimelapse60sExist:
            return " 60S"

    def setAEBBurstTimelapse(self,Mode,NumberOrTimeInterval):
        if Mode != "SINGLE SHOT":
            try:
                CaptureTypeElement1 = self.InitalDevice.driver.find_element_by_accessibility_id(
                    " " + Mode + " ")
            except Exception as e:
                ##current set is the right type
                if Mode == "BURST":
                    try:
                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" "+
                            NumberOrTimeInterval)
                    except:
                        if NumberOrTimeInterval == "3" or NumberOrTimeInterval == "5":
                            BurstSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": BurstSettingBarElement})
                            sleep(1.5)
                            try:
                                CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" "+
                                    NumberOrTimeInterval)
                            except:
                                self.logger.logger.warn(
                                    "Can not find burst setting value %s Element in capture mode***"%NumberOrTimeInterval)
                            else:
                                try:
                                    CaptureTypeElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set %s burst in capture mode error***" % NumberOrTimeInterval)
                                else:
                                    #sleep(1.5)
                                    # exit setting interface
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                        else:
                            BurstSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": BurstSettingBarElement})
                            sleep(1.5)
                            try:
                                CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" "+
                                    NumberOrTimeInterval)
                            except:
                                self.logger.logger.warn(
                                    "Can not find burst setting value %s Element in capture mode***" % NumberOrTimeInterval)
                            else:
                                try:
                                    CaptureTypeElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set %s burst in capture mode error***" % NumberOrTimeInterval)
                                else:
                                    #sleep(1.5)
                                    # exit setting interface
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                    else:
                        try:
                            CaptureTypeElement.click()
                            sleep(1.5)
                        except:
                            if NumberOrTimeInterval == "3" or NumberOrTimeInterval == "5":
                                BurstSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": BurstSettingBarElement})
                                sleep(1.5)
                                try:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                   NumberOrTimeInterval)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find burst setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                else:
                                    try:
                                        CaptureTypeElement.click()
                                    except:
                                        self.logger.logger.warn(
                                            "Set %s burst in capture mode error***" % NumberOrTimeInterval)
                                    else:
                                        # sleep(1.5)
                                        # exit setting interface
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            else:
                                BurstSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": BurstSettingBarElement})
                                sleep(1.5)
                                try:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                   NumberOrTimeInterval)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find burst setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                else:
                                    try:
                                        CaptureTypeElement.click()
                                    except:
                                        self.logger.logger.warn(
                                            "Set %s burst in capture mode error***" % NumberOrTimeInterval)
                                    else:
                                        # sleep(1.5)
                                        # exit setting interface
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                        else:
                            # exit setting interface
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
                elif Mode == "AEB":
                    try:
                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" "+
                            NumberOrTimeInterval)
                    except:
                        self.logger.logger.warn(
                            "Can not find AEB setting value %s Element in capture mode***" % NumberOrTimeInterval)
                    else:
                        try:
                            CaptureTypeElement.click()
                        except:
                            self.logger.logger.warn(
                                "Set %s AEB in capture mode error***" % NumberOrTimeInterval)
                        else:
                            # sleep(1.5)
                            # exit setting interface
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
                else:
                    CurrentTimelapse = self.GetCurrentTimelapse()
                    if CurrentTimelapse !=None:
                        CurrentTimelapseValue = int(CurrentTimelapse.replace("S","").replace(" ",""))
                        NumberOrTimeIntervalValue = int(NumberOrTimeInterval.replace("S",""))
                        try:
                            CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" "+
                                NumberOrTimeInterval)
                            CaptureTypeElementLocation = CaptureTypeElement.location
                            if CaptureTypeElementLocation["x"] > 667 or CaptureTypeElementLocation["x"] < 0:
                                self.logger.logger.warn(
                                    "Format Element is not visiable***")
                                raise AttributeError
                        except Exception as e:
                            if NumberOrTimeIntervalValue < CurrentTimelapseValue:
                                TimelapseSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": TimelapseSettingBarElement})
                                sleep(1.5)
                                try:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                   NumberOrTimeInterval)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find timelapse setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                else:
                                    ##60s is invisible ,but can find, so try other way
                                    try:
                                        CaptureTypeElement.click()
                                        sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Set %s timelapse in capture mode error***" % NumberOrTimeInterval)
                                    else:
                                        # sleep(1.5)
                                        # exit setting interface
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            elif NumberOrTimeIntervalValue > CurrentTimelapseValue:
                                TimelapseSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": TimelapseSettingBarElement})
                                sleep(1.5)
                                try:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                   NumberOrTimeInterval)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find timelapse setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                else:
                                    ##60s is invisible ,but can find, so try other way
                                    try:
                                        CaptureTypeElement.click()
                                        sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Set %s timelapse in capture mode error***" % NumberOrTimeInterval)
                                    else:
                                        # sleep(1.5)
                                        # exit setting interface
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            else:
                                # sleep(1.5)
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                        else:
                            try:
                                CaptureTypeElement.click()
                                sleep(1.5)
                            except:
                                if NumberOrTimeIntervalValue < CurrentTimelapseValue:
                                    TimelapseSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'right',
                                                                             "element": TimelapseSettingBarElement})
                                    sleep(1.5)
                                    try:
                                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                       NumberOrTimeInterval)
                                    except:
                                        self.logger.logger.warn(
                                            "Can not find timelapse setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                    else:
                                        ##60s is invisible ,but can find, so try other way
                                        try:
                                            CaptureTypeElement.click()
                                            sleep(1.5)
                                        except:
                                            self.logger.logger.warn(
                                                "Set %s timelapse in capture mode error***" % NumberOrTimeInterval)
                                        else:
                                            # sleep(1.5)
                                            # exit setting interface
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                elif NumberOrTimeIntervalValue > CurrentTimelapseValue:
                                    TimelapseSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'left',
                                                                             "element": TimelapseSettingBarElement})
                                    sleep(1.5)
                                    try:
                                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                       NumberOrTimeInterval)
                                    except:
                                        self.logger.logger.warn(
                                            "Can not find timelapse setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                    else:
                                        ##60s is invisible ,but can find, so try other way
                                        try:
                                            CaptureTypeElement.click()
                                            sleep(1.5)
                                        except:
                                            self.logger.logger.warn(
                                                "Set %s timelapse in capture mode error***" % NumberOrTimeInterval)
                                        else:
                                            # sleep(1.5)
                                            # exit setting interface
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                else:
                                    # sleep(1.5)
                                    # exit setting interface
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                            else:
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                    else:
                        self.logger.logger.warn(
                        "Can not get current timelapse  in capture mode***")

            else:
                CaptureTypeElement1.click()
                sleep(1.5)
                ##current set is the right type
                if Mode == "BURST":
                    try:
                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                       NumberOrTimeInterval)
                    except:
                        if NumberOrTimeInterval == "3" or NumberOrTimeInterval == "5":
                            BurstSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": BurstSettingBarElement})
                            sleep(1.5)
                            try:
                                CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                               NumberOrTimeInterval)
                            except:
                                self.logger.logger.warn(
                                    "Can not find burst setting value %s Element in capture mode***" % NumberOrTimeInterval)
                            else:
                                try:
                                    CaptureTypeElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set %s burst in capture mode error***" % NumberOrTimeInterval)
                                else:
                                    # sleep(1.5)
                                    # exit setting interface
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                        else:
                            BurstSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": BurstSettingBarElement})
                            sleep(1.5)
                            try:
                                CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                               NumberOrTimeInterval)
                            except:
                                self.logger.logger.warn(
                                    "Can not find burst setting value %s Element in capture mode***" % NumberOrTimeInterval)
                            else:
                                try:
                                    CaptureTypeElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set %s burst in capture mode error***" % NumberOrTimeInterval)
                                else:
                                    # sleep(1.5)
                                    # exit setting interface
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                    else:
                        try:
                            CaptureTypeElement.click()
                            sleep(1.5)
                        except:
                            if NumberOrTimeInterval == "3" or NumberOrTimeInterval == "5":
                                BurstSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": BurstSettingBarElement})
                                sleep(1.5)
                                try:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                   NumberOrTimeInterval)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find burst setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                else:
                                    try:
                                        CaptureTypeElement.click()
                                    except:
                                        self.logger.logger.warn(
                                            "Set %s burst in capture mode error***" % NumberOrTimeInterval)
                                    else:
                                        # sleep(1.5)
                                        # exit setting interface
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            else:
                                BurstSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": BurstSettingBarElement})
                                sleep(1.5)
                                try:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                   NumberOrTimeInterval)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find burst setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                else:
                                    try:
                                        CaptureTypeElement.click()
                                    except:
                                        self.logger.logger.warn(
                                            "Set %s burst in capture mode error***" % NumberOrTimeInterval)
                                    else:
                                        # sleep(1.5)
                                        # exit setting interface
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                        else:
                            # exit setting interface
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
                elif Mode == "AEB":
                    try:
                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                       NumberOrTimeInterval)
                    except:
                        self.logger.logger.warn(
                            "Can not find AEB setting value %s Element in capture mode***" % NumberOrTimeInterval)
                    else:
                        try:
                            CaptureTypeElement.click()
                        except:
                            self.logger.logger.warn(
                                "Set %s AEB in capture mode error***" % NumberOrTimeInterval)
                        else:
                            # sleep(1.5)
                            # exit setting interface
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
                else:
                    CurrentTimelapse = self.GetCurrentTimelapse()
                    if CurrentTimelapse !=None:
                        CurrentTimelapseValue = int(CurrentTimelapse.replace("S", "").replace(" ", ""))
                        NumberOrTimeIntervalValue = int(NumberOrTimeInterval.replace("S", ""))
                        try:
                            CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                           NumberOrTimeInterval)
                        except Exception as e:
                            if NumberOrTimeIntervalValue < CurrentTimelapseValue:
                                TimelapseSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": TimelapseSettingBarElement})
                                sleep(1.5)
                                try:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                   NumberOrTimeInterval)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find timelapse setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                else:
                                    ##60s is invisible ,but can find, so try other way
                                    try:
                                        CaptureTypeElement.click()
                                        sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Set %s timelapse in capture mode error***" % NumberOrTimeInterval)
                                    else:
                                        # sleep(1.5)
                                        # exit setting interface
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            elif NumberOrTimeIntervalValue > CurrentTimelapseValue:
                                TimelapseSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": TimelapseSettingBarElement})
                                sleep(1.5)
                                try:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                   NumberOrTimeInterval)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find timelapse setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                else:
                                    ##60s is invisible ,but can find, so try other way
                                    try:
                                        CaptureTypeElement.click()
                                        sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Set %s timelapse in capture mode error***" % NumberOrTimeInterval)
                                    else:
                                        # sleep(1.5)
                                        # exit setting interface
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            else:
                                # sleep(1.5)
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                        else:
                            try:
                                CaptureTypeElement.click()
                                sleep(1.5)
                            except:
                                if NumberOrTimeIntervalValue < CurrentTimelapseValue:
                                    TimelapseSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'right',
                                                                             "element": TimelapseSettingBarElement})
                                    sleep(1.5)
                                    try:
                                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                       NumberOrTimeInterval)
                                    except:
                                        self.logger.logger.warn(
                                            "Can not find timelapse setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                    else:
                                        ##60s is invisible ,but can find, so try other way
                                        try:
                                            CaptureTypeElement.click()
                                            sleep(1.5)
                                        except:
                                            self.logger.logger.warn(
                                                "Set %s timelapse in capture mode error***" % NumberOrTimeInterval)
                                        else:
                                            # sleep(1.5)
                                            # exit setting interface
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                elif NumberOrTimeIntervalValue > CurrentTimelapseValue:
                                    TimelapseSettingBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'left',
                                                                             "element": TimelapseSettingBarElement})
                                    sleep(1.5)
                                    try:
                                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " +
                                                                                                                       NumberOrTimeInterval)
                                    except:
                                        self.logger.logger.warn(
                                            "Can not find timelapse setting value %s Element in capture mode***" % NumberOrTimeInterval)
                                    else:
                                        ##60s is invisible ,but can find, so try other way
                                        try:
                                            CaptureTypeElement.click()
                                            sleep(1.5)
                                        except:
                                            self.logger.logger.warn(
                                                "Set %s timelapse in capture mode error***" % NumberOrTimeInterval)
                                        else:
                                            # sleep(1.5)
                                            # exit setting interface
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                else:
                                    # sleep(1.5)
                                    # exit setting interface
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                            else:
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                    else:
                        self.logger.logger.warn(
                            "Can not get current timelapse  in capture mode***")
        else:
            # exit setting interface
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})


    def SetCaptureTypeMode(self,Mode,Number=""):###has bug go to flight setting interface
        self.SwitchtoCaptureMode()
        sleep(0.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn(
                "Can not find Bottom Set Bar Element in capture mode***")
        else:
            pass
        try:
            CaptureModeElement = self.InitalDevice.driver.find_element_by_accessibility_id("MODE")
        except:
            try:
                BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'right', "element": BottomSetBarElement})
            except:
                self.logger.logger.warn(
                    "Can not find Bottom Set Bar Element in capture mode***")
            sleep(1.5)
            try:
                CaptureModeElement = self.InitalDevice.driver.find_element_by_accessibility_id("MODE")
            except Exception as e:
                self.logger.logger.warn(
                    "Can not find Capture mode setting Bar Element in capture mode***")
            else:
                try:
                    CaptureModeElement.click()
                    sleep(1.5)
                except:
                    self.logger.logger.warn("Go to capture mode setting interface in capture mode error***")
                try:
                    if Mode == "SINGLE SHOT":
                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" "+Mode)
                    else:
                        CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " + Mode+" ")
                except Exception as e:
                    #swipe setting bar
                    try:
                        CaptureTypeSwipeElement = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                    except:
                        self.logger.logger.warn("Can not find capture type settingg swipe in capture mode error***")
                    else:
                        if Mode =="SINGLE SHOT" or Mode =="BURST":
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right', "element": CaptureTypeSwipeElement})
                            sleep(1.5)
                            try:
                                if Mode == "SINGLE SHOT":
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        " " + Mode)
                                else:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        " " + Mode + " ")
                            except Exception as e:
                                self.logger.logger.warn(
                                    "Can not find the %s capture mode setting items in capture mode***"%Mode)
                            else:
                                try:
                                    CaptureTypeElement.click()
                                    sleep(1.5)
                                except:
                                    self.logger.logger.warn(
                                        "Go to  the %s capture mode setting interface in capture mode error***" % Mode)
                                else:
                                    self.setAEBBurstTimelapse(Mode,Number)

                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": CaptureTypeSwipeElement})
                            sleep(1.5)
                            try:
                                if Mode == "SINGLE SHOT":
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        " " + Mode)
                                else:
                                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        " " + Mode + " ")
                            except:
                                self.logger.logger.warn(
                                    "Can not find the %s capture mode setting items in capture mode***" % Mode)
                            else:
                                try:
                                    CaptureTypeElement.click()
                                    sleep(1.5)
                                except:
                                    self.logger.logger.warn(
                                        "Go to  the %s capture mode setting interface in capture mode error***" % Mode)
                                else:
                                    self.setAEBBurstTimelapse(Mode,Number)

                else:
                    try:
                        CaptureTypeElement.click()
                        sleep(1.5)
                    except:
                        self.logger.logger.warn(
                            "Go to  the %s capture mode setting interface in capture mode error***" % Mode)
                    else:
                        self.setAEBBurstTimelapse(Mode, Number)

        else:
            try:
                CaptureModeElement.click()
                sleep(1.5)
            except:
                self.logger.logger.warn("Go to capture mode setting interface in capture mode error***")
            try:
                if Mode == "SINGLE SHOT":
                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " + Mode)
                else:
                    CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(" " + Mode + " ")
            except Exception as e:
                # swipe setting bar
                try:
                    CaptureTypeSwipeElement = self.InitalDevice.driver.find_element_by_xpath(
                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                except:
                    self.logger.logger.warn("Can not find capture type settubg swipe in capture mode error***")
                else:
                    if Mode == "SINGLE SHOT" or Mode == "BURST":
                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                {'direction': 'right', "element": CaptureTypeSwipeElement})
                        sleep(1.5)
                        try:
                            if Mode == "SINGLE SHOT":
                                CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    " " + Mode)
                            else:
                                CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    " " + Mode + " ")
                        except Exception as e:
                            self.logger.logger.warn(
                                "Can not find the %s capture mode setting items in capture mode***" % Mode)
                        else:
                            try:
                                CaptureTypeElement.click()
                                sleep(1.5)
                            except:
                                self.logger.logger.warn(
                                    "Go to  the %s capture mode setting interface in capture mode error***" % Mode)
                            else:
                                self.setAEBBurstTimelapse(Mode, Number)

                    else:
                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                {'direction': 'left',
                                                                 "element": CaptureTypeSwipeElement})
                        sleep(1.5)
                        try:
                            if Mode == "SINGLE SHOT":
                                CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    " " + Mode)
                            else:
                                CaptureTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    " " + Mode + " ")
                        except:
                            self.logger.logger.warn(
                                "Can not find the %s capture mode setting items in capture mode***" % Mode)
                        else:
                            try:
                                CaptureTypeElement.click()
                                sleep(1.5)
                            except:
                                self.logger.logger.warn(
                                    "Go to  the %s capture mode setting interface in capture mode error***" % Mode)
                            else:
                                self.setAEBBurstTimelapse(Mode, Number)

            else:
                try:
                    CaptureTypeElement.click()
                    sleep(1.5)
                except:
                    self.logger.logger.warn(
                        "Go to  the %s capture mode setting interface in capture mode error***" % Mode)
                else:
                    self.setAEBBurstTimelapse(Mode, Number)



    def SetPictureSize(self,Size):
        # self.SwitchtoCaptureMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn(
                "Can not find Bottom Set Bar Element in capture mode***")
        else:
            pass
        try:
            PhotoSizeSetElement = self.InitalDevice.driver.find_element_by_accessibility_id("SIZE")
            sleep(1.5)
        except:
            self.logger.logger.warn(
                "Can not find Photo size setting item in capture mode***")
        else:
            try:
                PhotoSizeSetElement.click()
                sleep(1.5)
            except:
                self.logger.logger.warn(
                    "Go to the Photo size setting interface in capture mode error***")
            try:
                if Size == "4000X3000":
                    SizeElement = self.InitalDevice.driver.find_element_by_accessibility_id(Size+"(4:3)")
                else:
                    SizeElement = self.InitalDevice.driver.find_element_by_accessibility_id(Size + "(16:9)")
            except Exception as e:
                self.logger.logger.warn(
                    "Can not find Photo size setting value %s in capture mode***"%Size)
            else:
                try:
                    SizeElement.click()
                except:
                    self.logger.logger.warn(
                        "Set %s Photo size setting value in capture mode***" % Size)
                else:
                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})


    def SetPhotoFormat(self,Format):
        self.SwitchtoCaptureMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn(
                "Can not find Bottom Set Bar Element in capture mode***")
        else:
            pass
        try:
            PhotoFormatSetElement = self.InitalDevice.driver.find_element_by_accessibility_id("FORMAT")
            sleep(1.5)
        except Exception as e:
            self.logger.logger.warn(
                "Can not find format setting Element in capture mode***")
        else:
            PhotoFormatSetElement.click()
            sleep(1.5)
            try:
                if Format.find("RAW") !=-1 and Format.find("JPG") !=-1:
                    FormatElement = self.InitalDevice.driver.find_element_by_accessibility_id("RAW + JPG")
                else:
                    FormatElement = self.InitalDevice.driver.find_element_by_accessibility_id(Format)
            except:
                self.logger.logger.warn(
                    "Can not find photo format %s setting  in capture mode***"%Format)
            else:
                try:
                    FormatElement.click()
                except:
                    self.logger.logger.warn(
                        "Set %s photo format setting in capture mode error***" % Format)
                else:
                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
    def GetCurrentEV(self):
        iS0EVExist = self.InitalDevice.checkUIElementExist("± 0")
        iSN0p3EVExist = self.InitalDevice.checkUIElementExist("-0.3")
        iSN0p7EVExist = self.InitalDevice.checkUIElementExist("-0.7")
        iSN1p0EVExist = self.InitalDevice.checkUIElementExist("-1.0")
        iSN1p3EVExist = self.InitalDevice.checkUIElementExist("-1.3")
        iSN1p7EVExist = self.InitalDevice.checkUIElementExist("-1.7")
        iSN2p0EVExist = self.InitalDevice.checkUIElementExist("-2.0")
        iSN2p3EVExist = self.InitalDevice.checkUIElementExist("-2.3")
        iSN2p7EVExist = self.InitalDevice.checkUIElementExist("-2.7")
        iSN3p0EVExist = self.InitalDevice.checkUIElementExist("-3.0")
        iSP0p3EVExist = self.InitalDevice.checkUIElementExist("+0.3")
        iSP0p7EVExist = self.InitalDevice.checkUIElementExist("+0.7")
        iSP1p0EVExist = self.InitalDevice.checkUIElementExist("+1.0")
        iSP1p3EVExist = self.InitalDevice.checkUIElementExist("+1.3")
        iSP1p7EVExist = self.InitalDevice.checkUIElementExist("+1.7")
        iSP2p0EVExist = self.InitalDevice.checkUIElementExist("+2.0")
        iSP2p3EVExist = self.InitalDevice.checkUIElementExist("+2.3")
        iSP2p7EVExist = self.InitalDevice.checkUIElementExist("+2.7")
        iSP3p0EVExist = self.InitalDevice.checkUIElementExist("+3.0")
        if iS0EVExist:
            return "± 0"
        if iSN0p3EVExist:
            return "-0.3"
        if iSN0p7EVExist:
            return "-0.7"
        if iSN1p0EVExist:
            return "-1.0"
        if iSN1p3EVExist:
            return "-1.3"
        if iSN1p7EVExist:
            return "-1.7"
        if iSN2p0EVExist:
            return "-2.0"
        if iSN2p3EVExist:
            return "-2.3"
        if iSN2p7EVExist:
            return "-2.7"
        if iSN3p0EVExist:
            return "-3.0"
        if iSP0p3EVExist:
            return "+0.3"
        if iSP0p7EVExist:
            return "+0.7"
        if iSP1p0EVExist:
            return "+1.0"
        if iSP1p3EVExist:
            return "+1.3"
        if iSP1p7EVExist:
            return "+1.7"
        if iSP2p0EVExist:
            return "+2.0"
        if iSP2p3EVExist:
            return "+2.3"
        if iSP2p7EVExist:
            return "+2.7"
        if iSP3p0EVExist:
            return "+3.0"


    def SetEVInCaptureMode(self,EV):
        self.SwitchtoCaptureMode()
        sleep(1.5)
        self.setAutoExposureModeInCaptureMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'left', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn(
                "Can not find Bottom Set Bar Element in capture mode***")
        else:
            pass
        try:
            EVElement = self.InitalDevice.driver.find_element_by_accessibility_id("EV")
        except Exception as e:
            self.logger.logger.warn(
                "Can not find EV set item in capture mode***")
        else:
            CurrentEV = self.GetCurrentEV()
            try:
                EVElement.click()
                sleep(1.5)
            except:
                self.logger.logger.warn(
                    "Go to the EV setting  interface in capture mode error***")
            else:
                try:
                    EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(EV)
                    EVSetValueElementLocation = EVSetValueElement.location
                    if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                        self.logger.logger.warn(
                            "Element is not visiable***")
                        raise AttributeError
                except:
                    try:
                        EVSelectBarElement = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                    except:
                        self.logger.logger.warn(
                            "Can not find EV select bar in capture mode***")
                    else:
                        if CurrentEV != None:
                            if CurrentEV == "± 0":
                                CurrentEVValue = 0
                            else:
                                CurrentEVValue = float(CurrentEV)
                            if EV == "± 0":
                                EVValue = 0
                            else:
                                EVValue = float(EV)
                            if EVValue < CurrentEVValue:
                                swiptimes = 0
                                while True:
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'right', "element": EVSelectBarElement})
                                    sleep(1.5)
                                    try:
                                        EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(EV)
                                        EVSetValueElementLocation = EVSetValueElement.location
                                        if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                                            self.logger.logger.warn(
                                                "Element is not visiable***")
                                            raise AttributeError
                                    except:
                                        swiptimes = swiptimes + 1
                                        if swiptimes > 4:
                                            break
                                    else:
                                        try:
                                            EVSetValueElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Set %s EV in capture mode error***"%EV)
                                        else:
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                        break
                            elif EVValue > CurrentEVValue:
                                swiptimes = 0
                                while True:
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'left',
                                                                             "element": EVSelectBarElement})
                                    sleep(1.5)
                                    try:
                                        EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(EV)
                                        EVSetValueElementLocation = EVSetValueElement.location
                                        if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                                            self.logger.logger.warn(
                                                "Element is not visiable***")
                                            raise AttributeError
                                    except:
                                        swiptimes = swiptimes + 1
                                        if swiptimes > 4:
                                            break
                                    else:
                                        try:
                                            EVSetValueElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Set %s EV in capture mode error***"%EV)
                                        else:
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                        break
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                        else:
                            self.logger.logger.warn(
                                "Can not get current EV in capture mode ***" % EV)
                else:
                    try:
                        EVSetValueElement.click()
                    except:
                        try:
                            EVSelectBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find EV select bar in capture mode***")
                        else:
                            if CurrentEV!=None:
                                if CurrentEV == "± 0":
                                    CurrentEVValue = 0
                                else:
                                    CurrentEVValue = float(CurrentEV)
                                if EV == "± 0":
                                    EVValue = 0
                                else:
                                    EVValue = float(EV)
                                if EVValue < CurrentEVValue:
                                    swiptimes = 0
                                    while True:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'right',
                                                                                 "element": EVSelectBarElement})
                                        sleep(1.5)
                                        try:
                                            EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                EV)
                                            EVSetValueElementLocation = EVSetValueElement.location
                                            if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                                                self.logger.logger.warn(
                                                    "Element is not visiable***")
                                                raise AttributeError
                                        except:
                                            swiptimes = swiptimes + 1
                                            if swiptimes > 4:
                                                break
                                        else:
                                            try:
                                                EVSetValueElement.click()
                                            except:
                                                self.logger.logger.warn(
                                                    "Set %s EV in capture mode error***" % EV)
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                        {"x": 333,
                                                                                         "y": 187})
                                            break
                                elif EVValue > CurrentEVValue:
                                    swiptimes = 0
                                    while True:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": EVSelectBarElement})
                                        sleep(1.5)
                                        try:
                                            EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                EV)
                                            EVSetValueElementLocation = EVSetValueElement.location
                                            if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                                                self.logger.logger.warn(
                                                    "Element is not visiable***")
                                                raise AttributeError
                                        except:
                                            swiptimes = swiptimes + 1
                                            if swiptimes > 4:
                                                break
                                        else:
                                            try:
                                                EVSetValueElement.click()
                                            except:
                                                self.logger.logger.warn(
                                                    "Set %s EV in capture mode error***" % EV)
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                        {"x": 333,
                                                                                         "y": 187})
                                            break
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                            else:
                                self.logger.logger.warn(
                                    "Can not get current EV in capture mode ***" % EV)
                    else:
                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                {"x": 333,
                                                                 "y": 187})

    def GetCustomWBCurrentSetting(self):
        CWB2000KisExist = self.InitalDevice.checkUIElementExist(" 2000K ")
        CWB2100KisExist = self.InitalDevice.checkUIElementExist(" 2100K ")
        CWB2200KisExist = self.InitalDevice.checkUIElementExist(" 2200K ")
        CWB2300KisExist = self.InitalDevice.checkUIElementExist(" 2300K ")
        CWB2400KisExist = self.InitalDevice.checkUIElementExist(" 2400K ")
        CWB2500KisExist = self.InitalDevice.checkUIElementExist(" 2500K ")
        CWB2600KisExist = self.InitalDevice.checkUIElementExist(" 2600K ")
        CWB2700KisExist = self.InitalDevice.checkUIElementExist(" 2700K ")
        CWB2800KisExist = self.InitalDevice.checkUIElementExist(" 2800K ")
        CWB2900KisExist = self.InitalDevice.checkUIElementExist(" 2900K ")
        CWB3000KisExist = self.InitalDevice.checkUIElementExist(" 3000K ")
        CWB3100KisExist = self.InitalDevice.checkUIElementExist(" 3100K ")
        CWB3200KisExist = self.InitalDevice.checkUIElementExist(" 3200K ")
        CWB3300KisExist = self.InitalDevice.checkUIElementExist(" 3300K ")
        CWB3400KisExist = self.InitalDevice.checkUIElementExist(" 3400K ")
        CWB3500KisExist = self.InitalDevice.checkUIElementExist(" 3500K ")
        CWB3600KisExist = self.InitalDevice.checkUIElementExist(" 3600K ")
        CWB3700KisExist = self.InitalDevice.checkUIElementExist(" 3700K ")
        CWB3800KisExist = self.InitalDevice.checkUIElementExist(" 3800K ")
        CWB3900KisExist = self.InitalDevice.checkUIElementExist(" 3900K ")
        CWB4000KisExist = self.InitalDevice.checkUIElementExist(" 4000K ")
        CWB4100KisExist = self.InitalDevice.checkUIElementExist(" 4100K ")
        CWB4200KisExist = self.InitalDevice.checkUIElementExist(" 4200K ")
        CWB4300KisExist = self.InitalDevice.checkUIElementExist(" 4300K ")
        CWB4400KisExist = self.InitalDevice.checkUIElementExist(" 4400K ")
        CWB4500KisExist = self.InitalDevice.checkUIElementExist(" 4500K ")
        CWB4600KisExist = self.InitalDevice.checkUIElementExist(" 4600K ")
        CWB4700KisExist = self.InitalDevice.checkUIElementExist(" 4700K ")
        CWB4800KisExist = self.InitalDevice.checkUIElementExist(" 4800K ")
        CWB4900KisExist = self.InitalDevice.checkUIElementExist(" 4900K ")
        CWB5000KisExist = self.InitalDevice.checkUIElementExist(" 5000K ")
        CWB5100KisExist = self.InitalDevice.checkUIElementExist(" 5100K ")
        CWB5200KisExist = self.InitalDevice.checkUIElementExist(" 5200K ")
        CWB5300KisExist = self.InitalDevice.checkUIElementExist(" 5300K ")
        CWB5400KisExist = self.InitalDevice.checkUIElementExist(" 5400K ")
        CWB5500KisExist = self.InitalDevice.checkUIElementExist(" 5500K ")
        CWB5600KisExist = self.InitalDevice.checkUIElementExist(" 5600K ")
        CWB5700KisExist = self.InitalDevice.checkUIElementExist(" 5700K ")
        CWB5800KisExist = self.InitalDevice.checkUIElementExist(" 5800K ")
        CWB5900KisExist = self.InitalDevice.checkUIElementExist(" 5900K ")
        CWB6000KisExist = self.InitalDevice.checkUIElementExist(" 6000K ")
        CWB6100KisExist = self.InitalDevice.checkUIElementExist(" 6100K ")
        CWB6200KisExist = self.InitalDevice.checkUIElementExist(" 6200K ")
        CWB6300KisExist = self.InitalDevice.checkUIElementExist(" 6300K ")
        CWB6400KisExist = self.InitalDevice.checkUIElementExist(" 6400K ")
        CWB6500KisExist = self.InitalDevice.checkUIElementExist(" 6500K ")
        CWB6600KisExist = self.InitalDevice.checkUIElementExist(" 6600K ")
        CWB6700KisExist = self.InitalDevice.checkUIElementExist(" 6700K ")
        CWB6800KisExist = self.InitalDevice.checkUIElementExist(" 6800K ")
        CWB6900KisExist = self.InitalDevice.checkUIElementExist(" 6900K ")
        CWB7000KisExist = self.InitalDevice.checkUIElementExist(" 7000K ")
        CWB7100KisExist = self.InitalDevice.checkUIElementExist(" 7100K ")
        CWB7200KisExist = self.InitalDevice.checkUIElementExist(" 7200K ")
        CWB7300KisExist = self.InitalDevice.checkUIElementExist(" 7300K ")
        CWB7400KisExist = self.InitalDevice.checkUIElementExist(" 7400K ")
        CWB7500KisExist = self.InitalDevice.checkUIElementExist(" 7500K ")
        CWB7600KisExist = self.InitalDevice.checkUIElementExist(" 7600K ")
        CWB7700KisExist = self.InitalDevice.checkUIElementExist(" 7700K ")
        CWB7800KisExist = self.InitalDevice.checkUIElementExist(" 7800K ")
        CWB7900KisExist = self.InitalDevice.checkUIElementExist(" 7900K ")
        CWB8000KisExist = self.InitalDevice.checkUIElementExist(" 8000K ")
        CWB8100KisExist = self.InitalDevice.checkUIElementExist(" 8100K ")
        CWB8200KisExist = self.InitalDevice.checkUIElementExist(" 8200K ")
        CWB8300KisExist = self.InitalDevice.checkUIElementExist(" 8300K ")
        CWB8400KisExist = self.InitalDevice.checkUIElementExist(" 8400K ")
        CWB8500KisExist = self.InitalDevice.checkUIElementExist(" 8500K ")
        CWB8600KisExist = self.InitalDevice.checkUIElementExist(" 8600K ")
        CWB8700KisExist = self.InitalDevice.checkUIElementExist(" 8700K ")
        CWB8800KisExist = self.InitalDevice.checkUIElementExist(" 8800K ")
        CWB8900KisExist = self.InitalDevice.checkUIElementExist(" 8900K ")
        CWB9000KisExist = self.InitalDevice.checkUIElementExist(" 9000K ")
        CWB9100KisExist = self.InitalDevice.checkUIElementExist(" 9100K ")
        CWB9200KisExist = self.InitalDevice.checkUIElementExist(" 9200K ")
        CWB9300KisExist = self.InitalDevice.checkUIElementExist(" 9300K ")
        CWB9400KisExist = self.InitalDevice.checkUIElementExist(" 9400K ")
        CWB9500KisExist = self.InitalDevice.checkUIElementExist(" 9500K ")
        CWB9600KisExist = self.InitalDevice.checkUIElementExist(" 9600K ")
        CWB9700KisExist = self.InitalDevice.checkUIElementExist(" 9700K ")
        CWB9800KisExist = self.InitalDevice.checkUIElementExist(" 9800K ")
        CWB9900KisExist = self.InitalDevice.checkUIElementExist(" 9900K ")
        CWB10000KisExist = self.InitalDevice.checkUIElementExist(" 10000K ")
        if CWB2000KisExist:
            return " 2000K "
        if CWB2100KisExist:
            return " 2100K "
        if CWB2200KisExist:
            return " 2200K "
        if CWB2300KisExist:
            return " 2300K "
        if CWB2400KisExist:
            return " 2400K "
        if CWB2500KisExist:
            return " 2500K "
        if CWB2600KisExist:
            return " 2600K "
        if CWB2700KisExist:
            return " 2700K "
        if CWB2800KisExist:
            return " 2800K "
        if CWB2900KisExist:
            return " 2900K "
        if CWB3000KisExist:
            return " 3000K "
        if CWB3100KisExist:
            return " 3100K "
        if CWB3200KisExist:
            return " 3200K "
        if CWB3300KisExist:
            return " 3300K "
        if CWB3400KisExist:
            return " 3400K "
        if CWB3500KisExist:
            return " 3500K "
        if CWB3600KisExist:
            return " 3600K "
        if CWB3700KisExist:
            return " 3700K "
        if CWB3800KisExist:
            return " 3800K "
        if CWB3900KisExist:
            return " 3900K "
        if CWB4000KisExist:
            return " 4000K "
        if CWB4100KisExist:
            return " 4100K "
        if CWB4200KisExist:
            return " 4200K "
        if CWB4300KisExist:
            return " 4300K "
        if CWB4400KisExist:
            return " 4400K "
        if CWB4500KisExist:
            return " 4500K "
        if CWB4600KisExist:
            return " 4600K "
        if CWB4700KisExist:
            return " 4700K "
        if CWB4800KisExist:
            return " 4800K "
        if CWB4900KisExist:
            return " 4900K "
        if CWB5000KisExist:
            return " 5000K "
        if CWB5100KisExist:
            return " 5100K "
        if CWB5200KisExist:
            return " 5200K "
        if CWB5300KisExist:
            return " 5300K "
        if CWB5400KisExist:
            return " 5400K "
        if CWB5500KisExist:
            return " 5500K "
        if CWB5600KisExist:
            return " 5600K "
        if CWB5700KisExist:
            return " 5700K "
        if CWB5800KisExist:
            return " 5800K "
        if CWB5900KisExist:
            return " 5900K "
        if CWB6000KisExist:
            return " 6000K "
        if CWB6100KisExist:
            return " 6100K "
        if CWB6200KisExist:
            return " 6200K "
        if CWB6300KisExist:
            return " 6300K "
        if CWB6400KisExist:
            return " 6400K "
        if CWB6500KisExist:
            return " 6500K "
        if CWB6600KisExist:
            return " 6600K "
        if CWB6700KisExist:
            return " 6700K "
        if CWB6800KisExist:
            return " 6800K "
        if CWB6900KisExist:
            return " 6900K "
        if CWB7000KisExist:
            return " 7000K "
        if CWB7100KisExist:
            return " 7100K "
        if CWB7200KisExist:
            return " 7200K "
        if CWB7300KisExist:
            return " 7300K "
        if CWB7400KisExist:
            return " 7400K "
        if CWB7500KisExist:
            return " 7500K "
        if CWB7600KisExist:
            return " 7600K "
        if CWB7700KisExist:
            return " 7700K "
        if CWB7800KisExist:
            return " 7800K "
        if CWB7900KisExist:
            return " 7900K "
        if CWB8000KisExist:
            return " 8000K "
        if CWB8100KisExist:
            return " 8100K "
        if CWB8200KisExist:
            return " 8200K "
        if CWB8300KisExist:
            return " 8300K "
        if CWB8400KisExist:
            return " 8400K "
        if CWB8500KisExist:
            return " 8500K "
        if CWB8600KisExist:
            return " 8600K "
        if CWB8700KisExist:
            return " 8700K "
        if CWB8800KisExist:
            return " 8800K "
        if CWB8900KisExist:
            return " 8900K "
        if CWB9000KisExist:
            return " 9000K "
        if CWB9100KisExist:
            return " 9100K "
        if CWB9200KisExist:
            return " 9200K "
        if CWB9300KisExist:
            return " 9300K "
        if CWB9400KisExist:
            return " 9400K "
        if CWB9500KisExist:
            return " 9500K "
        if CWB9600KisExist:
            return " 9600K "
        if CWB9700KisExist:
            return " 9700K "
        if CWB9800KisExist:
            return " 9800K "
        if CWB9900KisExist:
            return " 9900K "
        if CWB10000KisExist:
            return " 10000K "

    def SetWhiteBalanceInCaptureMode(self,WB=None,ColorTempeture=None): #WB = 'Custom' or 'custom'
        self.SwitchtoCaptureMode()
        sleep(1.5)
        try:
            WBElement = self.InitalDevice.driver.find_element_by_accessibility_id("WB")
            if not WBElement.is_displayed():
                raise AttributeError
        except:
            try:
                BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                        {'direction': 'left', "element": BottomSetBarElement})
                sleep(1.5)
            except:
                self.logger.logger.warn(
                    "Can not find Bottom Set Bar Element in capture mode***")
            else:
                try:
                    WBElement = self.InitalDevice.driver.find_element_by_accessibility_id("WB")
                    if not WBElement.is_displayed():
                        raise AttributeError
                except:
                    self.logger.logger.warn(
                        "Can not find WB setting item in capture mode***")
                else:
                    try:
                        WBElement.click()
                        sleep(1.5)
                    except:
                        self.logger.logger.warn(
                            "Go to the WB setting interface in capture mode error***")
                    else:
                        if WB == 'Custom' or WB == 'custom':
                            try:
                                WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": WBItemBarElement})
                                sleep(1.5)

                            except:
                                self.logger.logger.warn(
                                    "Can not find WB select swipe bar in capture mode***")
                            else:
                                CustomCurrentSet = self.GetCustomWBCurrentSetting()
                                try:
                                    CustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        CustomCurrentSet)
                                except Exception as e:
                                    self.logger.logger.warn(
                                        "Can not find %s WB setting value in capture mode***" % CustomCurrentSet)
                                else:
                                    try:
                                        CustomWBElement.click()
                                        sleep(1)
                                        try:
                                            CustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                CustomCurrentSet)
                                        except:
                                            pass
                                        else:
                                            CustomWBElement.click()
                                            sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Go to the custom WB setting interface in capture mode error***")
                                    else:
                                        try:
                                            SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                ColorTempeture)
                                        except:
                                            if CustomCurrentSet!= None:
                                                CustomCurrentSetValue = int(
                                                    CustomCurrentSet.replace("K", "").replace(" ", ""))
                                                ColorTempetureValue = int(ColorTempeture.replace("K", "").replace(" ", ""))
                                                try:
                                                    CWBSelectBar = self.InitalDevice.driver.find_element_by_xpath(
                                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]"
                                                        "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                                        "/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]"
                                                        "/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find custom WB select swipe bar in capture mode***")
                                                else:
                                                    if ColorTempetureValue < CustomCurrentSetValue:
                                                        swiptimes = 0
                                                        while True:
                                                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                                    {
                                                                                                        'direction': 'right',
                                                                                                        "element": CWBSelectBar})
                                                            sleep(1.5)
                                                            try:
                                                                SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                    ColorTempeture)
                                                            except:
                                                                swiptimes = swiptimes + 1
                                                                if swiptimes > 16:
                                                                    break
                                                            else:
                                                                try:
                                                                    SetCustomWBElement.click()
                                                                except Exception as e:
                                                                    self.logger.logger.warn(
                                                                        "Can not find the WB setting item***")
                                                                else:
                                                                    try:
                                                                        backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                            "Back")
                                                                    except Exception as e:
                                                                        self.logger.logger.warn(
                                                                            "Can not find the back control button***")
                                                                    else:
                                                                        backElement.click()
                                                                    self.InitalDevice.driver.execute_script(
                                                                        "mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                                                    break
                                                    elif ColorTempetureValue > CustomCurrentSetValue:
                                                        swiptimes = 0
                                                        while True:
                                                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                                    {
                                                                                                        'direction': 'left',
                                                                                                        "element": CWBSelectBar})
                                                            sleep(1.5)
                                                            try:
                                                                SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                    ColorTempeture)
                                                            except:
                                                                swiptimes = swiptimes + 1
                                                                if swiptimes > 16:
                                                                    break
                                                            else:
                                                                try:
                                                                    SetCustomWBElement.click()
                                                                except Exception as e:
                                                                    self.logger.logger.warn(
                                                                        "Can not find the WB setting item***")
                                                                else:
                                                                    try:
                                                                        backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                            "Back")
                                                                    except Exception as e:
                                                                        self.logger.logger.warn(
                                                                            "Can not find the back control button***")
                                                                    else:
                                                                        backElement.click()
                                                                    self.InitalDevice.driver.execute_script(
                                                                        "mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                                                    break
                                                    else:
                                                        self.InitalDevice.driver.execute_script(
                                                            "mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                                            else:
                                                self.logger.logger.warn(
                                                    "Can not get current  custom WB setting***")

                                        else:
                                            try:
                                                SetCustomWBElement.click()
                                            except:
                                                if CustomCurrentSet!= None:
                                                    CustomCurrentSetValue = int(
                                                        CustomCurrentSet.replace("K", "").replace(" ", ""))
                                                    ColorTempetureValue = int(
                                                        ColorTempeture.replace("K", "").replace(" ", ""))
                                                    try:
                                                        CWBSelectBar = self.InitalDevice.driver.find_element_by_xpath(
                                                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]"
                                                            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                                            "/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]"
                                                            "/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Can not find custom WB select swipe bar in capture mode***")
                                                    else:
                                                        if ColorTempetureValue < CustomCurrentSetValue:
                                                            swiptimes = 0
                                                            while True:
                                                                self.InitalDevice.driver.execute_script(
                                                                    "mobile: swipe",
                                                                    {
                                                                        'direction': 'right',
                                                                        "element": CWBSelectBar})
                                                                sleep(1.5)
                                                                try:
                                                                    SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                        ColorTempeture)
                                                                except:
                                                                    swiptimes = swiptimes + 1
                                                                    if swiptimes > 16:
                                                                        break
                                                                else:
                                                                    try:
                                                                        SetCustomWBElement.click()
                                                                    except Exception as e:
                                                                        self.logger.logger.warn(
                                                                            "Can not find the WB setting item***")
                                                                    else:
                                                                        try:
                                                                            backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                                "Back")
                                                                        except Exception as e:
                                                                            self.logger.logger.warn(
                                                                                "Can not find the back control button***")
                                                                        else:
                                                                            try:
                                                                                backElement.click()
                                                                            except:
                                                                                self.logger.logger.warn(
                                                                                    "Click the back control error***")
                                                                            else:
                                                                                self.InitalDevice.driver.execute_script(
                                                                                    "mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                                                        break
                                                        elif ColorTempetureValue > CustomCurrentSetValue:
                                                            swiptimes = 0
                                                            while True:
                                                                self.InitalDevice.driver.execute_script(
                                                                    "mobile: swipe",
                                                                    {
                                                                        'direction': 'left',
                                                                        "element": CWBSelectBar})
                                                                sleep(1.5)
                                                                try:
                                                                    SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                        ColorTempeture)
                                                                except:
                                                                    swiptimes = swiptimes + 1
                                                                    if swiptimes > 16:
                                                                        break
                                                                else:
                                                                    try:
                                                                        SetCustomWBElement.click()
                                                                    except Exception as e:
                                                                        self.logger.logger.warn(
                                                                            "Can not find the WB setting item***")
                                                                    else:
                                                                        try:
                                                                            backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                                "Back")
                                                                        except Exception as e:
                                                                            self.logger.logger.warn(
                                                                                "Can not find the back control button***")
                                                                        else:
                                                                            try:
                                                                                backElement.click()
                                                                            except:
                                                                                self.logger.logger.warn(
                                                                                    "Click the back control error***")
                                                                            else:
                                                                                self.InitalDevice.driver.execute_script(
                                                                                    "mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                                                        break
                                                        else:
                                                            self.InitalDevice.driver.execute_script(
                                                                "mobile: tap",
                                                                {"x": 333,
                                                                 "y": 187})
                                                else:
                                                    self.logger.logger.warn(
                                                        "Can not get current  custom WB setting***")
                                            else:
                                                try:
                                                    backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        "Back")
                                                except Exception as e:
                                                    self.logger.logger.warn("Can not find the back control button***")
                                                else:
                                                    try:
                                                        backElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Click the back control error***")
                                                    else:
                                                        self.InitalDevice.driver.execute_script(
                                                            "mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                        else:
                            try:
                                SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(WB)
                            except:
                                try:
                                    WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'right',
                                                                             "element": WBItemBarElement})
                                    sleep(1.5)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find WB select swipe bar in capture mode***")
                                else:
                                    try:
                                        SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(WB)
                                    except:
                                        try:
                                            WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                    {'direction': 'left',
                                                                                     "element": WBItemBarElement})
                                            sleep(1.5)
                                        except:
                                            self.logger.logger.warn(
                                                "Can not find WB select swipe bar in capture mode***")
                                        else:
                                            try:
                                                SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                    WB)
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the %s WB item in capture mode***" % WB)
                                            else:
                                                try:
                                                    SetWBItem.click()
                                                except:
                                                    self.logger.logger.warn(
                                                        "Set the %s WB in capture mode error***" % WB)
                                                else:
                                                    self.InitalDevice.driver.execute_script(
                                                        "mobile: tap",
                                                        {"x": 333,
                                                         "y": 187})

                                    else:
                                        try:
                                            SetWBItem.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Set the %s WB in capture mode error***" % WB)
                                        else:
                                            self.InitalDevice.driver.execute_script(
                                                "mobile: tap",
                                                {"x": 333,
                                                 "y": 187})
                            else:
                                try:
                                    SetWBItem.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the %s WB in capture mode error***" % WB)
                                else:
                                    self.InitalDevice.driver.execute_script(
                                        "mobile: tap",
                                        {"x": 333,
                                         "y": 187})
        else:
            WBElement.click()
            sleep(1.5)
            if WB == 'Custom' or WB == 'custom':
                try:
                    WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                            {'direction': 'left',
                                                             "element": WBItemBarElement})
                    sleep(1.5)

                except:
                    self.logger.logger.warn(
                        "Can not find WB select swipe bar in capture mode***")
                else:
                    CustomCurrentSet = self.GetCustomWBCurrentSetting()
                    try:
                        CustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            CustomCurrentSet)
                    except Exception as e:
                        self.logger.logger.warn(
                            "Can not find %s WB setting value in capture mode***" % CustomCurrentSet)
                    else:
                        try:
                            CustomWBElement.click()
                            sleep(1)
                            try:
                                CustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    CustomCurrentSet)
                            except:
                                pass
                            else:
                                CustomWBElement.click()
                                sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Go to the custom WB setting interface in capture mode error***")
                        else:
                            try:
                                SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    ColorTempeture)
                            except:
                                if CustomCurrentSet != None:
                                    CustomCurrentSetValue = int(CustomCurrentSet.replace("K", "").replace(" ", ""))
                                    ColorTempetureValue = int(ColorTempeture.replace("K", "").replace(" ", ""))
                                    try:
                                        CWBSelectBar = self.InitalDevice.driver.find_element_by_xpath(
                                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]"
                                            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                            "/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]"
                                            "/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    except:
                                        self.logger.logger.warn(
                                            "Can not find custom WB select swipe bar in capture mode***")
                                    else:
                                        if ColorTempetureValue < CustomCurrentSetValue:
                                            swiptimes = 0
                                            while True:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {
                                                                                            'direction': 'right',
                                                                                            "element": CWBSelectBar})
                                                sleep(1.5)
                                                try:
                                                    SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        ColorTempeture)
                                                except:
                                                    swiptimes = swiptimes + 1
                                                    if swiptimes > 16:
                                                        break
                                                else:
                                                    try:
                                                        SetCustomWBElement.click()
                                                    except Exception as e:
                                                        self.logger.logger.warn(
                                                            "Can not find the WB setting item***")
                                                    else:
                                                        try:
                                                            backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except Exception as e:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            backElement.click()
                                                        self.InitalDevice.driver.execute_script(
                                                            "mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                                                        break
                                        elif ColorTempetureValue > CustomCurrentSetValue:
                                            swiptimes = 0
                                            while True:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {
                                                                                            'direction': 'left',
                                                                                            "element": CWBSelectBar})
                                                sleep(1.5)
                                                try:
                                                    SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        ColorTempeture)
                                                except:
                                                    swiptimes = swiptimes + 1
                                                    if swiptimes > 16:
                                                        break
                                                else:
                                                    try:
                                                        SetCustomWBElement.click()
                                                    except Exception as e:
                                                        self.logger.logger.warn(
                                                            "Can not find the WB setting item***")
                                                    else:
                                                        try:
                                                            backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except Exception as e:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            backElement.click()
                                                        self.InitalDevice.driver.execute_script(
                                                            "mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                                                        break
                                        else:
                                            self.InitalDevice.driver.execute_script(
                                                "mobile: tap",
                                                {"x": 333,
                                                 "y": 187})
                                else:
                                    self.logger.logger.warn(
                                        "Can not get current  custom WB setting***")

                            else:
                                try:
                                    SetCustomWBElement.click()
                                except:
                                    if CustomCurrentSet != None:
                                        CustomCurrentSetValue = int(
                                            CustomCurrentSet.replace("K", "").replace(" ", ""))
                                        ColorTempetureValue = int(
                                            ColorTempeture.replace("K", "").replace(" ", ""))
                                        try:
                                            CWBSelectBar = self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]"
                                                "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                                "/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]"
                                                "/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                        except:
                                            self.logger.logger.warn(
                                                "Can not find custom WB select swipe bar in capture mode***")
                                        else:
                                            if ColorTempetureValue < CustomCurrentSetValue:
                                                swiptimes = 0
                                                while True:
                                                    self.InitalDevice.driver.execute_script(
                                                        "mobile: swipe",
                                                        {
                                                            'direction': 'right',
                                                            "element": CWBSelectBar})
                                                    sleep(1.5)
                                                    try:
                                                        SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                            ColorTempeture)
                                                    except:
                                                        swiptimes = swiptimes + 1
                                                        if swiptimes > 16:
                                                            break
                                                    else:
                                                        try:
                                                            SetCustomWBElement.click()
                                                        except Exception as e:
                                                            self.logger.logger.warn(
                                                                "Can not find the WB setting item***")
                                                        else:
                                                            try:
                                                                backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                    "Back")
                                                            except Exception as e:
                                                                self.logger.logger.warn(
                                                                    "Can not find the back control button***")
                                                            else:
                                                                try:
                                                                    backElement.click()
                                                                except:
                                                                    self.logger.logger.warn(
                                                                        "Click the back control error***")
                                                                else:
                                                                    self.InitalDevice.driver.execute_script(
                                                                        "mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                                            break
                                            elif ColorTempetureValue > CustomCurrentSetValue:
                                                swiptimes = 0
                                                while True:
                                                    self.InitalDevice.driver.execute_script(
                                                        "mobile: swipe",
                                                        {
                                                            'direction': 'left',
                                                            "element": CWBSelectBar})
                                                    sleep(1.5)
                                                    try:
                                                        SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                            ColorTempeture)
                                                    except:
                                                        swiptimes = swiptimes + 1
                                                        if swiptimes > 16:
                                                            break
                                                    else:
                                                        try:
                                                            SetCustomWBElement.click()
                                                        except Exception as e:
                                                            self.logger.logger.warn(
                                                                "Can not find the WB setting item***")
                                                        else:
                                                            try:
                                                                backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                    "Back")
                                                            except Exception as e:
                                                                self.logger.logger.warn(
                                                                    "Can not find the back control button***")
                                                            else:
                                                                try:
                                                                    backElement.click()
                                                                except:
                                                                    self.logger.logger.warn(
                                                                        "Click the back control error***")
                                                                else:
                                                                    self.InitalDevice.driver.execute_script(
                                                                        "mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                                            break
                                            else:
                                                self.InitalDevice.driver.execute_script(
                                                    "mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})
                                    else:
                                        self.logger.logger.warn(
                                            "Can not get current  custom WB setting***")

                                else:
                                    try:
                                        backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                            "Back")
                                    except Exception as e:
                                        self.logger.logger.warn("Can not find the back control button***")
                                    else:
                                        try:
                                            backElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Click the back control error***")
                                        else:
                                            self.InitalDevice.driver.execute_script(
                                                "mobile: tap",
                                                {"x": 333,
                                                 "y": 187})
            else:
                try:
                    SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(WB)
                except:
                    try:
                        WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                {'direction': 'right',
                                                                 "element": WBItemBarElement})
                        sleep(1.5)
                    except:
                        self.logger.logger.warn(
                            "Can not find WB select swipe bar in capture mode***")
                    else:
                        try:
                            SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(WB)
                        except:
                            try:
                                WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": WBItemBarElement})
                                sleep(1.5)
                            except:
                                self.logger.logger.warn(
                                    "Can not find WB select swipe bar in capture mode***")
                            else:
                                try:
                                    SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        WB)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the %s WB item in capture mode***" % WB)
                                else:
                                    try:
                                        SetWBItem.click()
                                    except:
                                        self.logger.logger.warn(
                                            "Set the %s WB in capture mode error***" % WB)
                                    else:
                                        self.InitalDevice.driver.execute_script(
                                            "mobile: tap",
                                            {"x": 333,
                                             "y": 187})

                        else:
                            try:
                                SetWBItem.click()
                            except:
                                self.logger.logger.warn(
                                    "Set the %s WB in capture mode error***" % WB)
                            else:
                                self.InitalDevice.driver.execute_script(
                                    "mobile: tap",
                                    {"x": 333,
                                     "y": 187})
                else:
                    try:
                        SetWBItem.click()
                    except:
                        self.logger.logger.warn(
                            "Set the %s WB in capture mode error***" % WB)
                    else:
                        self.InitalDevice.driver.execute_script(
                            "mobile: tap",
                            {"x": 333,
                             "y": 187})



    def SetColorInCaptureMode(self,Color):
        self.SwitchtoCaptureMode()
        sleep(1.5)
        try:
            ColorSelectElement = self.InitalDevice.driver.find_element_by_accessibility_id("COLOR")
        except:
            try:
                BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                        {'direction': 'left', "element": BottomSetBarElement})
                sleep(1.5)
            except:
                self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
            else:
                try:
                    ColorSelectElement = self.InitalDevice.driver.find_element_by_accessibility_id("COLOR")
                except:
                    self.logger.logger.warn(
                        "Can not find the Color setting item, maybe it is not on the camera interface***")
                else:
                    if not self.InitalDevice.checkUIElementExist("Btn console help normal"):
                        try:
                            ColorSelectElement.click()
                            sleep(1.5)
                        except:
                            self.logger.logger.warn("Select the Color Error***")
                        else:
                            if Color == "DREAM" or Color == "CLASSIC" or Color == "NOSTALGIC":
                                try:
                                    ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                                except:
                                    self.logger.logger.warn("Can not find Color swipe bar***")
                                else:
                                    try:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                    except:
                                        self.logger.logger.warn("Swipe color  bar Error***")
                                    else:
                                        sleep(1.5)
                                try:
                                    ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                                except:
                                    self.logger.logger.warn("Find the %s setting item error***" % Color)
                                else:
                                    try:
                                        ColorSetElement.click()
                                    except:
                                        self.logger.logger.warn("Set %s setting error***" % Color)
                                    else:
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            elif Color == "NONE" or Color == "LOG" or Color == "VIVID":
                                try:
                                    ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                                except:
                                    self.logger.logger.warn("Can not find Color swipe bar***")
                                else:
                                    try:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'right',
                                                                                 "element": ColorSwipeBar})
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'right',
                                                                                 "element": ColorSwipeBar})
                                    except:
                                        self.logger.logger.warn("Swipe color  bar Error***")
                                    else:
                                        sleep(1.5)
                                try:
                                    ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                                except:
                                    self.logger.logger.warn("Find the %s setting item error***" % Color)
                                else:
                                    try:
                                        ColorSetElement.click()
                                    except:
                                        self.logger.logger.warn("Set %s setting error***" % Color)
                                    else:
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            else:
                                try:
                                    ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                                except:
                                    self.logger.logger.warn("Can not find Color swipe bar***")
                                else:
                                    try:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'right',
                                                                                 "element": ColorSwipeBar})
                                    except:
                                        self.logger.logger.warn("Swipe color  bar Error***")
                                    else:
                                        sleep(1.5)
                                try:
                                    ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                                except:
                                    self.logger.logger.warn("Find the %s setting item error***" % Color)
                                else:
                                    try:
                                        ColorSetElement.click()
                                    except:
                                        self.logger.logger.warn("Set %s setting error***" % Color)
                                    else:
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                    else:
                        try:
                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                        except:
                            try:
                                ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                            except:
                                self.logger.logger.warn("Can not find Color swipe bar***")
                            else:
                                swiptimes = 0
                                while True:
                                    try:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                        sleep(1.5)
                                    except:
                                        pass
                                    else:
                                        try:
                                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                Color)
                                        except:
                                            swiptimes = swiptimes + 1
                                            if swiptimes > 3:
                                                break
                                        else:
                                            try:
                                                ColorSetElement.click()
                                            except:
                                                self.logger.logger.warn("Set the Color %s Error***" % Color)
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                        {"x": 333,
                                                                                         "y": 187})
                                                break
                                if swiptimes > 3:
                                    Otherswiptimes = 0
                                    while True:
                                        try:
                                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                    {'direction': 'right',
                                                                                     "element": ColorSwipeBar})
                                            sleep(1.5)
                                        except:
                                            pass
                                        else:
                                            try:
                                                ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                    Color)
                                            except:
                                                Otherswiptimes = Otherswiptimes + 1
                                                if Otherswiptimes > 3:
                                                    break
                                            else:
                                                try:
                                                    ColorSetElement.click()
                                                except:
                                                    self.logger.logger.warn("Set the Color %s Error***" % Color)
                                                else:
                                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                            {"x": 333,
                                                                                             "y": 187})
                                                    break

                        else:
                            try:
                                ColorSetElement.click()
                            except:
                                self.logger.logger.warn("Set the Color %s Error***" % Color)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
        else:
            if not self.InitalDevice.checkUIElementExist(
                    "Btn console help normal"):  # if color select interface exists,do not click the Color Select Item bar
                try:
                    ColorSelectElement.click()
                    sleep(1.5)
                except:
                    self.logger.logger.warn("Select the Color Error***")
                else:
                    if Color == "DREAM" or Color == "CLASSIC" or Color == "NOSTALGIC":
                        try:
                            ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                        except:
                            self.logger.logger.warn("Can not find Color swipe bar***")
                        else:
                            try:
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": ColorSwipeBar})
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": ColorSwipeBar})
                            except:
                                self.logger.logger.warn("Swipe color  bar Error***")
                            else:
                                sleep(1.5)
                        try:
                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                        except:
                            self.logger.logger.warn("Find the %s setting item error***" % Color)
                        else:
                            try:
                                ColorSetElement.click()
                            except:
                                self.logger.logger.warn("Set %s setting error***" % Color)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                    elif Color == "NONE" or Color == "LOG" or Color == "VIVID":
                        try:
                            ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                        except:
                            self.logger.logger.warn("Can not find Color swipe bar***")
                        else:
                            try:
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": ColorSwipeBar})
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": ColorSwipeBar})
                            except:
                                self.logger.logger.warn("Swipe color  bar Error***")
                            else:
                                sleep(1.5)
                        try:
                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                        except:
                            self.logger.logger.warn("Find the %s setting item error***" % Color)
                        else:
                            try:
                                ColorSetElement.click()
                            except:
                                self.logger.logger.warn("Set %s setting error***" % Color)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                    else:
                        try:
                            ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                        except:
                            self.logger.logger.warn("Can not find Color swipe bar***")
                        else:
                            try:
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": ColorSwipeBar})
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": ColorSwipeBar})
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": ColorSwipeBar})
                            except:
                                self.logger.logger.warn("Swipe color  bar Error***")
                            else:
                                sleep(1.5)
                        try:
                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                        except:
                            self.logger.logger.warn("Find the %s setting item error***" % Color)
                        else:
                            try:
                                ColorSetElement.click()
                            except:
                                self.logger.logger.warn("Set %s setting error***" % Color)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})

            else:
                if Color == "DREAM" or Color == "CLASSIC" or Color == "NOSTALGIC":
                    try:
                        ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                    except:
                        self.logger.logger.warn("Can not find Color swipe bar***")
                    else:
                        try:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": ColorSwipeBar})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": ColorSwipeBar})
                        except:
                            self.logger.logger.warn("Swipe color  bar Error***")
                        else:
                            sleep(1.5)
                    try:
                        ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                    except:
                        self.logger.logger.warn("Find the %s setting item error***" % Color)
                    else:
                        try:
                            ColorSetElement.click()
                        except:
                            self.logger.logger.warn("Set %s setting error***" % Color)
                        else:
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
                elif Color == "NONE" or Color == "LOG" or Color == "VIVID":
                    try:
                        ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                    except:
                        self.logger.logger.warn("Can not find Color swipe bar***")
                    else:
                        try:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": ColorSwipeBar})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": ColorSwipeBar})
                        except:
                            self.logger.logger.warn("Swipe color  bar Error***")
                        else:
                            sleep(1.5)
                    try:
                        ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                    except:
                        self.logger.logger.warn("Find the %s setting item error***" % Color)
                    else:
                        try:
                            ColorSetElement.click()
                        except:
                            self.logger.logger.warn("Set %s setting error***" % Color)
                        else:
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
                else:
                    try:
                        ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                    except:
                        self.logger.logger.warn("Can not find Color swipe bar***")
                    else:
                        try:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": ColorSwipeBar})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": ColorSwipeBar})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": ColorSwipeBar})
                        except:
                            self.logger.logger.warn("Swipe color  bar Error***")
                        else:
                            sleep(1.5)
                    try:
                        ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                    except:
                        self.logger.logger.warn("Find the %s setting item error***" % Color)
                    else:
                        try:
                            ColorSetElement.click()
                        except:
                            self.logger.logger.warn("Set %s setting error***" % Color)
                        else:
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})

    def GetCurrentSharpnessSetting(self):
        isSharpnessP1 = self.InitalDevice.checkUIElementExist(" SHARPNESS +1 ")
        isSharpnessP2 = self.InitalDevice.checkUIElementExist(" SHARPNESS +2 ")
        isSharpnessP3 = self.InitalDevice.checkUIElementExist(" SHARPNESS +3 ")
        isSharpness0 = self.InitalDevice.checkUIElementExist(" SHARPNESS ±0 ")
        isSharpnessN1 = self.InitalDevice.checkUIElementExist(" SHARPNESS -1 ")
        isSharpnessN2 = self.InitalDevice.checkUIElementExist(" SHARPNESS -2 ")
        isSharpnessN3 = self.InitalDevice.checkUIElementExist(" SHARPNESS -3 ")
        if isSharpnessP1:
            return " SHARPNESS +1 "
        if isSharpnessP2:
            return " SHARPNESS +2 "
        if isSharpnessP3:
            return " SHARPNESS +3 "
        if isSharpness0:
            return " SHARPNESS ±0 "
        if isSharpnessN1:
            return " SHARPNESS -1 "
        if isSharpnessN2:
            return " SHARPNESS -2 "
        if isSharpnessN3:
            return " SHARPNESS -3 "


    def GetCurrentContrastSetting(self):
        isCONTRASTP1 = self.InitalDevice.checkUIElementExist(" CONTRAST +1 ")
        isCONTRASTP2 = self.InitalDevice.checkUIElementExist(" CONTRAST +2 ")
        isCONTRASTP3 = self.InitalDevice.checkUIElementExist(" CONTRAST +3 ")
        isCONTRAST0 = self.InitalDevice.checkUIElementExist(" CONTRAST ±0 ")
        isCONTRASTN1 = self.InitalDevice.checkUIElementExist(" CONTRAST -1 ")
        isCONTRASTN2 = self.InitalDevice.checkUIElementExist(" CONTRAST -2 ")
        isCONTRASTN3 = self.InitalDevice.checkUIElementExist(" CONTRAST -3 ")
        if isCONTRASTP1:
            return " CONTRAST +1 "
        if isCONTRASTP2:
            return " CONTRAST +2 "
        if isCONTRASTP3:
            return " CONTRAST +3 "
        if isCONTRAST0:
            return " CONTRAST ±0 "
        if isCONTRASTN1:
            return " CONTRAST -1 "
        if isCONTRASTN2:
            return " CONTRAST -2 "
        if isCONTRASTN3:
            return " CONTRAST -3 "

    def GetCurrentSaturationSetting(self):
        isSATURATIONP1 = self.InitalDevice.checkUIElementExist(" SATURATION +1 ")
        isSATURATIONP2 = self.InitalDevice.checkUIElementExist(" SATURATION +2 ")
        isSATURATIONP3 = self.InitalDevice.checkUIElementExist(" SATURATION +3 ")
        isSATURATION0 = self.InitalDevice.checkUIElementExist(" SATURATION ±0 ")
        isSATURATIONN1 = self.InitalDevice.checkUIElementExist(" SATURATION -1 ")
        isSATURATIONN2 = self.InitalDevice.checkUIElementExist(" SATURATION -2 ")
        isSATURATIONN3 = self.InitalDevice.checkUIElementExist(" SATURATION -3 ")
        if isSATURATIONP1:
            return " SATURATION +1 "
        if isSATURATIONP2:
            return " SATURATION +2 "
        if isSATURATIONP3:
            return " SATURATION +3 "
        if isSATURATION0:
            return " SATURATION ±0 "
        if isSATURATIONN1:
            return " SATURATION -1 "
        if isSATURATIONN2:
            return " SATURATION -2 "
        if isSATURATIONN3:
            return " SATURATION -3 "

    def SetStyleInCaptureMode(self,Style="STD",Sharpness="±0",Contrast="±0",Saturation="±0"):
        self.SwitchtoCaptureMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'left', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            try:
                 SelectStyleSettingElement= self.InitalDevice.driver.find_element_by_accessibility_id("STYLE")  #1
            except:
                self.logger.logger.warn(
                    "Can not find the Style setting item, maybe it is not on the camera interface***")
            else:
                try:
                    SelectStyleSettingElement.click()  #2
                except:
                    self.logger.logger.warn(
                        "Select the Style setting item, maybe it is not on the camera interface***")
                else:
                    if Style == "STD" or Style == "LAND" or Style == "NEUT":
                        try:
                            StyleSwipeElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the style swipe bar, maybe it is not on the camera interface***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": StyleSwipeElement})
                            sleep(1.5)
                            try:
                                if Style == "STD":
                                    StyleItemElement = self.InitalDevice.driver.find_element_by_accessibility_id(" STD. ±0 ±0 ±0")
                                elif Style == "LAND":
                                    StyleItemElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        " LAND. +1 +1 ±0")
                                else:
                                    StyleItemElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        " NEUT. -1 ±0 ±0")
                            except:
                                self.logger.logger.warn(
                                    "Can not find the style item, maybe it is not on the camera interface***")
                            else:
                                try:
                                    StyleItemElement.click()
                                except:
                                    self.logger.logger.warn(
                                    "Set the %s style Error***"%Style)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                    else:
                        try:
                            StyleSwipeElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the style swipe bar, maybe it is not on the camera interface***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": StyleSwipeElement})
                            sleep(1.5)
                            try:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 304}) # go to custom style setting interface
                            except:
                                pass
                            else:
                                ##set Sharpness
                                #get current sharpness
                                CurrentSharpness = self.GetCurrentSharpnessSetting()
                                try:
                                    SharpnessSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(CurrentSharpness)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the sharpness setting control button***")
                                else:
                                    try:
                                        SharpnessSettingElement.click()
                                        if self.InitalDevice.checkUIElementExist(CurrentSharpness):
                                            SharpnessSettingElement.click()
                                            sleep(1.5)
                                        else:
                                            sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Go to  the sharpness setting interface error***")
                                    else:
                                        if Sharpness =="+1" or Sharpness =="+2" or Sharpness =="+3":
                                            try:
                                                SharpnessValueSwipBar= self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the sharpness value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": SharpnessValueSwipBar})
                                                sleep(1.5)
                                                tmpSharpness = " "+Sharpness
                                                try:
                                                    SharpnessValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(tmpSharpness)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the sharpness value item***")
                                                else:
                                                    try:
                                                        SharpnessValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the sharpness value Error***")
                                                    else:
                                                        #After set sharpness successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id("Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        elif Sharpness =="-1" or Sharpness =="-2" or Sharpness =="-3":
                                            try:
                                                SharpnessValueSwipBar= self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the sharpness value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SharpnessValueSwipBar})
                                                sleep(1.5)
                                                tmpSharpness = " "+Sharpness
                                                try:
                                                    SharpnessValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(tmpSharpness)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the sharpness value item***")
                                                else:
                                                    try:
                                                        SharpnessValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the sharpness value Error***")
                                                    else:
                                                        #After set sharpness successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id("Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        else:
                                            try:
                                                SharpnessValueSwipBar= self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the sharpness value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SharpnessValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SharpnessValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": SharpnessValueSwipBar})
                                                sleep(1.5)
                                                tmpSharpness = " "+Sharpness
                                                try:
                                                    SharpnessValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(tmpSharpness)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the sharpness value item***")
                                                else:
                                                    try:
                                                        SharpnessValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the sharpness value Error***")
                                                    else:
                                                        #After set sharpness successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id("Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                ##set Contrast
                                # get current Contrast
                                CurrentContrast = self.GetCurrentContrastSetting()
                                try:
                                    ContrastSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        CurrentContrast)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the Contrast setting control button***")
                                else:
                                    try:
                                        ContrastSettingElement.click()
                                        if  self.InitalDevice.checkUIElementExist(CurrentContrast):
                                            ContrastSettingElement.click()
                                            sleep(1.5)
                                        else:
                                            sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Go to  the Contrast setting interface error***")
                                    else:
                                        if Contrast == "+1" or Contrast == "+2" or Contrast == "+3":
                                            try:
                                                ContrastValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Contrast value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": ContrastValueSwipBar})
                                                sleep(1.5)
                                                tmpContrast = " " + Contrast
                                                try:
                                                    ContrastValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpContrast)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Contrast value item***")
                                                else:
                                                    try:
                                                        ContrastValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Contrast value Error***")
                                                    else:
                                                        # After set Contrast successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        elif Contrast == "-1" or Contrast == "-2" or Contrast == "-3":
                                            try:
                                                ContrastValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Contrast value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": ContrastValueSwipBar})
                                                sleep(1.5)
                                                tmpContrast = " " + Contrast
                                                try:
                                                    ContrastValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpContrast)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Contrast value item***")
                                                else:
                                                    try:
                                                        ContrastValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Contrast value Error***")
                                                    else:
                                                        # After set Contrast successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        else:
                                            try:
                                                ContrastValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Contrast value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": ContrastValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": ContrastValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": ContrastValueSwipBar})
                                                sleep(1.5)
                                                tmpContrast = " " + Contrast
                                                try:
                                                    ContrastValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpContrast)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Contrast value item***")
                                                else:
                                                    try:
                                                        ContrastValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Contrast value Error***")
                                                    else:
                                                        # After set Contrast successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                ##set Saturation
                                # get current Saturation
                                CurrentSaturation = self.GetCurrentSaturationSetting()
                                try:
                                    SaturationSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        CurrentSaturation)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the Saturation setting control button***")
                                else:
                                    try:
                                        SaturationSettingElement.click()
                                        if self.InitalDevice.checkUIElementExist(CurrentSaturation):
                                            SaturationSettingElement.click()
                                            sleep(1.5)
                                        else:
                                            sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Go to  the Saturation setting interface error***")
                                    else:
                                        if Saturation == "+1" or Saturation == "+2" or Saturation == "+3":
                                            try:
                                                SaturationValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Saturation value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": SaturationValueSwipBar})
                                                sleep(1.5)
                                                tmpSaturation = " " + Saturation
                                                try:
                                                    SaturationValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpSaturation)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Saturation value item***")
                                                else:
                                                    try:
                                                        SaturationValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Saturation value Error***")
                                                    else:
                                                        # After set Saturation successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        elif Saturation == "-1" or Saturation == "-2" or Saturation == "-3":
                                            try:
                                                SaturationValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Saturation value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SaturationValueSwipBar})
                                                sleep(1.5)
                                                tmpSaturation = " " + Saturation
                                                try:
                                                    SaturationValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpSaturation)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Saturation value item***")
                                                else:
                                                    try:
                                                        SaturationValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Saturation value Error***")
                                                    else:
                                                        # After set Saturation successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        else:
                                            try:
                                                SaturationValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Saturation value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SaturationValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SaturationValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": SaturationValueSwipBar})
                                                sleep(1.5)
                                                tmpSaturation = " " + Saturation
                                                try:
                                                    SaturationValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpSaturation)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Saturation value item***")
                                                else:
                                                    try:
                                                        SaturationValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Saturation value Error***")
                                                    else:
                                                        # After set Saturation successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
            #Exit style setting
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})
    def SetDigitalZoomInCaptureMode(self,DigitalZoom):
        self.SwitchtoCaptureMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'left', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            try:
                 SelectStyleSettingElement= self.InitalDevice.driver.find_element_by_accessibility_id("DIGITAL ZOOM")
            except:
                self.logger.logger.warn(
                    "Can not find the Digital Zoom setting item, maybe it is not on the camera interface***")
            else:
                try:
                    SelectStyleSettingElement.click()
                    sleep(1.5)
                except:
                    self.logger.logger.warn(
                        "Go to the Digital Zoom setting menu error***")
                else:
                    if DigitalZoom =="1.0×" or DigitalZoom =="2.0×" or DigitalZoom =="3.0×":
                        try:
                            DigitalZoomSwipe = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the Digital Zoom value swipe***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": DigitalZoomSwipe})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": DigitalZoomSwipe})
                            sleep(1.5)
                            try:
                                DigitalZoomElement = self.InitalDevice.driver.find_element_by_accessibility_id(DigitalZoom)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the Digital Zoom value item***")
                            else:
                                try:
                                    DigitalZoomElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the Digital Zoom %s value Error***"%DigitalZoom)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                    elif DigitalZoom =="6.0×" or DigitalZoom =="7.0×" or DigitalZoom =="8.0×":
                        try:
                            DigitalZoomSwipe = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the Digital Zoom value swipe***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": DigitalZoomSwipe})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": DigitalZoomSwipe})
                            sleep(1.5)
                            try:
                                DigitalZoomElement = self.InitalDevice.driver.find_element_by_accessibility_id(DigitalZoom)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the Digital Zoom value item***")
                            else:
                                try:
                                    DigitalZoomElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the Digital Zoom %s value Error***"%DigitalZoom)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                    else:
                        try:
                            DigitalZoomSwipe = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the Digital Zoom value swipe***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": DigitalZoomSwipe})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": DigitalZoomSwipe})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": DigitalZoomSwipe})
                            sleep(1.5)
                            try:
                                DigitalZoomElement = self.InitalDevice.driver.find_element_by_accessibility_id(DigitalZoom)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the Digital Zoom value item***")
                            else:
                                try:
                                    DigitalZoomElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the Digital Zoom %s value Error***"%DigitalZoom)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
    def GotoAlbumInCaptureMode(self):
        self.SwitchtoCaptureMode()
        sleep(1.5)
        try:
            AlbumEnterElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]")
        except:
            self.logger.logger.warn(
                "Can not find the album control button***")
        else:
            try:
                AlbumEnterElement.click()
            except:
                self.logger.logger.warn(
                    "Go to the album error***")
            else:
                pass
    def GotoMultiAlbumInCaptureMode(self):
        self.GotoAlbumInCaptureMode()
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            self.logger.logger.warn(
                "Can not find the muti-album control button,may be it is not in Album interface***")
        else:
            try:
                MultAblumEnterElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Go to the muti album error***")
            else:
                pass
    def SelectNLNCItem(self,N=1,M=1):#N 1-2,M 1-5
        self.GotoMultiAlbumInCaptureMode()
        X = int((2*M-1)*133/2)
        Y = int(60+(2*N-1)*132/2)
        try:
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": X,
                                                     "y": Y})
        except:
            self.logger.logger.warn("Select the %d line and %d colum error***"%(N,M))
        else:
            sleep(0.5)

############################Setting in record mode#################################
    def setManualExposureModeInRecordMode(self):
        self.SwitchtoRecordMode()
        sleep(0.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except Exception as e:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            pass
        try:
            el2 = self.InitalDevice.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"MANUAL\"])[2]")
        except:
            try:
                SelectExpModeElement = self.InitalDevice.driver.find_element_by_accessibility_id("AUTO")
            except:
                self.logger.logger.warn(
                    "Can not find the Exposure setting item***")
            else:
                SelectExpModeElement.click()
                sleep(1.5)
                try:
                    ManualExpModeElement= self.InitalDevice.driver.find_element_by_accessibility_id("MANUAL")
                except:
                    self.logger.logger.warn(
                        "Can not find the Manual Exposure value***")
                else:
                    try:
                        ManualExpModeElement.click()
                    except:
                        self.logger.logger.warn(
                            "Set Manual Exposure Mode In RecordMode Error***")
                    else:
                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                {"x": 333,
                                                                 "y": 187})
        else:
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})
    def setAutoExposureModeInRecordMode(self):
        self.SwitchtoRecordMode()
        sleep(0.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn(
                "Can not find the bottom setting bar item***")
        else:
            pass
        try:
            el2 = self.InitalDevice.driver.find_element_by_accessibility_id("AUTO")
        except:
            try:
                SelectExpModeElement = self.InitalDevice.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"MANUAL\"])[2]")
            except:
                pass
            else:
                SelectExpModeElement.click()
                sleep(0.5)
                try:
                    AutoExpModeElement= self.InitalDevice.driver.find_element_by_accessibility_id("AUTO")
                except:
                    self.logger.logger.warn(
                        "Set Auto Exposure Mode In RecordMode Error***")
                else:
                    AutoExpModeElement.click()
                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
        else:
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})

    def GetCurrentShutter(self):
        isShutter8000Exist = self.InitalDevice.checkUIElementExist("1/8000")
        isShutter6000Exist = self.InitalDevice.checkUIElementExist("1/6000")
        isShutter5000Exist = self.InitalDevice.checkUIElementExist("1/5000")
        isShutter4000Exist = self.InitalDevice.checkUIElementExist("1/4000")
        isShutter3200Exist = self.InitalDevice.checkUIElementExist("1/3200")
        isShutter2500Exist = self.InitalDevice.checkUIElementExist("1/2500")
        isShutter2000Exist = self.InitalDevice.checkUIElementExist("1/2000")
        isShutter1600Exist = self.InitalDevice.checkUIElementExist("1/1600")
        isShutter1250Exist = self.InitalDevice.checkUIElementExist("1/1250")
        isShutter1000Exist = self.InitalDevice.checkUIElementExist("1/1000")
        isShutter800Exist = self.InitalDevice.checkUIElementExist("1/800")
        isShutter640Exist = self.InitalDevice.checkUIElementExist("1/640")
        isShutter500Exist = self.InitalDevice.checkUIElementExist("1/500")
        isShutter400Exist = self.InitalDevice.checkUIElementExist("1/400")
        isShutter320Exist = self.InitalDevice.checkUIElementExist("1/320")
        isShutter240Exist = self.InitalDevice.checkUIElementExist("1/240")
        isShutter200Exist = self.InitalDevice.checkUIElementExist("1/200")
        isShutter160Exist = self.InitalDevice.checkUIElementExist("1/160")
        isShutter120Exist = self.InitalDevice.checkUIElementExist("1/120")
        isShutter100Exist = self.InitalDevice.checkUIElementExist("1/100")
        isShutter80Exist = self.InitalDevice.checkUIElementExist("1/80")
        isShutter60Exist = self.InitalDevice.checkUIElementExist("1/60")
        isShutter50Exist = self.InitalDevice.checkUIElementExist("1/50")
        isShutter40Exist = self.InitalDevice.checkUIElementExist("1/40")
        isShutter30Exist = self.InitalDevice.checkUIElementExist("1/30")
        isShutter25Exist = self.InitalDevice.checkUIElementExist("1/25")
        isShutter20Exist = self.InitalDevice.checkUIElementExist("1/20")
        isShutter15Exist = self.InitalDevice.checkUIElementExist("1/15")
        isShutter12p5Exist = self.InitalDevice.checkUIElementExist("1/12.5")
        isShutter10Exist = self.InitalDevice.checkUIElementExist("1/10")
        isShutter8Exist = self.InitalDevice.checkUIElementExist("1/8")
        isShutter6p25Exist = self.InitalDevice.checkUIElementExist("1/6.25")
        isShutter5Exist = self.InitalDevice.checkUIElementExist("1/5")
        isShutter4Exist = self.InitalDevice.checkUIElementExist("1/4")
        isShutter3Exist = self.InitalDevice.checkUIElementExist("1/3")
        isShutter2Exist = self.InitalDevice.checkUIElementExist("1/2")
        isShutter2p5Exist = self.InitalDevice.checkUIElementExist("1/2.5")
        isShutter1p67Exist = self.InitalDevice.checkUIElementExist("1/1.67")
        isShutter1p25Exist = self.InitalDevice.checkUIElementExist("1/1.25")
        isShutter1SExist = self.InitalDevice.checkUIElementExist("1.0\"")
        isShutter1p3SExist = self.InitalDevice.checkUIElementExist("1.3\"")
        isShutter1p6SExist = self.InitalDevice.checkUIElementExist("1.6\"")
        isShutter2SExist = self.InitalDevice.checkUIElementExist("2.0\"")
        isShutter2p5SExist = self.InitalDevice.checkUIElementExist("2.5\"")
        isShutter3SExist = self.InitalDevice.checkUIElementExist("3.0\"")
        isShutter3p2SExist = self.InitalDevice.checkUIElementExist("3.2\"")
        isShutter4SExist = self.InitalDevice.checkUIElementExist("4.0\"")
        isShutter5SExist = self.InitalDevice.checkUIElementExist("5.0\"")
        isShutter6SExist = self.InitalDevice.checkUIElementExist("6.0\"")
        isShutter8SExist = self.InitalDevice.checkUIElementExist("8.0\"")
        if isShutter8000Exist:
            return "1/8000"
        if isShutter6000Exist:
            return "1/6000"
        if isShutter5000Exist:
            return "1/5000"
        if isShutter4000Exist:
            return "1/4000"
        if isShutter3200Exist:
            return "1/3200"
        if isShutter2500Exist:
            return "1/2500"
        if isShutter2000Exist:
            return "1/2000"
        if isShutter1600Exist:
            return "1/1600"
        if isShutter1250Exist:
            return "1/1250"
        if isShutter1000Exist:
            return "1/1000"
        if isShutter800Exist:
            return "1/800"
        if isShutter640Exist:
            return "1/640"
        if isShutter500Exist:
            return "1/500"
        if isShutter400Exist:
            return "1/400"
        if isShutter320Exist:
            return "1/320"
        if isShutter240Exist:
            return "1/240"
        if isShutter200Exist:
            return "1/200"
        if isShutter160Exist:
            return "1/160"
        if isShutter120Exist:
            return "1/120"
        if isShutter100Exist:
            return "1/100"
        if isShutter80Exist:
            return "1/80"
        if isShutter60Exist:
            return "1/60"
        if isShutter50Exist:
            return "1/50"
        if isShutter40Exist:
            return "1/40"
        if isShutter30Exist:
            return "1/30"
        if isShutter25Exist:
            return "1/25"
        if isShutter20Exist:
            return "1/20"
        if isShutter15Exist:
            return "1/15"
        if isShutter12p5Exist:
            return "1/12.5"
        if isShutter10Exist:
            return "1/10"
        if isShutter8Exist:
            return "1/8"
        if isShutter6p25Exist:
            return "1/6.25"
        if isShutter5Exist:
            return "1/5"
        if isShutter4Exist:
            return "1/4"
        if isShutter3Exist:
            return "1/3"
        if isShutter2Exist:
            return "1/2"
        if isShutter2p5Exist:
            return "1/2.5"
        if isShutter1p67Exist:
            return "1/1.67"
        if isShutter1p25Exist:
            return "1/1.25"
        if isShutter1SExist:
            return "1\""
        if isShutter1p3SExist:
            return "1.3\""
        if isShutter1p6SExist:
            return "1.6\""
        if isShutter2SExist:
            return "2\""
        if isShutter2p5SExist:
            return "2.5\""
        if isShutter3SExist:
            return "3\""
        if isShutter3p2SExist:
            return "3.2\""
        if isShutter4SExist:
            return "4\""
        if isShutter5SExist:
            return "5\""
        if isShutter6SExist:
            return "6\""
        if isShutter8SExist:
            return "8\""

    def setShutterInRecordMode(self,shutter):
        ##select shutter setting
        self.SwitchtoRecordMode()
        sleep(0.5)
        self.setManualExposureModeInRecordMode()
        sleep(0.5)
        try:
            BottomSettingBarElement = self.InitalDevice.driver.find_element_by_accessibility_id("Img_console_bottom_bar_bg")
        except:
            self.logger.logger.warn(
                "Can not find the bottom setting bar item***")
        else:
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'left', "element": BottomSettingBarElement})
            sleep(1.5)
        CurrentShutter = self.GetCurrentShutter()
        try:
           shutterSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("SHUTTER")
        except Exception as e:
            pass
        else:
            shutterSettingElement.click()
            sleep(1.5)
        try:
            if shutter.find("/") != -1:
                ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter)
                if not ShutterElement.is_displayed():
                    raise AttributeError
            else:
                ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter+"\"")
                if not ShutterElement.is_displayed():
                    raise AttributeError
        except:
            if shutter.__contains__("/"):
                shutterlist = shutter.split("/")
                shutterValue = float(shutterlist[0])/float(shutterlist[1])
            else:
                shutterValue = float(shutter.replace("\"", ""))
            if CurrentShutter !=None:
                if CurrentShutter.__contains__("/"):
                    CurrentShutterlist = CurrentShutter.split("/")
                    currentShutterValue = float(CurrentShutterlist[0]) / float(CurrentShutterlist[1])
                else:
                    currentShutterValue = float(CurrentShutter.replace("\"", ""))
                if shutterValue == currentShutterValue:
                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                    return
                elif shutterValue > currentShutterValue:
                    swiptimes = 0
                    while True:
                        try:
                            shuttersliderElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": shuttersliderElement})
                            sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Can not find shutter slider Element***")
                        else:
                            try:
                                if shutter.find("/"):
                                    ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter)
                                    if not ShutterElement.is_displayed():
                                        raise AttributeError
                                else:
                                    ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        shutter + "\"")
                                    if not ShutterElement.is_displayed():
                                        raise AttributeError
                            except:
                                swiptimes = swiptimes + 1
                                if swiptimes > 15:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                                    self.logger.logger.warn(
                                        "Set shutter to %s fail***" % shutter)
                                    break
                                pass
                            else:
                                ShutterElement.click()
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                break
                else:
                    swiptimes = 0
                    while True:
                        try:
                            shuttersliderElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": shuttersliderElement})
                            sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Can not find shutter slider Element***")
                        else:
                            try:
                                if shutter.find("/"):
                                    ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(shutter)
                                    if not ShutterElement.is_displayed():
                                        raise AttributeError
                                else:
                                    ShutterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        shutter + "\"")
                                    if not ShutterElement.is_displayed():
                                        raise AttributeError
                            except:
                                swiptimes = swiptimes + 1
                                if swiptimes > 15:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                                    self.logger.logger.warn(
                                        "Set shutter to %s in record mode error***" % shutter)
                                    break
                            else:
                                ShutterElement.click()
                                # exit setting interface
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                break
            else:
                self.logger.logger.warn(
                    "Can not get current shutter***")
                # exit setting interface
                self.InitalDevice.driver.execute_script("mobile: tap",
                                                        {"x": 333,
                                                         "y": 187})

        else:
            try:
                ShutterElement.click()
            except:
                self.logger.logger.warn(
                    "Set shutter to %s in record mode error***" % shutter)
            else:
                self.InitalDevice.driver.execute_script("mobile: tap",
                                                        {"x": 333,
                                                         "y": 187})

    def GetCurrentISOSetting(self):
        iSISO100Exist = self.InitalDevice.checkUIElementExist("100")
        iSISO200Exist = self.InitalDevice.checkUIElementExist("200")
        iSISO400Exist = self.InitalDevice.checkUIElementExist("400")
        iSISO800Exist = self.InitalDevice.checkUIElementExist("800")
        iSISO1600Exist = self.InitalDevice.checkUIElementExist("1600")
        iSISO3200Exist = self.InitalDevice.checkUIElementExist("3200")
        if iSISO100Exist:
            return "100"
        if iSISO200Exist:
            return "200"
        if iSISO400Exist:
            return "400"
        if iSISO800Exist:
            return "800"
        if iSISO1600Exist:
            return "1600"
        if iSISO3200Exist:
            return "3200"


    def setISOInRecordMode(self,ISO):
        ##select shutter setting
        self.SwitchtoRecordMode()
        sleep(1.5)
        self.setManualExposureModeInRecordMode()
        sleep(1.5)
        try:
            ExposureSettingElement = self.InitalDevice.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"MANUAL\"])[2]")
            ResolutionSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("RESOLUTION")
        except:
            self.logger.logger.warn(
                "Can not find the bottom setting bar item***")
        else:
            #long press the position of ExposureSettingElement move to the position of ResolutionSettingElement
            try:
                TouchAction(self.InitalDevice.driver).long_press(ExposureSettingElement).move_to(ResolutionSettingElement).release().perform()
            except Exception as e:
                self.logger.logger.warn(e)
            else:
                sleep(1.5)
        CurrentISO = self.GetCurrentISOSetting()
        if CurrentISO !=None:
            CurrentISOValue = int(CurrentISO)
            ISOValue = int(ISO)
            try:
                ISOSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("ISO")
            except Exception as e:
                self.logger.logger.warn(
                    "Can not find ISO setting item in record mode***")
            else:
                ISOSettingElement.click()
                sleep(1.5)
            if ISOValue > CurrentISOValue:
                try:
                    shuttersliderElement = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                except:
                    self.logger.logger.warn(
                        "Can not find ISO value swip bar in record mode***")
                else:
                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                            {'direction': 'left', "element": shuttersliderElement})
                    sleep(1.5)
                    try:
                        ISOElement = self.InitalDevice.driver.find_element_by_accessibility_id(ISO)
                    except:
                        self.logger.logger.warn(
                            "Can not find ISO value setting item in record mode***")
                    else:
                        try:
                            ISOElement.click()
                        except:
                            self.logger.logger.warn(
                                "Set ISO to %s in record mode error***" % ISO)
                        else:
                            # exit setting interface
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
            elif ISOValue < CurrentISOValue:
                try:
                    shuttersliderElement = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                except:
                    self.logger.logger.warn(
                        "Can not find ISO value swip bar in record mode***")
                else:
                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                            {'direction': 'right', "element": shuttersliderElement})
                    sleep(1.5)
                    try:
                        ISOElement = self.InitalDevice.driver.find_element_by_accessibility_id(ISO)
                    except:
                        self.logger.logger.warn(
                            "Can not find ISO setting value item in record mode***")
                    else:
                        try:
                            ISOElement.click()
                        except:
                            self.logger.logger.warn(
                                "Set ISO to %s in record mode error***" % ISO)
                        else:
                            # exit setting interface
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
            else:
                # exit setting interface
                self.InitalDevice.driver.execute_script("mobile: tap",
                                                        {"x": 333,
                                                         "y": 187})
        else:
            self.logger.logger.warn(
                "Can not get current ISO  in record mode***")
            # exit setting interface
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})


    def SetEVInRecordMode(self,EV):
        self.SwitchtoRecordMode()
        sleep(1.5)
        self.setAutoExposureModeInRecordMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'left', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn(
                "Can not find Bottom Set Bar Element in capture mode***")
        else:
            pass
        try:
            EVElement = self.InitalDevice.driver.find_element_by_accessibility_id("EV")
        except Exception as e:
            self.logger.logger.warn(
                "Can not find EV set item in capture mode***")
        else:
            CurrentEV = self.GetCurrentEV()
            try:
                EVElement.click()
                sleep(1.5)
            except:
                self.logger.logger.warn(
                    "Go to the EV setting  interface in capture mode error***")
            else:
                try:
                    EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(EV)
                    EVSetValueElementLocation = EVSetValueElement.location
                    if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                        self.logger.logger.warn(
                            "Element is not visiable***")
                        raise AttributeError
                except:
                    try:
                        EVSelectBarElement = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                    except:
                        self.logger.logger.warn(
                            "Can not find EV select bar in capture mode***")
                    else:
                        if CurrentEV !=None:
                            if CurrentEV == "± 0":
                                CurrentEVValue = 0
                            else:
                                CurrentEVValue = float(CurrentEV)
                            if EV == "± 0":
                                EVValue = 0
                            else:
                                EVValue = float(EV)
                            if EVValue < CurrentEVValue:
                                swiptimes = 0
                                while True:
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'right', "element": EVSelectBarElement})
                                    sleep(1.5)
                                    try:
                                        EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(EV)
                                        EVSetValueElementLocation = EVSetValueElement.location
                                        if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                                            self.logger.logger.warn(
                                                "Element is not visiable***")
                                            raise AttributeError
                                    except:
                                        swiptimes = swiptimes + 1
                                        if swiptimes > 4:
                                            break
                                    else:
                                        try:
                                            EVSetValueElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Set %s EV in capture mode error***"%EV)
                                        else:
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                        break
                            elif EVValue > CurrentEVValue:
                                swiptimes = 0
                                while True:
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'left',
                                                                             "element": EVSelectBarElement})
                                    sleep(1.5)
                                    try:
                                        EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(EV)
                                        EVSetValueElementLocation = EVSetValueElement.location
                                        if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                                            self.logger.logger.warn(
                                                "Element is not visiable***")
                                            raise AttributeError
                                    except:
                                        swiptimes = swiptimes + 1
                                        if swiptimes > 4:
                                            break
                                    else:
                                        try:
                                            EVSetValueElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Set %s EV in capture mode error***"%EV)
                                        else:
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                        break
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                        else:
                            self.logger.logger.warn(
                                "Can not get current EV in capture mode***")
                else:
                    try:
                        EVSetValueElement.click()
                    except:
                        try:
                            EVSelectBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find EV select bar in capture mode***")
                        else:
                            if CurrentEV !=None:
                                if CurrentEV == "± 0":
                                    CurrentEVValue = 0
                                else:
                                    CurrentEVValue = float(CurrentEV)
                                if EV == "± 0":
                                    EVValue = 0
                                else:
                                    EVValue = float(EV)
                                if EVValue < CurrentEVValue:
                                    swiptimes = 0
                                    while True:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'right',
                                                                                 "element": EVSelectBarElement})
                                        sleep(1.5)
                                        try:
                                            EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                EV)
                                            EVSetValueElementLocation = EVSetValueElement.location
                                            if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                                                self.logger.logger.warn(
                                                    "Element is not visiable***")
                                                raise AttributeError
                                        except:
                                            swiptimes = swiptimes + 1
                                            if swiptimes > 4:
                                                break
                                        else:
                                            try:
                                                EVSetValueElement.click()
                                            except:
                                                self.logger.logger.warn(
                                                    "Set %s EV in capture mode error***" % EV)
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                        {"x": 333,
                                                                                         "y": 187})
                                            break
                                elif EVValue > CurrentEVValue:
                                    swiptimes = 0
                                    while True:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": EVSelectBarElement})
                                        sleep(1.5)
                                        try:
                                            EVSetValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                EV)
                                            EVSetValueElementLocation = EVSetValueElement.location
                                            if EVSetValueElementLocation["x"] > 667 or EVSetValueElementLocation["x"] < 0:
                                                self.logger.logger.warn(
                                                    "Element is not visiable***")
                                                raise AttributeError
                                        except:
                                            swiptimes = swiptimes + 1
                                            if swiptimes > 4:
                                                break
                                        else:
                                            try:
                                                EVSetValueElement.click()
                                            except:
                                                self.logger.logger.warn(
                                                    "Set %s EV in capture mode error***" % EV)
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                        {"x": 333,
                                                                                         "y": 187})
                                            break
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                            else:
                                self.logger.logger.warn(
                                    "Can not get current EV in capture mode***")
                    else:
                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                {"x": 333,
                                                                 "y": 187})
    def SetWhiteBalanceInRecordMode(self,WB=None,ColorTempeture=None): #WB = 'Custom' or 'custom'
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            WBElement = self.InitalDevice.driver.find_element_by_accessibility_id("WB")
            if not WBElement.is_displayed():
                raise AttributeError
        except:
            try:
                BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                        {'direction': 'left', "element": BottomSetBarElement})
                sleep(1.5)
            except:
                self.logger.logger.warn(
                    "Can not find Bottom Set Bar Element in capture mode***")
            else:
                try:
                    WBElement = self.InitalDevice.driver.find_element_by_accessibility_id("WB")
                    if not WBElement.is_displayed():
                        raise AttributeError
                except:
                    self.logger.logger.warn(
                        "Can not find WB setting item in capture mode***")
                else:
                    try:
                        WBElement.click()
                        sleep(1.5)
                    except:
                        self.logger.logger.warn(
                            "Go to the WB setting interface in capture mode error***")
                    else:
                        if WB == 'Custom' or WB == 'custom':
                            try:
                                WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": WBItemBarElement})
                                sleep(1.5)

                            except:
                                self.logger.logger.warn(
                                    "Can not find WB select swipe bar in capture mode***")
                            else:
                                CustomCurrentSet = self.GetCustomWBCurrentSetting()
                                try:
                                    CustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        CustomCurrentSet)
                                except Exception as e:
                                    self.logger.logger.warn(
                                        "Can not find %s WB setting value in capture mode***" % CustomCurrentSet)
                                else:
                                    try:
                                        CustomWBElement.click()
                                        sleep(1)
                                        try:
                                            CustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                CustomCurrentSet)
                                        except:
                                            pass
                                        else:
                                            CustomWBElement.click()
                                            sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Go to the custom WB setting interface in capture mode error***")
                                    else:
                                        try:
                                            SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                ColorTempeture)
                                        except:
                                            if CustomCurrentSet != None:
                                                CustomCurrentSetValue = int(
                                                    CustomCurrentSet.replace("K", "").replace(" ", ""))
                                                ColorTempetureValue = int(ColorTempeture.replace("K", "").replace(" ", ""))
                                                try:
                                                    CWBSelectBar = self.InitalDevice.driver.find_element_by_xpath(
                                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]"
                                                        "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                                        "/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]"
                                                        "/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find custom WB select swipe bar in capture mode***")
                                                else:
                                                    if ColorTempetureValue < CustomCurrentSetValue:
                                                        swiptimes = 0
                                                        while True:
                                                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                                    {
                                                                                                        'direction': 'right',
                                                                                                        "element": CWBSelectBar})
                                                            sleep(1.5)
                                                            try:
                                                                SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                    ColorTempeture)
                                                            except:
                                                                swiptimes = swiptimes + 1
                                                                if swiptimes > 16:
                                                                    break
                                                            else:
                                                                try:
                                                                    SetCustomWBElement.click()
                                                                except Exception as e:
                                                                    self.logger.logger.warn(
                                                                        "Can not find the WB setting item***")
                                                                else:
                                                                    try:
                                                                        backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                            "Back")
                                                                    except Exception as e:
                                                                        self.logger.logger.warn(
                                                                            "Can not find the back control button***")
                                                                    else:
                                                                        backElement.click()
                                                                    self.InitalDevice.driver.execute_script(
                                                                        "mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                                                    break
                                                    elif ColorTempetureValue > CustomCurrentSetValue:
                                                        swiptimes = 0
                                                        while True:
                                                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                                    {
                                                                                                        'direction': 'left',
                                                                                                        "element": CWBSelectBar})
                                                            sleep(1.5)
                                                            try:
                                                                SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                    ColorTempeture)
                                                            except:
                                                                swiptimes = swiptimes + 1
                                                                if swiptimes > 16:
                                                                    break
                                                            else:
                                                                try:
                                                                    SetCustomWBElement.click()
                                                                except Exception as e:
                                                                    self.logger.logger.warn(
                                                                        "Can not find the WB setting item***")
                                                                else:
                                                                    try:
                                                                        backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                            "Back")
                                                                    except Exception as e:
                                                                        self.logger.logger.warn(
                                                                            "Can not find the back control button***")
                                                                    else:
                                                                        backElement.click()
                                                                    self.InitalDevice.driver.execute_script(
                                                                        "mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                                                    break
                                                    else:
                                                        self.InitalDevice.driver.execute_script(
                                                            "mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                                            else:
                                                self.logger.logger.warn(
                                                    "Can not get custom WB***")

                                        else:
                                            try:
                                                SetCustomWBElement.click()
                                            except:
                                                if CustomCurrentSet !=None:
                                                    CustomCurrentSetValue = int(
                                                        CustomCurrentSet.replace("K", "").replace(" ", ""))
                                                    ColorTempetureValue = int(
                                                        ColorTempeture.replace("K", "").replace(" ", ""))
                                                    try:
                                                        CWBSelectBar = self.InitalDevice.driver.find_element_by_xpath(
                                                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]"
                                                            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                                            "/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]"
                                                            "/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Can not find custom WB select swipe bar in capture mode***")
                                                    else:
                                                        if ColorTempetureValue < CustomCurrentSetValue:
                                                            swiptimes = 0
                                                            while True:
                                                                self.InitalDevice.driver.execute_script(
                                                                    "mobile: swipe",
                                                                    {
                                                                        'direction': 'right',
                                                                        "element": CWBSelectBar})
                                                                sleep(1.5)
                                                                try:
                                                                    SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                        ColorTempeture)
                                                                except:
                                                                    swiptimes = swiptimes + 1
                                                                    if swiptimes > 16:
                                                                        break
                                                                else:
                                                                    try:
                                                                        SetCustomWBElement.click()
                                                                    except Exception as e:
                                                                        self.logger.logger.warn(
                                                                            "Can not find the WB setting item***")
                                                                    else:
                                                                        try:
                                                                            backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                                "Back")
                                                                        except Exception as e:
                                                                            self.logger.logger.warn(
                                                                                "Can not find the back control button***")
                                                                        else:
                                                                            try:
                                                                                backElement.click()
                                                                            except:
                                                                                self.logger.logger.warn(
                                                                                    "Click the back control error***")
                                                                            else:
                                                                                self.InitalDevice.driver.execute_script(
                                                                                    "mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                                                        break
                                                        elif ColorTempetureValue > CustomCurrentSetValue:
                                                            swiptimes = 0
                                                            while True:
                                                                self.InitalDevice.driver.execute_script(
                                                                    "mobile: swipe",
                                                                    {
                                                                        'direction': 'left',
                                                                        "element": CWBSelectBar})
                                                                sleep(1.5)
                                                                try:
                                                                    SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                        ColorTempeture)
                                                                except:
                                                                    swiptimes = swiptimes + 1
                                                                    if swiptimes > 16:
                                                                        break
                                                                else:
                                                                    try:
                                                                        SetCustomWBElement.click()
                                                                    except Exception as e:
                                                                        self.logger.logger.warn(
                                                                            "Can not find the WB setting item***")
                                                                    else:
                                                                        try:
                                                                            backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                                "Back")
                                                                        except Exception as e:
                                                                            self.logger.logger.warn(
                                                                                "Can not find the back control button***")
                                                                        else:
                                                                            try:
                                                                                backElement.click()
                                                                            except:
                                                                                self.logger.logger.warn(
                                                                                    "Click the back control error***")
                                                                            else:
                                                                                self.InitalDevice.driver.execute_script(
                                                                                    "mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                                                                        break
                                                        else:
                                                            self.InitalDevice.driver.execute_script(
                                                                "mobile: tap",
                                                                {"x": 333,
                                                                 "y": 187})
                                                else:
                                                    self.logger.logger.warn(
                                                        "Can not get custom WB***")
                                            else:
                                                try:
                                                    backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        "Back")
                                                except Exception as e:
                                                    self.logger.logger.warn("Can not find the back control button***")
                                                else:
                                                    try:
                                                        backElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Click the back control error***")
                                                    else:
                                                        self.InitalDevice.driver.execute_script(
                                                            "mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                        else:
                            try:
                                SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(WB)
                            except:
                                try:
                                    WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                            {'direction': 'right',
                                                                             "element": WBItemBarElement})
                                    sleep(1.5)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find WB select swipe bar in capture mode***")
                                else:
                                    try:
                                        SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(WB)
                                    except:
                                        try:
                                            WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                    {'direction': 'left',
                                                                                     "element": WBItemBarElement})
                                            sleep(1.5)
                                        except:
                                            self.logger.logger.warn(
                                                "Can not find WB select swipe bar in capture mode***")
                                        else:
                                            try:
                                                SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                    WB)
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the %s WB item in capture mode***" % WB)
                                            else:
                                                try:
                                                    SetWBItem.click()
                                                except:
                                                    self.logger.logger.warn(
                                                        "Set the %s WB in capture mode error***" % WB)
                                                else:
                                                    self.InitalDevice.driver.execute_script(
                                                        "mobile: tap",
                                                        {"x": 333,
                                                         "y": 187})

                                    else:
                                        try:
                                            SetWBItem.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Set the %s WB in capture mode error***" % WB)
                                        else:
                                            self.InitalDevice.driver.execute_script(
                                                "mobile: tap",
                                                {"x": 333,
                                                 "y": 187})
                            else:
                                try:
                                    SetWBItem.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the %s WB in capture mode error***" % WB)
                                else:
                                    self.InitalDevice.driver.execute_script(
                                        "mobile: tap",
                                        {"x": 333,
                                         "y": 187})
        else:
            WBElement.click()
            sleep(1.5)
            if WB == 'Custom' or WB == 'custom':
                try:
                    WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                            {'direction': 'left',
                                                             "element": WBItemBarElement})
                    sleep(1.5)

                except:
                    self.logger.logger.warn(
                        "Can not find WB select swipe bar in capture mode***")
                else:
                    CustomCurrentSet = self.GetCustomWBCurrentSetting()
                    try:
                        CustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            CustomCurrentSet)
                    except Exception as e:
                        self.logger.logger.warn(
                            "Can not find %s WB setting value in capture mode***" % CustomCurrentSet)
                    else:
                        try:
                            CustomWBElement.click()
                            sleep(1)
                            try:
                                CustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    CustomCurrentSet)
                            except:
                                pass
                            else:
                                CustomWBElement.click()
                                sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Go to the custom WB setting interface in capture mode error***")
                        else:
                            try:
                                SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    ColorTempeture)
                            except:
                                if CustomCurrentSet != None:
                                    CustomCurrentSetValue = int(CustomCurrentSet.replace("K", "").replace(" ", ""))
                                    ColorTempetureValue = int(ColorTempeture.replace("K", "").replace(" ", ""))
                                    try:
                                        CWBSelectBar = self.InitalDevice.driver.find_element_by_xpath(
                                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]"
                                            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                            "/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]"
                                            "/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    except:
                                        self.logger.logger.warn(
                                            "Can not find custom WB select swipe bar in capture mode***")
                                    else:
                                        if ColorTempetureValue < CustomCurrentSetValue:
                                            swiptimes = 0
                                            while True:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {
                                                                                            'direction': 'right',
                                                                                            "element": CWBSelectBar})
                                                sleep(1.5)
                                                try:
                                                    SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        ColorTempeture)
                                                except:
                                                    swiptimes = swiptimes + 1
                                                    if swiptimes > 16:
                                                        break
                                                else:
                                                    try:
                                                        SetCustomWBElement.click()
                                                    except Exception as e:
                                                        self.logger.logger.warn(
                                                            "Can not find the WB setting item***")
                                                    else:
                                                        try:
                                                            backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except Exception as e:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            backElement.click()
                                                        self.InitalDevice.driver.execute_script(
                                                            "mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                                                        break
                                        elif ColorTempetureValue > CustomCurrentSetValue:
                                            swiptimes = 0
                                            while True:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {
                                                                                            'direction': 'left',
                                                                                            "element": CWBSelectBar})
                                                sleep(1.5)
                                                try:
                                                    SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        ColorTempeture)
                                                except:
                                                    swiptimes = swiptimes + 1
                                                    if swiptimes > 16:
                                                        break
                                                else:
                                                    try:
                                                        SetCustomWBElement.click()
                                                    except Exception as e:
                                                        self.logger.logger.warn(
                                                            "Can not find the WB setting item***")
                                                    else:
                                                        try:
                                                            backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except Exception as e:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            backElement.click()
                                                        self.InitalDevice.driver.execute_script(
                                                            "mobile: tap",
                                                            {"x": 333,
                                                             "y": 187})
                                                        break
                                        else:
                                            self.InitalDevice.driver.execute_script(
                                                "mobile: tap",
                                                {"x": 333,
                                                 "y": 187})
                                else:
                                    self.logger.logger.warn(
                                        "Can not get custom WB***")

                            else:
                                try:
                                    SetCustomWBElement.click()
                                except:
                                    if CustomCurrentSet != None:
                                        CustomCurrentSetValue = int(
                                            CustomCurrentSet.replace("K", "").replace(" ", ""))
                                        ColorTempetureValue = int(
                                            ColorTempeture.replace("K", "").replace(" ", ""))
                                        try:
                                            CWBSelectBar = self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]"
                                                "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                                "/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]"
                                                "/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                        except:
                                            self.logger.logger.warn(
                                                "Can not find custom WB select swipe bar in capture mode***")
                                        else:
                                            if ColorTempetureValue < CustomCurrentSetValue:
                                                swiptimes = 0
                                                while True:
                                                    self.InitalDevice.driver.execute_script(
                                                        "mobile: swipe",
                                                        {
                                                            'direction': 'right',
                                                            "element": CWBSelectBar})
                                                    sleep(1.5)
                                                    try:
                                                        SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                            ColorTempeture)
                                                    except:
                                                        swiptimes = swiptimes + 1
                                                        if swiptimes > 16:
                                                            break
                                                    else:
                                                        try:
                                                            SetCustomWBElement.click()
                                                        except Exception as e:
                                                            self.logger.logger.warn(
                                                                "Can not find the WB setting item***")
                                                        else:
                                                            try:
                                                                backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                    "Back")
                                                            except Exception as e:
                                                                self.logger.logger.warn(
                                                                    "Can not find the back control button***")
                                                            else:
                                                                try:
                                                                    backElement.click()
                                                                except:
                                                                    self.logger.logger.warn(
                                                                        "Click the back control error***")
                                                                else:
                                                                    self.InitalDevice.driver.execute_script(
                                                                        "mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                                            break
                                            elif ColorTempetureValue > CustomCurrentSetValue:
                                                swiptimes = 0
                                                while True:
                                                    self.InitalDevice.driver.execute_script(
                                                        "mobile: swipe",
                                                        {
                                                            'direction': 'left',
                                                            "element": CWBSelectBar})
                                                    sleep(1.5)
                                                    try:
                                                        SetCustomWBElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                            ColorTempeture)
                                                    except:
                                                        swiptimes = swiptimes + 1
                                                        if swiptimes > 16:
                                                            break
                                                    else:
                                                        try:
                                                            SetCustomWBElement.click()
                                                        except Exception as e:
                                                            self.logger.logger.warn(
                                                                "Can not find the WB setting item***")
                                                        else:
                                                            try:
                                                                backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                    "Back")
                                                            except Exception as e:
                                                                self.logger.logger.warn(
                                                                    "Can not find the back control button***")
                                                            else:
                                                                try:
                                                                    backElement.click()
                                                                except:
                                                                    self.logger.logger.warn(
                                                                        "Click the back control error***")
                                                                else:
                                                                    self.InitalDevice.driver.execute_script(
                                                                        "mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                                                            break
                                            else:
                                                self.InitalDevice.driver.execute_script(
                                                    "mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})
                                    else:
                                        self.logger.logger.warn(
                                            "Can not get custom WB***")
                                else:
                                    try:
                                        backElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                            "Back")
                                    except Exception as e:
                                        self.logger.logger.warn("Can not find the back control button***")
                                    else:
                                        try:
                                            backElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Click the back control error***")
                                        else:
                                            self.InitalDevice.driver.execute_script(
                                                "mobile: tap",
                                                {"x": 333,
                                                 "y": 187})
            else:
                try:
                    SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(WB)
                except:
                    try:
                        WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                {'direction': 'right',
                                                                 "element": WBItemBarElement})
                        sleep(1.5)
                    except:
                        self.logger.logger.warn(
                            "Can not find WB select swipe bar in capture mode***")
                    else:
                        try:
                            SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(WB)
                        except:
                            try:
                                WBItemBarElement = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": WBItemBarElement})
                                sleep(1.5)
                            except:
                                self.logger.logger.warn(
                                    "Can not find WB select swipe bar in capture mode***")
                            else:
                                try:
                                    SetWBItem = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        WB)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the %s WB item in capture mode***" % WB)
                                else:
                                    try:
                                        SetWBItem.click()
                                    except:
                                        self.logger.logger.warn(
                                            "Set the %s WB in capture mode error***" % WB)
                                    else:
                                        self.InitalDevice.driver.execute_script(
                                            "mobile: tap",
                                            {"x": 333,
                                             "y": 187})

                        else:
                            try:
                                SetWBItem.click()
                            except:
                                self.logger.logger.warn(
                                    "Set the %s WB in capture mode error***" % WB)
                            else:
                                self.InitalDevice.driver.execute_script(
                                    "mobile: tap",
                                    {"x": 333,
                                     "y": 187})
                else:
                    try:
                        SetWBItem.click()
                    except:
                        self.logger.logger.warn(
                            "Set the %s WB in capture mode error***" % WB)
                    else:
                        self.InitalDevice.driver.execute_script(
                            "mobile: tap",
                            {"x": 333,
                             "y": 187})

    def SetColorInRecordMode(self,Color):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            ColorSelectElement = self.InitalDevice.driver.find_element_by_accessibility_id("COLOR")
        except:
            try:
                BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                        {'direction': 'left', "element": BottomSetBarElement})
                sleep(1.5)
            except:
                self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
            else:
                try:
                    ColorSelectElement = self.InitalDevice.driver.find_element_by_accessibility_id("COLOR")
                except:
                    self.logger.logger.warn(
                        "Can not find the Color setting item, maybe it is not on the camera interface***")
                else:
                    if not self.InitalDevice.checkUIElementExist("Btn console help normal"):
                        try:
                            ColorSelectElement.click()
                            sleep(1.5)
                        except:
                            self.logger.logger.warn("Select the Color Error***")
                        else:
                            if Color == "DREAM" or Color == "CLASSIC" or Color == "NOSTALGIC":
                                try:
                                    ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                                except:
                                    self.logger.logger.warn("Can not find Color swipe bar***")
                                else:
                                    try:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                    except:
                                        self.logger.logger.warn("Swipe color  bar Error***")
                                    else:
                                        sleep(1.5)
                                try:
                                    ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                                except:
                                    self.logger.logger.warn("Find the %s setting item error***" % Color)
                                else:
                                    try:
                                        ColorSetElement.click()
                                    except:
                                        self.logger.logger.warn("Set %s setting error***" % Color)
                                    else:
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            elif Color == "NONE" or Color == "LOG" or Color == "VIVID":
                                try:
                                    ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                                except:
                                    self.logger.logger.warn("Can not find Color swipe bar***")
                                else:
                                    try:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'right',
                                                                                 "element": ColorSwipeBar})
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'right',
                                                                                 "element": ColorSwipeBar})
                                    except:
                                        self.logger.logger.warn("Swipe color  bar Error***")
                                    else:
                                        sleep(1.5)
                                try:
                                    ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                                except:
                                    self.logger.logger.warn("Find the %s setting item error***" % Color)
                                else:
                                    try:
                                        ColorSetElement.click()
                                    except:
                                        self.logger.logger.warn("Set %s setting error***" % Color)
                                    else:
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                            else:
                                try:
                                    ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                                except:
                                    self.logger.logger.warn("Can not find Color swipe bar***")
                                else:
                                    try:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'right',
                                                                                 "element": ColorSwipeBar})
                                    except:
                                        self.logger.logger.warn("Swipe color  bar Error***")
                                    else:
                                        sleep(1.5)
                                try:
                                    ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                                except:
                                    self.logger.logger.warn("Find the %s setting item error***" % Color)
                                else:
                                    try:
                                        ColorSetElement.click()
                                    except:
                                        self.logger.logger.warn("Set %s setting error***" % Color)
                                    else:
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 333,
                                                                                 "y": 187})
                    else:
                        try:
                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                        except:
                            try:
                                ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                            except:
                                self.logger.logger.warn("Can not find Color swipe bar***")
                            else:
                                swiptimes = 0
                                while True:
                                    try:
                                        self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                {'direction': 'left',
                                                                                 "element": ColorSwipeBar})
                                        sleep(1.5)
                                    except:
                                        pass
                                    else:
                                        try:
                                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                Color)
                                        except:
                                            swiptimes = swiptimes + 1
                                            if swiptimes > 3:
                                                break
                                        else:
                                            try:
                                                ColorSetElement.click()
                                            except:
                                                self.logger.logger.warn("Set the Color %s Error***" % Color)
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                        {"x": 333,
                                                                                         "y": 187})
                                                break
                                if swiptimes > 3:
                                    Otherswiptimes = 0
                                    while True:
                                        try:
                                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                    {'direction': 'right',
                                                                                     "element": ColorSwipeBar})
                                            sleep(1.5)
                                        except:
                                            pass
                                        else:
                                            try:
                                                ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                    Color)
                                            except:
                                                Otherswiptimes = Otherswiptimes + 1
                                                if Otherswiptimes > 3:
                                                    break
                                            else:
                                                try:
                                                    ColorSetElement.click()
                                                except:
                                                    self.logger.logger.warn("Set the Color %s Error***" % Color)
                                                else:
                                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                            {"x": 333,
                                                                                             "y": 187})
                                                    break

                        else:
                            try:
                                ColorSetElement.click()
                            except:
                                self.logger.logger.warn("Set the Color %s Error***" % Color)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
        else:
            if not self.InitalDevice.checkUIElementExist(
                    "Btn console help normal"):  # if color select interface exists,do not click the Color Select Item bar
                try:
                    ColorSelectElement.click()
                    sleep(1.5)
                except:
                    self.logger.logger.warn("Select the Color Error***")
                else:
                    if Color == "DREAM" or Color == "CLASSIC" or Color == "NOSTALGIC":
                        try:
                            ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                        except:
                            self.logger.logger.warn("Can not find Color swipe bar***")
                        else:
                            try:
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": ColorSwipeBar})
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": ColorSwipeBar})
                            except:
                                self.logger.logger.warn("Swipe color  bar Error***")
                            else:
                                sleep(1.5)
                        try:
                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                        except:
                            self.logger.logger.warn("Find the %s setting item error***" % Color)
                        else:
                            try:
                                ColorSetElement.click()
                            except:
                                self.logger.logger.warn("Set %s setting error***" % Color)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                    elif Color == "NONE" or Color == "LOG" or Color == "VIVID":
                        try:
                            ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                        except:
                            self.logger.logger.warn("Can not find Color swipe bar***")
                        else:
                            try:
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": ColorSwipeBar})
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": ColorSwipeBar})
                            except:
                                self.logger.logger.warn("Swipe color  bar Error***")
                            else:
                                sleep(1.5)
                        try:
                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                        except:
                            self.logger.logger.warn("Find the %s setting item error***" % Color)
                        else:
                            try:
                                ColorSetElement.click()
                            except:
                                self.logger.logger.warn("Set %s setting error***" % Color)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                    else:
                        try:
                            ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                        except:
                            self.logger.logger.warn("Can not find Color swipe bar***")
                        else:
                            try:
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": ColorSwipeBar})
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": ColorSwipeBar})
                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": ColorSwipeBar})
                            except:
                                self.logger.logger.warn("Swipe color  bar Error***")
                            else:
                                sleep(1.5)
                        try:
                            ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                        except:
                            self.logger.logger.warn("Find the %s setting item error***" % Color)
                        else:
                            try:
                                ColorSetElement.click()
                            except:
                                self.logger.logger.warn("Set %s setting error***" % Color)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})

            else:
                if Color == "DREAM" or Color == "CLASSIC" or Color == "NOSTALGIC":
                    try:
                        ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                    except:
                        self.logger.logger.warn("Can not find Color swipe bar***")
                    else:
                        try:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": ColorSwipeBar})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": ColorSwipeBar})
                        except:
                            self.logger.logger.warn("Swipe color  bar Error***")
                        else:
                            sleep(1.5)
                    try:
                        ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                    except:
                        self.logger.logger.warn("Find the %s setting item error***" % Color)
                    else:
                        try:
                            ColorSetElement.click()
                        except:
                            self.logger.logger.warn("Set %s setting error***" % Color)
                        else:
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
                elif Color == "NONE" or Color == "LOG" or Color == "VIVID":
                    try:
                        ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                    except:
                        self.logger.logger.warn("Can not find Color swipe bar***")
                    else:
                        try:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": ColorSwipeBar})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": ColorSwipeBar})
                        except:
                            self.logger.logger.warn("Swipe color  bar Error***")
                        else:
                            sleep(1.5)
                    try:
                        ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                    except:
                        self.logger.logger.warn("Find the %s setting item error***" % Color)
                    else:
                        try:
                            ColorSetElement.click()
                        except:
                            self.logger.logger.warn("Set %s setting error***" % Color)
                        else:
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
                else:
                    try:
                        ColorSwipeBar = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
                    except:
                        self.logger.logger.warn("Can not find Color swipe bar***")
                    else:
                        try:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": ColorSwipeBar})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": ColorSwipeBar})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": ColorSwipeBar})
                        except:
                            self.logger.logger.warn("Swipe color  bar Error***")
                        else:
                            sleep(1.5)
                    try:
                        ColorSetElement = self.InitalDevice.driver.find_element_by_accessibility_id(Color)
                    except:
                        self.logger.logger.warn("Find the %s setting item error***" % Color)
                    else:
                        try:
                            ColorSetElement.click()
                        except:
                            self.logger.logger.warn("Set %s setting error***" % Color)
                        else:
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
    def SetStyleInRecordMode(self,Style="STD",Sharpness="±0",Contrast="±0",Saturation="±0"):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'left', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            try:
                 SelectStyleSettingElement= self.InitalDevice.driver.find_element_by_accessibility_id("STYLE")
            except:
                self.logger.logger.warn(
                    "Can not find the Style setting item, maybe it is not on the camera interface***")
            else:
                try:
                    SelectStyleSettingElement.click()
                except:
                    self.logger.logger.warn(
                        "Select the Style setting item, maybe it is not on the camera interface***")
                else:
                    if Style == "STD" or Style == "LAND" or Style == "NEUT":
                        try:
                            StyleSwipeElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the style swipe bar, maybe it is not on the camera interface***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": StyleSwipeElement})
                            sleep(1.5)
                            try:
                                if Style == "STD":
                                    StyleItemElement = self.InitalDevice.driver.find_element_by_accessibility_id(" STD. ±0 ±0 ±0")
                                elif Style == "LAND":
                                    StyleItemElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        " LAND. +1 +1 ±0")
                                else:
                                    StyleItemElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        " NEUT. -1 ±0 ±0")
                            except:
                                self.logger.logger.warn(
                                    "Can not find the style item, maybe it is not on the camera interface***")
                            else:
                                try:
                                    StyleItemElement.click()
                                except:
                                    self.logger.logger.warn(
                                    "Set the %s style Error***"%Style)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                    else:
                        try:
                            StyleSwipeElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the style swipe bar, maybe it is not on the camera interface***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": StyleSwipeElement})
                            sleep(1.5)
                            try:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 304}) # go to custom style setting interface
                            except:
                                pass
                            else:
                                ##set Sharpness
                                #get current sharpness
                                CurrentSharpness = self.GetCurrentSharpnessSetting()
                                try:
                                    SharpnessSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(CurrentSharpness)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the sharpness setting control button***")
                                else:
                                    try:
                                        SharpnessSettingElement.click()
                                        if self.InitalDevice.checkUIElementExist(CurrentSharpness):
                                            SharpnessSettingElement.click()
                                            sleep(1.5)
                                        else:
                                            sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Go to  the sharpness setting interface error***")
                                    else:
                                        if Sharpness =="+1" or Sharpness =="+2" or Sharpness =="+3":
                                            try:
                                                SharpnessValueSwipBar= self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the sharpness value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": SharpnessValueSwipBar})
                                                sleep(1.5)
                                                tmpSharpness = " "+Sharpness
                                                try:
                                                    SharpnessValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(tmpSharpness)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the sharpness value item***")
                                                else:
                                                    try:
                                                        SharpnessValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the sharpness value Error***")
                                                    else:
                                                        #After set sharpness successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id("Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        elif Sharpness =="-1" or Sharpness =="-2" or Sharpness =="-3":
                                            try:
                                                SharpnessValueSwipBar= self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the sharpness value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SharpnessValueSwipBar})
                                                sleep(1.5)
                                                tmpSharpness = " "+Sharpness
                                                try:
                                                    SharpnessValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(tmpSharpness)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the sharpness value item***")
                                                else:
                                                    try:
                                                        SharpnessValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the sharpness value Error***")
                                                    else:
                                                        #After set sharpness successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id("Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        else:
                                            try:
                                                SharpnessValueSwipBar= self.InitalDevice.driver.find_element_by_xpath(
                                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the sharpness value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SharpnessValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SharpnessValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": SharpnessValueSwipBar})
                                                sleep(1.5)
                                                tmpSharpness = " "+Sharpness
                                                try:
                                                    SharpnessValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(tmpSharpness)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the sharpness value item***")
                                                else:
                                                    try:
                                                        SharpnessValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the sharpness value Error***")
                                                    else:
                                                        #After set sharpness successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id("Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                ##set Contrast
                                # get current Contrast
                                CurrentContrast = self.GetCurrentContrastSetting()
                                try:
                                    ContrastSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        CurrentContrast)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the Contrast setting control button***")
                                else:
                                    try:
                                        ContrastSettingElement.click()
                                        if  self.InitalDevice.checkUIElementExist(CurrentContrast):
                                            ContrastSettingElement.click()
                                            sleep(1.5)
                                        else:
                                            sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Go to  the Contrast setting interface error***")
                                    else:
                                        if Contrast == "+1" or Contrast == "+2" or Contrast == "+3":
                                            try:
                                                ContrastValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Contrast value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": ContrastValueSwipBar})
                                                sleep(1.5)
                                                tmpContrast = " " + Contrast
                                                try:
                                                    ContrastValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpContrast)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Contrast value item***")
                                                else:
                                                    try:
                                                        ContrastValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Contrast value Error***")
                                                    else:
                                                        # After set Contrast successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        elif Contrast == "-1" or Contrast == "-2" or Contrast == "-3":
                                            try:
                                                ContrastValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Contrast value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": ContrastValueSwipBar})
                                                sleep(1.5)
                                                tmpContrast = " " + Contrast
                                                try:
                                                    ContrastValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpContrast)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Contrast value item***")
                                                else:
                                                    try:
                                                        ContrastValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Contrast value Error***")
                                                    else:
                                                        # After set Contrast successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        else:
                                            try:
                                                ContrastValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Contrast value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": ContrastValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": ContrastValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": ContrastValueSwipBar})
                                                sleep(1.5)
                                                tmpContrast = " " + Contrast
                                                try:
                                                    ContrastValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpContrast)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Contrast value item***")
                                                else:
                                                    try:
                                                        ContrastValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Contrast value Error***")
                                                    else:
                                                        # After set Contrast successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                ##set Saturation
                                # get current Saturation
                                CurrentSaturation = self.GetCurrentSaturationSetting()
                                try:
                                    SaturationSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        CurrentSaturation)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the Saturation setting control button***")
                                else:
                                    try:
                                        SaturationSettingElement.click()
                                        if self.InitalDevice.checkUIElementExist(CurrentSaturation):
                                            SaturationSettingElement.click()
                                            sleep(1.5)
                                        else:
                                            sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Go to  the Saturation setting interface error***")
                                    else:
                                        if Saturation == "+1" or Saturation == "+2" or Saturation == "+3":
                                            try:
                                                SaturationValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Saturation value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": SaturationValueSwipBar})
                                                sleep(1.5)
                                                tmpSaturation = " " + Saturation
                                                try:
                                                    SaturationValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpSaturation)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Saturation value item***")
                                                else:
                                                    try:
                                                        SaturationValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Saturation value Error***")
                                                    else:
                                                        # After set Saturation successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        elif Saturation == "-1" or Saturation == "-2" or Saturation == "-3":
                                            try:
                                                SaturationValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Saturation value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SaturationValueSwipBar})
                                                sleep(1.5)
                                                tmpSaturation = " " + Saturation
                                                try:
                                                    SaturationValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpSaturation)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Saturation value item***")
                                                else:
                                                    try:
                                                        SaturationValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Saturation value Error***")
                                                    else:
                                                        # After set Saturation successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
                                        else:
                                            try:
                                                SaturationValueSwipBar = self.InitalDevice.driver.find_element_by_xpath(
                                                    "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                            except:
                                                self.logger.logger.warn(
                                                    "Can not find the Saturation value swipe bar***")
                                            else:
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SaturationValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'right',
                                                                                         "element": SaturationValueSwipBar})
                                                self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                                        {'direction': 'left',
                                                                                         "element": SaturationValueSwipBar})
                                                sleep(1.5)
                                                tmpSaturation = " " + Saturation
                                                try:
                                                    SaturationValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        tmpSaturation)
                                                except:
                                                    self.logger.logger.warn(
                                                        "Can not find the Saturation value item***")
                                                else:
                                                    try:
                                                        SaturationValueElement.click()
                                                    except:
                                                        self.logger.logger.warn(
                                                            "Set the Saturation value Error***")
                                                    else:
                                                        # After set Saturation successfully, go back to next top menu
                                                        try:
                                                            BackElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                                "Back")
                                                        except:
                                                            self.logger.logger.warn(
                                                                "Can not find the back control button***")
                                                        else:
                                                            BackElement.click()
                                                            sleep(1.5)
            #Exit style setting
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})

    def SetDigitalZoomInRecordMode(self,DigitalZoom):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'left', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            try:
                 SelectStyleSettingElement= self.InitalDevice.driver.find_element_by_accessibility_id("DIGITAL ZOOM")
            except:
                self.logger.logger.warn(
                    "Can not find the Digital Zoom setting item, maybe it is not on the camera interface***")
            else:
                try:
                    SelectStyleSettingElement.click()
                    sleep(1.5)
                except:
                    self.logger.logger.warn(
                        "Go to the Digital Zoom setting menu error***")
                else:
                    if DigitalZoom =="1.0×" or DigitalZoom =="2.0×" or DigitalZoom =="3.0×":
                        try:
                            DigitalZoomSwipe = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the Digital Zoom value swipe***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": DigitalZoomSwipe})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": DigitalZoomSwipe})
                            sleep(1.5)
                            try:
                                DigitalZoomElement = self.InitalDevice.driver.find_element_by_accessibility_id(DigitalZoom)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the Digital Zoom value item***")
                            else:
                                try:
                                    DigitalZoomElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the Digital Zoom %s value Error***"%DigitalZoom)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                    elif DigitalZoom =="6.0×" or DigitalZoom =="7.0×" or DigitalZoom =="8.0×":
                        try:
                            DigitalZoomSwipe = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the Digital Zoom value swipe***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": DigitalZoomSwipe})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": DigitalZoomSwipe})
                            sleep(1.5)
                            try:
                                DigitalZoomElement = self.InitalDevice.driver.find_element_by_accessibility_id(DigitalZoom)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the Digital Zoom value item***")
                            else:
                                try:
                                    DigitalZoomElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the Digital Zoom %s value Error***"%DigitalZoom)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                    else:
                        try:
                            DigitalZoomSwipe = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                        except:
                            self.logger.logger.warn(
                                "Can not find the Digital Zoom value swipe***")
                        else:
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": DigitalZoomSwipe})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": DigitalZoomSwipe})
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": DigitalZoomSwipe})
                            sleep(1.5)
                            try:
                                DigitalZoomElement = self.InitalDevice.driver.find_element_by_accessibility_id(DigitalZoom)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the Digital Zoom value item***")
                            else:
                                try:
                                    DigitalZoomElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the Digital Zoom %s value Error***"%DigitalZoom)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})

    def SetPIVInRecordMode(self,PIV):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            try:
                 SelectPIVSettingElement= self.InitalDevice.driver.find_element_by_accessibility_id("PIV")
            except:
                self.logger.logger.warn(
                    "Can not find the PIV setting item, maybe it is not on the camera interface***")
            else:
                try:
                    SelectPIVSettingElement.click()
                    sleep(1.5)
                except:
                    self.logger.logger.warn(
                        "Go to PIV setting menu error***")
                else:
                    if PIV == "MANUAL" or PIV =="5S" or PIV =="10S":
                        try:
                            PIVValueSelectElement = self.InitalDevice.driver.find_element_by_xpath(
                            "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": PIVValueSelectElement})
                            sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Can not find the PIV Value Select Element, maybe it is not on the camera interface***")
                        else:
                            try:
                                PIVValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    PIV)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the %s PIV Value***"%PIV)
                            else:
                                PIVValueElement.click()
                                #sleep(1)
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                    elif PIV == "30" or PIV =="60S":
                        try:
                            PIVValueSelectElement = self.InitalDevice.driver.find_element_by_xpath(
                                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": PIVValueSelectElement})
                            sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Can not find the PIV Value Select Element, maybe it is not on the camera interface***")
                        else:
                            try:
                                PIVValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    PIV)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the %s PIV Value***" % PIV)
                            else:
                                try:
                                    PIVValueElement.click()
                                    #sleep(1)
                                except:
                                    self.logger.logger.warn(
                                        "Set the %s PIV value error***" % PIV)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                    else:
                        self.logger.logger.warn(
                            "Input the wrong %s PIV setting value***"%PIV)




    def SetvideoStandardInRecordMode(self,standard):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            try:
                SelectVideoStandardSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("STANDARD")
            except:
                self.logger.logger.warn(
                    "Can not find the PIV setting item, maybe it is not on the camera interface***")
            else:
                try:
                    SelectVideoStandardSettingElement.click()
                except:
                    self.logger.logger.warn(
                        "Go to Video standard setting menu error***")
                else:
                    try:
                        StandardValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            standard)
                    except:
                        self.logger.logger.warn(
                            "Can not find the %s video standard Value***" % standard)
                    else:
                        try:
                            StandardValueElement.click()
                        except:
                            self.logger.logger.warn(
                                "Set the %s video standard value error***" % standard)
                        else:
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
    def SetVideoFormatInRecordMode(self, format):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            try:
                SelectVideoFormatSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("FORMAT")
            except:
                self.logger.logger.warn(
                    "Can not find the Format setting item, maybe it is not on the camera interface***")
            else:
                try:
                    SelectVideoFormatSettingElement.click()
                except:
                    self.logger.logger.warn(
                        "Go to Video format setting menu error***")
                else:
                    try:
                        VideoFormatValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            format)
                    except:
                        self.logger.logger.warn(
                            "Can not find the %s video format Value***" % format)
                    else:
                        try:
                            VideoFormatValueElement.click()
                        except:
                            self.logger.logger.warn(
                                "Set the %s video format value error***" % format)
                        else:
                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                    {"x": 333,
                                                                     "y": 187})
    def SetVideoResolutionInRecordMode(self,resolution):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            try:
                SelectVideoResolutionSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("RESOLUTION")
            except:
                self.logger.logger.warn(
                    "Can not find the video resolution setting item, maybe it is not on the camera interface***")
            else:
                try:
                    SelectVideoResolutionSettingElement.click()
                except:
                    self.logger.logger.warn(
                        "Go to video resolution setting menu error***")
                else:
                    if resolution =="4K+(4096X2160)" or resolution =="4K(3840X2160)" or resolution =="2.7K(2720X1530)":
                        try:
                            ResolutionValueSelectElement = self.InitalDevice.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'right',
                                                                     "element": ResolutionValueSelectElement})
                            sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Can not find the resolution value select element, maybe it is not on the camera interface***")
                        else:
                            try:
                                resolutionValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(resolution)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the %s resolution value itme***"%resolution)
                            else:
                                try:
                                    resolutionValueElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the %s video resolution value error***" % resolution)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})
                    else:
                        try:
                            ResolutionValueSelectElement = self.InitalDevice.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                    {'direction': 'left',
                                                                     "element": ResolutionValueSelectElement})
                            sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Can not find the resolution value select element, maybe it is not on the camera interface***")
                        else:
                            try:
                                resolutionValueElement = self.InitalDevice.driver.find_element_by_accessibility_id(resolution)
                            except:
                                self.logger.logger.warn(
                                    "Can not find the %s resolution value itme***"%resolution)
                            else:
                                try:
                                    resolutionValueElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Set the %s video resolution value error***" % resolution)
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 333,
                                                                             "y": 187})


    def GetCurrentFrameRate(self):
        is24fpsExist = self.InitalDevice.checkUIElementExist("24 FPS")
        is25fpsExist = self.InitalDevice.checkUIElementExist("25 FPS")
        is30fpsExist = self.InitalDevice.checkUIElementExist("30 FPS")
        is48fpsExist = self.InitalDevice.checkUIElementExist("48 FPS")
        is50fpsExist = self.InitalDevice.checkUIElementExist("50 FPS")
        is60fpsExist = self.InitalDevice.checkUIElementExist("60 FPS")
        is120fpsExist = self.InitalDevice.checkUIElementExist("120 FPS")
        is240fpsExist = self.InitalDevice.checkUIElementExist("240 FPS")
        if is24fpsExist:
            return "24 FPS"
        if is25fpsExist:
            return "25 FPS"
        if is30fpsExist:
            return "30 FPS"
        if is48fpsExist:
            return "48 FPS"
        if is50fpsExist:
            return "50 FPS"
        if is60fpsExist:
            return "60 FPS"
        if is120fpsExist:
            return "120 FPS"
        if is240fpsExist:
            return "240 FPS"
    def SetVideoFrameRateInRecordMode(self,framerate):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            BottomSetBarElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
            self.InitalDevice.driver.execute_script("mobile: swipe",
                                                    {'direction': 'right', "element": BottomSetBarElement})
            sleep(1.5)
        except:
            self.logger.logger.warn("Can not find the bottom set bar, maybe it is not on the camera interface***")
        else:
            try:
                SelectVideoFrameRateSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                    "FRAME RATE")
            except:
                self.logger.logger.warn(
                    "Can not find the video frame rate setting item, maybe it is not on the camera interface***")
            else:
                CurrentFrameRate = self.GetCurrentFrameRate()
                if CurrentFrameRate !=None:
                    CurrentFrameRateValue = int(CurrentFrameRate.replace("FPS","").replace(" ",""))
                    framerateValue = int(framerate.replace("FPS","").replace(" ",""))
                    try:
                        SelectVideoFrameRateSettingElement.click()
                    except:
                        self.logger.logger.warn(
                            "Can not find the video frame rate select element, maybe it is not on the camera interface***")
                    else:
                        try:
                            VideoFrameRateElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                framerate)
                            VideoFrameRateElementLocation = VideoFrameRateElement.location
                            if VideoFrameRateElementLocation["x"] > 667 or VideoFrameRateElementLocation["x"] < 0:
                                self.logger.logger.warn(
                                    "FrameRate Element is not visiable***")
                                raise AttributeError
                        except:
                            if framerateValue < CurrentFrameRateValue:
                                try:
                                    FrameRateValueSelectElement = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'left',
                                                                         "element": FrameRateValueSelectElement})
                                    sleep(1.5)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the video frame rate value select element***")
                                else:
                                    try:
                                        VideoFrameRateElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        framerate)
                                    except:
                                        self.logger.logger.warn(
                                            "Can not find the video %s frame rate value***"%framerate)
                                    else:
                                        try:
                                            VideoFrameRateElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Set the video %s frame rate error***" % framerate)
                                        else:
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                            elif framerateValue > CurrentFrameRateValue:
                                try:
                                    FrameRateValueSelectElement = self.InitalDevice.driver.find_element_by_xpath(
                                        "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
                                    self.InitalDevice.driver.execute_script("mobile: swipe",
                                                                        {'direction': 'right',
                                                                         "element": FrameRateValueSelectElement})
                                    sleep(1.5)
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the video frame rate value select element***")
                                else:
                                    try:
                                        VideoFrameRateElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        framerate)
                                    except:
                                        self.logger.logger.warn(
                                            "Can not find the video %s frame rate value***"%framerate)
                                    else:
                                        try:
                                            VideoFrameRateElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Set the video %s frame rate error***" % framerate)
                                        else:
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 333,
                                                                                     "y": 187})
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
    
                        else:
                            try:
                                VideoFrameRateElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Set the video %s frame rate error***" % framerate)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 333,
                                                                         "y": 187})
                else:
                    self.logger.logger.warn(
                        "Can not get  the current video %s frame rate value***")
    def startRecord(self):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            startRecordElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console video normal")
        except:
            self.logger.logger.warn(
                "Can not find the start record control button***")
        else:
            try:
               startRecordElement.click()
               sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Start  record error***")
            else:
                try:
                    checkSDCardFullElement = self.InitalDevice.driver.find_element_by_accessibility_id("SD card is full")
                except:
                    pass
                else:
                    self.logger.logger.warn(
                        "SD card is full!!!")
                    self.FormatSDcardWithCameraSetting()
                    try:
                        startRecordElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            "Btn console video normal")
                    except:
                        self.logger.logger.warn(
                            "Can not find the start record control button***")
                    else:
                        try:
                            startRecordElement.click()
                        except:
                            self.logger.logger.warn(
                                "Start  record error***")
                        else:
                            pass

    def stopRecord(self):
        try:
            stopRecordElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console video recording")
        except:
            self.logger.logger.warn(
                "Can not find the stop record control button***")
        else:
            try:
                stopRecordElement.click()
            except:
                self.logger.logger.warn(
                    "Stop record error***")
            else:
                sleep(0.5)
    def GotoAlbumInRecordMode(self):
        self.SwitchtoRecordMode()
        sleep(1.5)
        try:
            AlbumEnterElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]")
        except:
            self.logger.logger.warn(
                "Can not find the album control button***")
        else:
            try:
                AlbumEnterElement.click()
            except:
                self.logger.logger.warn(
                    "Go to the album error***")
            else:
                sleep(1.5)
    def ZoomThePhotoPreview(self,zoom=2.0,speed=1.0):
        try:
            imagepreviewElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage")
        except:
            self.logger.logger.warn(
                "Can not find the image preview***")
        else:
            try:
               self.InitalDevice.driver.execute_script('mobile: pinch', {'scale': zoom, 'velocity': speed, 'element': imagepreviewElement})
            except:
                self.logger.logger.warn(
                    "Zoom the image preview error***")
            else:
                pass
    def DragVideoPlayProgress(self,progress="0.5"):
        try:
            playsliderElement = self.InitalDevice.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSlider")
        except:
            self.logger.logger.warn(
                "Can no find the slider***")
        else:
            playsliderElement.send_keys(progress)

    def PauseContinuePlayVideo(self,sleeptime = 1):
        try:
            playPauseElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn Play Normal")
        except:
            pass
        else:
            try:
                playPauseElement.click()
            except:
                self.logger.logger.warn(
                    "Pause playing the video preview error***")
            else:
                sleep(sleeptime)


    def PlayVideoInSingleAlbum(self):
        try:
            playIconElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn ClickedPlay")
        except:
            self.logger.logger.warn(
                "Current item is not the video preview***")
        else:
            try:
                playIconElement.click()
            except:
                self.logger.logger.warn(
                    "Play the video preview error***")
            else:
                self.InitalDevice.driver.execute_script("mobile: tap",
                                                        {"x": 200,
                                                         "y": 187})
                # try:
                #     playsliderElement = self.InitalDevice.driver.find_element_by_xpath(
                #         "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSlider")
                # except:
                #     self.logger.logger.warn(
                #         "Can no find the slider***")
                # else:
                #     playsliderElement.send_keys("0.5")
                # sleep(1)
                # try:
                #     playPauseElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn Play Normal")
                # except:
                #     pass
                # else:
                #     try:
                #         playPauseElement.click()
                #     except:
                #         self.logger.logger.warn(
                #             "Pause playing the video preview error***")
                #     else:
                #         sleep(1)
                #     try:
                #         playsliderElement = self.InitalDevice.driver.find_element_by_xpath(
                #             "//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSlider")
                #     except:
                #         self.logger.logger.warn(
                #             "Can no find the slider***")
                #     else:
                #         playsliderElement.send_keys("0.5")
                #     sleep(1)
                #     try:
                #         playPauseElement.click()
                #     except:
                #         self.logger.logger.warn(
                #             "Go on playing the video preview error***")
                #     else:
                #         sleep(1.5)
                # while True:
                #     try:
                #         playIconElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn ClickedPlay")
                #     except:
                #         try:
                #             playPauseElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn Play Normal")
                #         except:
                #             pass
                #         else:
                #             try:
                #                 playIconElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                #                     "Btn ClickedPlay")
                #             except:
                #                 pass
                #             else:
                #                 break
                #             # try:
                #             #     ProgressElement=self.InitalDevice.driver.find_element_by_accessibility_id("Progress")
                #             # except:
                #             #     self.logger.logger.warn(
                #             #         "Can not find the progress***")
                #             # else:
                #             #     TouchAction(self.InitalDevice.driver)
                #             try:
                #                 playPauseElement.click()
                #             except:
                #                 self.logger.logger.warn(
                #                     "Pause playing the video preview error***")
                #             else:
                #                 sleep(0.5)
                #             try:
                #                 playPauseElement.click()
                #             except:
                #                 self.logger.logger.warn(
                #                     "Go on playing the video preview error***")
                #             else:
                #                 sleep(10)
                #
                #     else:
                #         # self.InitalDevice.driver.execute_script("mobile: tap",
                #         #                                         {"x": 200,
                #         #                                          "y": 187})
                #         break
    def SwipeLeftUntilFindVideo(self):
        try:
            AlbumMainWindowElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            try:
                SelectAllElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
            except:
                self.logger.logger.warn(
                    "Can not find the album main window, may be it is not in Album interface***")
            else:
                self.SelectNLNCItem(1, 1)
                while True:
                    try:
                        TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(x=0,
                                                                                                             y=187).release().perform()
                        # sleep(0.5)
                    except:
                        self.logger.logger.warn(
                            "Swipe the album main window error***")
                    else:
                        sleep(0.5)
                        try:
                            playIconElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "Btn ClickedPlay")
                        except:
                            try:
                                NoMoreDataElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    "No more data...")
                            except:
                                self.logger.logger.warn(
                                    "Current item is not the video preview***")
                            else:
                                sleep(1.5)
                                break
                        else:
                            sleep(1.5)
                            break
        else:
            while True:
                try:
                    TouchAction(self.InitalDevice.driver).long_press(x=333,y=187,duration=100).move_to(x=0, y=187).release().perform()
                    #sleep(0.5)
                except:
                    self.logger.logger.warn(
                        "Swipe the album main window error***")
                else:
                    sleep(0.5)
                    try:
                        playIconElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            "Btn ClickedPlay")
                    except:
                        try:
                            NoMoreDataElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "No more data...")
                        except:
                            self.logger.logger.warn(
                                "Current item is not the video preview***")
                        else:
                            sleep(1.5)
                            break
                    else:
                        sleep(1.5)
                        break

    def GotoMultiAlbumInRecordMode(self):
        self.GotoAlbumInRecordMode()
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            self.logger.logger.warn(
                "Can not find the muti-album control button,may be it is not in Album interface***")
        else:
            try:
                MultAblumEnterElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Go to the muti album error***")
            else:
                pass
    def GotoMultiAlbumInSigleAlbum(self):
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            self.logger.logger.warn(
                "Can not find the muti-album control button,may be it is not in Album interface***")
        else:
            try:
                MultAblumEnterElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Go to the muti album error***")
            else:
                pass
    def EXitAlbum(self):
        try:
            AlbumBackElement = self.InitalDevice.driver.find_element_by_accessibility_id("Back")
        except:
            self.logger.logger.warn(
                "Can not find the album back control button***")
            self.InitalDevice.driver.execute_script("mobile: tap",
                                                    {"x": 333,
                                                     "y": 187})
            try:
                AlbumBackElement = self.InitalDevice.driver.find_element_by_accessibility_id("Back")
            except:
                self.logger.logger.warn(
                    "Can not find the album back control button***")
            else:
                try:
                    AlbumBackElement.click()
                except:
                    self.logger.logger.warn(
                        "Exit album error***")
                else:
                    pass
        else:
            try:
                AlbumBackElement.click()
            except:
                self.logger.logger.warn(
                    "Exit album error***")
            else:
                pass

    def SwipeLeftInAlbum(self,number):
        try:
            AlbumMainWindowElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            try:
                SelectAllElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
            except:
                self.logger.logger.warn(
                    "Can not find the album main window, may be it is not in Album interface***")
            else:
                self.SelectNLNCItem(1, 1)
                for i in range(0, number, 1):
                    try:
                        TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(x=0,
                                                                                                             y=187).release().perform()
                        # sleep(0.5)
                    except:
                        self.logger.logger.warn(
                            "Swipe the album main window error***")
                    else:
                        pass
                sleep(0.5)
        else:
            for i in range(0,number,1):
                try:
                    TouchAction(self.InitalDevice.driver).long_press(x=333,y=187,duration=100).move_to(x=0, y=187).release().perform()
                    #sleep(0.5)
                except:
                    self.logger.logger.warn(
                        "Swipe the album main window error***")
                else:
                    pass
            sleep(0.5)
    def SwipeRightInAlbum(self,number):
        try:
            AlbumMainWindowElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            try:
                SelectAllElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
            except:
                self.logger.logger.warn(
                    "Can not find the album main window, may be it is not in Album interface***")
            else:
                self.SelectNLNCItem(1, 1)
                for i in range(0, number, 1):
                    try:
                        TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(x=0,
                                                                                                             y=187).release().perform()
                        # sleep(0.5)
                    except:
                        self.logger.logger.warn(
                            "Swipe the album main window error***")
                    else:
                        pass
                sleep(0.5)
        else:
            for i in range(0,number,1):
                try:
                    TouchAction(self.InitalDevice.driver).long_press(x=333,y=187,duration=100).move_to(x=667,
                                                                                           y=187).release().perform()
                    #sleep(0.5)
                except:
                    self.logger.logger.warn(
                        "Swipe the album main window error***")
                else:
                    pass
            sleep(0.5)


    def SwipeUpInMultiAlbum(self,number):
        self.GotoAlbumInRecordMode()
        sleep(1.5)
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            try:
                SelectAllElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
            except:
                self.logger.logger.warn(
                    "Can not find the select all control button,may be it is not in multi Album select interface***")
            else:
                # swipe up...
                for i in range(0, number, 1):
                    try:
                        TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(x=333,
                                                                                                             y=0).release().perform()
                        # sleep(0.5)
                    except:
                        self.logger.logger.warn(
                            "Swipe the album main window error***")
                    else:
                        pass
                        sleep(0.5)
        else:
            try:
                MultAblumEnterElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Go to the muti album error***")
            else:
                # swipe up...
                for i in range(0, number, 1):
                    try:
                        TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(x=333,
                                                                                                             y=0).release().perform()
                        # sleep(0.5)
                    except:
                        self.logger.logger.warn(
                            "Swipe the album main window error***")
                    else:
                        pass
                        sleep(0.5)

    def SwipeDownInMultiAlbum(self,number):
        self.GotoAlbumInRecordMode()
        sleep(1.5)
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            try:
                SelectAllElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
            except:
                self.logger.logger.warn(
                    "Can not find the select all control button,may be it is not in multi Album select interface***")
            else:
                # swipe up...
                for i in range(0, number, 1):
                    try:
                        TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(x=333,
                                                                                                             y=300).release().perform()
                        # sleep(0.5)
                    except:
                        self.logger.logger.warn(
                            "Swipe the album main window error***")
                    else:
                        pass
                        sleep(0.5)
        else:
            try:
                MultAblumEnterElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Go to the muti album error***")
            else:
                # swipe up...
                for i in range(0, number, 1):
                    try:
                        TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(x=333,
                                                                                                             y=300).release().perform()
                        # sleep(0.5)
                    except:
                        self.logger.logger.warn(
                            "Swipe the album main window error***")
                    else:
                        pass
                        sleep(0.5)

    def DownLoadCurrentSigleItemInAlbum(self):
        try:
            DownloadElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn Download Normal")
        except:
            self.logger.logger.warn(
                "Can not find the download control button***")
        else:
            try:
                DownloadElement.click()
            except:
                self.logger.logger.warn(
                    "Download all itmes in album error***")
            else:
                try:
                    HasCheckDialogElement = self.InitalDevice.driver.find_element_by_accessibility_id("OK")
                except:
                    pass
                else:
                    HasCheckDialogElement.click()

                while True:
                    try:
                        SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
                    except:
                        sleep(0.1)
                    else:
                        self.logger.logger.warn(
                            "Download itme in album successfully!!!")
                        break


    def DownSelectMultiItemsInAlbum(self,SwipeUpNum=1, SwipeDownNum=1,SelectNumber=1):
        self.GotoAlbumInRecordMode()
        sleep(1.5)
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            try:
                SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
            except:
                self.logger.logger.warn(
                    "Can not find the select album control button,may be it is not in multi Album interface***")
            else:
                self.SwipeUpInMultiAlbum(SwipeUpNum)
                self.SwipeDownInMultiAlbum(SwipeDownNum)
                try:
                    SelectEnterElement.click()
                except:
                    self.logger.logger.warn(
                        "Go to the select album error***")
                else:
                    for i in range(0, SelectNumber, 1):
                        N1 = random.randint(1, 2)
                        M1 = random.randint(1, 5)
                        self.SelectNLNCItem(N1, M1)
                    try:
                        DownloadElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            "Btn Download Normal")
                    except:
                        self.logger.logger.warn(
                            "Can not find the download control button***")
                    else:
                        try:
                            DownloadElement.click()
                        except:
                            self.logger.logger.warn(
                                "Download all itmes in album error***")
                        else:
                            try:
                                HasCheckDialogElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    "OK")
                            except:
                                pass
                            else:
                                try:
                                   HasCheckDialogElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Check download all itmes in album error***")
                                else:
                                    waitloops = 0
                                    while True:
                                        try:
                                            SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                "Select")
                                        except:
                                            if waitloops > 300:
                                                try:
                                                    CancelElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        "Cancel")
                                                except:
                                                    pass
                                                else:
                                                    CancelElement.click()
                                                    sleep(1)
                                            sleep(1.5)
                                            waitloops = waitloops + 1
                                        else:
                                            if SelectEnterElement.is_displayed():
                                                break
                                            waitloops = waitloops + 1
        else:
            try:
                MultAblumEnterElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Go to the muti album error***")
            else:
                try:
                    SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
                except:
                    self.logger.logger.warn(
                        "Can not find the select album control button,may be it is not in multi Album interface***")
                else:
                    self.SwipeUpInMultiAlbum(SwipeUpNum)
                    self.SwipeDownInMultiAlbum(SwipeDownNum)
                    try:
                        SelectEnterElement.click()
                    except:
                        self.logger.logger.warn(
                            "Go to the select album error***")
                    else:
                        for i in range(0, SelectNumber, 1):
                            N1 = random.randint(1, 2)
                            M1 = random.randint(1, 5)
                            self.SelectNLNCItem(N1, M1)
                        try:
                            DownloadElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "Btn Download Normal")
                        except:
                            self.logger.logger.warn(
                                "Can not find the download control button***")
                        else:
                            try:
                                DownloadElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Download all itmes in album error***")
                            else:
                                try:
                                    HasCheckDialogElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                        "OK")
                                except:
                                    pass
                                else:
                                    try:
                                        HasCheckDialogElement.click()
                                    except:
                                        self.logger.logger.warn(
                                            "Check download all itmes in album error***")
                                    else:
                                        waitloops = 0
                                        while True:
                                            try:
                                                SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                    "Select")
                                            except:
                                                if waitloops >100:
                                                    try:
                                                        CancelElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                            "Cancel")
                                                    except:
                                                        pass
                                                    else:
                                                        CancelElement.click()
                                                        sleep(1)
                                                sleep(1.5)
                                                waitloops = waitloops +1
                                            else:
                                                if SelectEnterElement.is_displayed():
                                                    break
                                                waitloops = waitloops +1

    def DeleteSelectMultiItemsInAlbum(self,SwipeUpNum=1, SwipeDownNum=1,SelectNumber=1):
        self.GotoAlbumInRecordMode()
        sleep(1.5)
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            try:
                SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
            except:
                self.logger.logger.warn(
                    "Can not find the select album control button,may be it is not in multi Album interface***")
            else:
                self.SwipeUpInMultiAlbum(SwipeUpNum)
                self.SwipeDownInMultiAlbum(SwipeDownNum)
                try:
                    SelectEnterElement.click()
                except:
                    self.logger.logger.warn(
                        "Go to the select album error***")
                else:
                    for i in range(0, SelectNumber, 1):
                        N1 = random.randint(1, 2)
                        M1 = random.randint(1, 5)
                        self.SelectNLNCItem(N1, M1)
                    # delete selected multi item in multi album
                    try:
                        DeletElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                            "Btn Delete Normal")
                    except:
                        self.logger.logger.warn(
                            "Can not find the delete control***")
                    else:
                        try:
                            DeletElement.click()
                            sleep(1.5)
                        except:
                            self.logger.logger.warn(
                                "Click the delete control error***")
                        else:
                            try:
                                TouchAction(self.InitalDevice.driver).tap(x=242, y=338).perform()
                            except:
                                self.logger.logger.warn(
                                    "Delete selected multi items in multi album error***")
                            else:
                                while True:
                                    try:
                                        SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                            "Select")
                                    except:
                                        try:
                                            SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                "Album")
                                        except:
                                            sleep(1.5)
                                        else:
                                            break

                                    else:
                                        if SelectEnterElement.is_displayed():
                                            break
        else:
            try:
                MultAblumEnterElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Go to the muti album error***")
            else:
                try:
                    SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
                except:
                    self.logger.logger.warn(
                        "Can not find the select album control button,may be it is not in multi Album interface***")
                else:
                    self.SwipeUpInMultiAlbum(SwipeUpNum)
                    self.SwipeDownInMultiAlbum(SwipeDownNum)
                    try:
                        SelectEnterElement.click()
                    except:
                        self.logger.logger.warn(
                            "Go to the select album error***")
                    else:
                        for i in range(0, SelectNumber, 1):
                            N1 = random.randint(1, 2)
                            M1 = random.randint(1, 5)
                            self.SelectNLNCItem(N1, M1)
                        # delete selected multi item in multi album
                        try:
                            DeletElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "Btn Delete Normal")
                        except:
                            self.logger.logger.warn(
                                "Can not find the delete control***")
                        else:
                            try:
                                DeletElement.click()
                                sleep(1.5)
                            except:
                                self.logger.logger.warn(
                                    "Click the delete control error***")
                            else:
                                try:
                                    TouchAction(self.InitalDevice.driver).tap(x=242, y=338).perform()
                                except:
                                    self.logger.logger.warn(
                                        "Delete selected multi items in multi album error***")
                                else:
                                    while True:
                                        try:
                                            SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                "Select")
                                        except:
                                            try:
                                                SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                    "Album")
                                            except:
                                                sleep(1.5)
                                            else:
                                                break
                                        else:
                                            if SelectEnterElement.is_displayed():
                                                break








    def DownAllItemsInAlbum(self):
        self.GotoAlbumInRecordMode()
        sleep(1.5)
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            try:
                SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
            except:
                self.logger.logger.warn(
                    "Can not find the select album control button,may be it is not in multi Album interface***")
            else:
                try:
                    SelectEnterElement.click()
                except:
                    self.logger.logger.warn(
                        "Go to the select all album error***")
                else:
                    try:
                        SelectAllElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select All")
                    except:
                        self.logger.logger.warn(
                            "Can not find the select all control button,may be it is not in multi Album select interface***")
                    else:
                        try:
                            SelectAllElement.click()
                        except:
                            self.logger.logger.warn(
                                "Select all items error***")
                        else:
                            try:
                                DownloadElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    "Btn Download Normal")
                            except:
                                self.logger.logger.warn(
                                    "Can not find the download control button***")
                            else:
                                try:
                                    DownloadElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Download all itmes in album error***")
                                else:
                                    try:
                                        HasCheckDialogElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                            "OK")
                                    except:
                                        pass
                                    else:
                                        try:
                                            HasCheckDialogElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Check download all itmes in album error***")
                                        else:
                                            while True:
                                                try:
                                                    SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                        "Select")
                                                except:
                                                    sleep(1.5)
                                                else:
                                                    self.EXitAlbum()
                                                    break
        else:
            try:
                MultAblumEnterElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Go to the muti album error***")
            else:
                # swip up until get no more data ...
                while True:
                    try:
                        TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(
                            x=333,
                            y=0).release().perform()
                        sleep(0.5)
                    except:
                        self.logger.logger.warn(
                            "Swip muli album to the bottom in multi album error***")
                        break
                    else:
                        try:
                            NoMoreDataElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "No more data...")
                        except:
                            self.logger.logger.warn(
                                "Did not swip to the bottom in multi album")
                        else:
                            break
                try:
                    SelectEnterElement=self.InitalDevice.driver.find_element_by_accessibility_id("Select")
                except:
                    self.logger.logger.warn(
                        "Can not find the select album control button,may be it is not in multi Album interface***")
                else:
                    try:
                        SelectEnterElement.click()
                    except:
                        self.logger.logger.warn(
                            "Go to the select all album error***")
                    else:
                        try:
                            SelectAllElement=self.InitalDevice.driver.find_element_by_accessibility_id("Select All")
                        except:
                            self.logger.logger.warn(
                                "Can not find the select all control button,may be it is not in multi Album select interface***")
                        else:
                            try:
                               SelectAllElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Select all items error***")
                            else:
                                try:
                                    DownloadElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn Download Normal")
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the download control button***")
                                else:
                                    try:
                                        DownloadElement.click()
                                    except:
                                        self.logger.logger.warn(
                                            "Download all itmes in album error***")
                                    else:
                                        try:
                                            HasCheckDialogElement = self.InitalDevice.driver.find_element_by_accessibility_id("OK")
                                        except:
                                            pass
                                        else:
                                            try:
                                                HasCheckDialogElement.click()
                                            except:
                                                self.logger.logger.warn(
                                                    "Check download all itmes in album error***")
                                            else:
                                                while True:
                                                    try:
                                                        SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                                            "Select")
                                                    except:
                                                        sleep(1.5)
                                                    else:
                                                        self.EXitAlbum()
                                                        break
    def checkSDisFullWithPopSDFullDialog(self):
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("SD card is full")
        except:
            #self.logger.logger.warn(
                #"SD is not full***")
            return False
        else:
            self.logger.logger.warn(
             "SD is full***")
            return True
    def FormatSDCardWithPopSDFullDialog(self):
        if self.checkSDisFullWithPopSDFullDialog():
            try:
                FormatItemElement = self.InitalDevice.driver.find_element_by_accessibility_id("Format")
            except:
                self.logger.logger.warn(
                    "Can not find format control***")
            else:
                try:
                    FormatItemElement.click()
                except:
                    self.logger.logger.warn(
                        "Format sd card error***")
                else:
                    pass
        else:
            pass
    def CancelFormatSDCardWithPopSDFullDialog(self):
        if self.checkSDisFullWithPopSDFullDialog():
            try:
                CancelFormatItemElement = self.InitalDevice.driver.find_element_by_accessibility_id("Cancel")
            except:
                self.logger.logger.warn(
                    "Can not find Cancel control***")
            else:
                try:
                    CancelFormatItemElement.click()
                except:
                    self.logger.logger.warn(
                        "Cancel sd card error***")
        else:
            pass

    def FormatSDcardWithCameraSetting(self):
        self.GoToCameraMainWindow()
        sleep(1.5)
        #if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    TouchAction(self.InitalDevice.driver).long_press(x=503,y=204,duration=100).move_to(x=503,
                                                                                           y=1).release().perform()
                    #sleep(0.5)
                except:
                    self.logger.logger.warn(
                        "Swipe the camera setting menu error***")
                else:
                    try:
                        FormatItemElement = self.InitalDevice.driver.find_element_by_accessibility_id("Format SD Card")
                        FormatItemElementLocation = FormatItemElement.location
                        if FormatItemElementLocation["x"] > 667 or FormatItemElementLocation["x"] < 0:
                            self.logger.logger.warn(
                            "Format Element is not visiable***")
                            raise AttributeError
                    except:
                        try:
                            TouchAction(self.InitalDevice.driver).long_press(x=503, y=204, duration=100).move_to(x=503,
                                                                                                                 y=1).release().perform()
                            # sleep(0.5)
                        except:
                            self.logger.logger.warn(
                                "Swipe the camera setting menu error***")
                        else:
                            try:
                                FormatItemElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                    "Format SD Card")
                                FormatItemElementLocation = FormatItemElement.location
                                if FormatItemElementLocation["x"] > 667 or FormatItemElementLocation["x"] < 0:
                                    self.logger.logger.warn(
                                        "Format Element is not visiable***")
                                    raise AttributeError
                            except:
                                self.logger.logger.warn(
                                    "Can not find format element***")
                            else:
                                try:
                                    FormatItemElement.click()
                                    sleep(1)
                                except:
                                    self.logger.logger.warn(
                                        "format SD card error***")
                                else:
                                    try:
                                        FormatDialogElement = self.InitalDevice.driver.find_element_by_accessibility_id("Format")
                                    except:
                                        self.logger.logger.warn(
                                            "Can not find format control***")
                                    else:
                                        try:
                                            FormatDialogElement.click()
                                        except:
                                            self.logger.logger.warn(
                                                "Format sd card error***")
                                        else:
                                            self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                    {"x": 200,
                                                                                     "y": 187})
                    else:
                        try:
                            FormatItemElement.click()
                            sleep(1)
                        except:
                            self.logger.logger.warn(
                                "format SD card error***")
                        else:
                            try:
                                FormatDialogElement = self.InitalDevice.driver.find_element_by_accessibility_id("Format")
                            except:
                                self.logger.logger.warn(
                                    "Can not find format control***")
                            else:
                                try:
                                    FormatDialogElement.click()
                                except:
                                    self.logger.logger.warn(
                                        "Format sd card error***")
                                else:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 200,
                                                                             "y": 187})
    def SwitchRecordSubtitle(self,Flag = "On"):
        self.SwitchtoRecordMode()
        sleep(1.5)
        # if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                "Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    subutitleElemet = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeSwitch[@name=\"Subtitle .ass Files\"]")
                    CurrentSubtitleSwitchValue = subutitleElemet.text
                except:
                    self.logger.logger.warn(
                        "Can not find subtitle setting control***")
                else:
                    if Flag =="On":
                        if CurrentSubtitleSwitchValue =="1":
                            return
                        else:
                            try:
                                subutitleElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Set subtitle error***")
                            else:
                                if CurrentSubtitleSwitchValue != subutitleElemet.text:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 200,
                                                                             "y": 187})
                                else:
                                    self.logger.logger.warn(
                                        "Set subtitle error***")
                    elif Flag =="Off":
                        if CurrentSubtitleSwitchValue =="0":
                            return
                        else:
                            try:
                                subutitleElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Set subtitle error***")
                            else:
                                if CurrentSubtitleSwitchValue != subutitleElemet.text:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 200,
                                                                             "y": 187})
                                else:
                                    self.logger.logger.warn(
                                        "Set subtitle error***")



    def DeleteCurrentItemInSingleAlbum(self):
        try:
            iSInSingleAblumElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            self.logger.logger.warn(
                "it is not in single album interface***")
        else:
            try:
                DeleteElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn Delete Normal")
            except:
                self.logger.logger.warn(
                    "Can not find delete control in single album interface***")
            else:
                try:
                    DeleteElement.click()
                except:
                    self.logger.logger.warn(
                        "Click delete control in single album interface error***")
                else:
                    iSDeleteVideoElemetExist = self.InitalDevice.checkUIElementExist("Delete Video")
                    iSDeletePhotoElemetExist = self.InitalDevice.checkUIElementExist("Delete Photo")
                    if iSDeleteVideoElemetExist:
                        try:
                            DeleteVideoElemet = self.InitalDevice.driver.find_element_by_accessibility_id("Delete Video")
                        except:
                            self.logger.logger.warn(
                                "Can not find Delete Video control in single album interface***")
                        else:
                            try:
                                DeleteVideoElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Delete item in single album error***")
                            else:
                                sleep(0.5)
                    if iSDeletePhotoElemetExist:
                        try:
                            DeletePhotoElemet = self.InitalDevice.driver.find_element_by_accessibility_id("Delete Photo")
                        except:
                            self.logger.logger.warn(
                                "Can not find Delete Photo control in single album interface***")
                        else:
                            try:
                               DeletePhotoElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Delete item in single album error***")
                            else:
                                sleep(0.5)

    def DeleteAllItemInMultiAlbum(self):
        self.GotoAlbumInRecordMode()
        sleep(1.5)
        try:
            MultAblumEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Album")
        except:
            self.logger.logger.warn(
                "Can not find the muti-album control button,may be it is not in Album interface***")
        else:
            try:
                MultAblumEnterElement.click()
                sleep(0.5)
            except:
                self.logger.logger.warn(
                    "Go to the muti album error***")
            else:
                # swip up until get no more data ...
                while True:
                    try:
                        TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(
                            x=333,
                            y=0).release().perform()
                        sleep(0.5)
                    except:
                        self.logger.logger.warn(
                            "Swip muli album to the bottom in multi album error***")
                        break
                    else:
                        try:
                            NoMoreDataElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                                "No more data...")
                        except:
                            self.logger.logger.warn(
                                "Did not swip to the bottom in multi album")
                        else:
                            break
                try:
                    SelectEnterElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select")
                except:
                    self.logger.logger.warn(
                        "Can not find the select album control button,may be it is not in multi Album interface***")
                else:
                    try:
                        SelectEnterElement.click()
                    except:
                        self.logger.logger.warn(
                            "Go to the select all album error***")
                    else:
                        try:
                            SelectAllElement = self.InitalDevice.driver.find_element_by_accessibility_id("Select All")
                        except:
                            self.logger.logger.warn(
                                "Can not find the select all control button,may be it is not in multi Album select interface***")
                        else:
                            try:
                                SelectAllElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Select all items error***")
                            else:
                                #delete all item in multi album
                                try:
                                    DeletElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn Delete Normal")
                                except:
                                    self.logger.logger.warn(
                                        "Can not find the delete control***")
                                else:
                                    try:
                                        DeletElement.click()
                                        sleep(1.5)
                                    except:
                                        self.logger.logger.warn(
                                            "Click the delete control error***")
                                    else:
                                        try:
                                            TouchAction(self.InitalDevice.driver).tap(x=242,y=338).perform()
                                        except:
                                            self.logger.logger.warn(
                                                "Delete all item in multi album error***")
                                        else:
                                            pass
    def SetCameraGrid(self,gridType = "None"):
        self.GoToCameraMainWindow()
        sleep(1.5)
        # if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                "Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    GridSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("Grid")
                except:
                    self.logger.logger.warn(
                        "Can not find camera Grid setting control***")
                else:
                    try:
                        GridSettingElement.click()
                    except:
                        self.logger.logger.warn(
                            "Enter camera Grid setting interface error***")
                    else:
                        try:
                            GridTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(gridType)
                        except:
                            self.logger.logger.warn(
                                "Can not find the camera %s Grid type ***"%gridType)
                        else:
                            try:
                                GridTypeElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Set the %s camera Grid error***"%gridType)

                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 200,
                                                                         "y": 187})
    def SetCameraCenterPoint(self,CenterPoint = "None"):
        self.GoToCameraMainWindow()
        sleep(1.5)
        # if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                "Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    CenterPointSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("Center Point")
                except:
                    self.logger.logger.warn(
                        "Can not find camera center point setting control***")
                else:
                    try:
                        CenterPointSettingElement.click()
                    except:
                        self.logger.logger.warn(
                            "Enter camera Center Point setting interface error***")
                    else:
                        try:
                            CenterPointTypeElement = self.InitalDevice.driver.find_element_by_accessibility_id(CenterPoint)
                        except:
                            self.logger.logger.warn(
                                "Can not find the camera %s Center Point type ***"%CenterPoint)
                        else:
                            try:
                                CenterPointTypeElement.click()
                            except:
                                self.logger.logger.warn(
                                    "Set the %s camera Center Point error***"%CenterPoint)

                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 200,
                                                                         "y": 187})
    def SwitchHistogram(self,Flag = "On"):
        self.GoToCameraMainWindow()
        sleep(1.5)
        # if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                "Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    HistogramElemet = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeSwitch[@name=\"Histogram\"]")
                    CurrentHistogramSwitchValue = HistogramElemet.text
                except:
                    self.logger.logger.warn(
                        "Can not find Histogram setting control***")
                else:
                    if Flag =="On":
                        if CurrentHistogramSwitchValue =="1":
                            return
                        else:
                            try:
                                HistogramElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Set Histogram error***")
                            else:
                                if CurrentHistogramSwitchValue != HistogramElemet.text:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 200,
                                                                             "y": 187})
                                else:
                                    self.logger.logger.warn(
                                        "Set Histogram error***")
                    elif Flag =="Off":
                        if CurrentHistogramSwitchValue =="0":
                            return
                        else:
                            try:
                                HistogramElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Set Histogram error***")
                            else:
                                if CurrentHistogramSwitchValue != HistogramElemet.text:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 200,
                                                                             "y": 187})
                                else:
                                    self.logger.logger.warn(
                                        "Set Histogram error***")
    def SwitchOverExposureWarning(self,Flag = "On"):
        self.GoToCameraMainWindow()
        sleep(1.5)
        # if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                "Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    OverExposureWarningElemet = self.InitalDevice.driver.find_element_by_xpath(
                        "//XCUIElementTypeSwitch[@name=\"Over Exposure Warning\"]")
                    CurrentOverExposureWarningSwitchValue = OverExposureWarningElemet.text
                except:
                    self.logger.logger.warn(
                        "Can not find OverExposureWarning setting control***")
                else:
                    if Flag =="On":
                        if CurrentOverExposureWarningSwitchValue =="1":
                            return
                        else:
                            try:
                                OverExposureWarningElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Set OverExposureWarning error***")
                            else:
                                if CurrentOverExposureWarningSwitchValue != OverExposureWarningElemet.text:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 200,
                                                                             "y": 187})
                                else:
                                    self.logger.logger.warn(
                                        "Set OverExposureWarning error***")
                    elif Flag =="Off":
                        if CurrentOverExposureWarningSwitchValue =="0":
                            return
                        else:
                            try:
                                OverExposureWarningElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Set OverExposureWarning error***")
                            else:
                                if CurrentOverExposureWarningSwitchValue != OverExposureWarningElemet.text:
                                    self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 200,
                                                                             "y": 187})
                                else:
                                    self.logger.logger.warn(
                                        "Set OverExposureWarning error***")
    def SetAntiFlicker(self,AntiflickerType="Auto"):
        self.GoToCameraMainWindow()
        sleep(1.5)
        # if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                "Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    AntiflickerElemet = self.InitalDevice.driver.find_element_by_accessibility_id("Anti-Flicker")
                except:
                    self.logger.logger.warn(
                        "Can not find Anti-flicker setting control***")
                else:
                    try:
                        AntiflickerElemet.click()
                    except:
                        self.logger.logger.warn(
                            "Enter Anti-flicker setting interface error***")
                    else:
                        try:
                            AntiflickerTypeElemet = self.InitalDevice.driver.find_element_by_accessibility_id(AntiflickerType)
                        except:
                            self.logger.logger.warn(
                                "Can not find the %s Anti-flicker setting item***"%AntiflickerType)
                        else:
                            try:
                                AntiflickerTypeElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Set the %s Anti-flicker setting error***"%AntiflickerType)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 200,
                                                                         "y": 187})
    def SetVideoEncodingFormat(self,VideoEncodingFormatType="H.264"):
        self.GoToCameraMainWindow()
        sleep(1.5)
        # if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                "Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    VideoEncodingFormatElemet = self.InitalDevice.driver.find_element_by_accessibility_id("Video Encoding Format")
                except:
                    self.logger.logger.warn(
                        "Can not find VideoEncodingFormat setting control***")
                else:
                    try:
                        VideoEncodingFormatElemet.click()
                    except:
                        self.logger.logger.warn(
                            "Enter VideoEncodingFormat setting interface error***")
                    else:
                        try:
                            VideoEncodingFormatTypeElemet = self.InitalDevice.driver.find_element_by_accessibility_id(VideoEncodingFormatType)
                        except:
                            self.logger.logger.warn(
                                "Can not find the %s Anti-flicker setting item***"%VideoEncodingFormatType)
                        else:
                            try:
                                VideoEncodingFormatElemet.click()
                            except:
                                self.logger.logger.warn(
                                    "Set the %s Anti-flicker setting error***"%VideoEncodingFormatType)
                            else:
                                self.InitalDevice.driver.execute_script("mobile: tap",
                                                                        {"x": 200,
                                                                         "y": 187})
    def ResetCamera(self):
        self.GoToCameraMainWindow()
        sleep(1.5)
        #if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    TouchAction(self.InitalDevice.driver).long_press(x=503,y=204,duration=100).move_to(x=503,
                                                                                           y=1).release().perform()
                    #sleep(0.5)
                except:
                    self.logger.logger.warn(
                        "Swipe the camera setting menu error***")
                else:
                    try:
                        ResetCameraElement = self.InitalDevice.driver.find_element_by_accessibility_id("Reset Camera")
                        ResetCameraElementLocation = ResetCameraElement.location
                        if ResetCameraElementLocation["x"] > 667 or ResetCameraElementLocation["x"] < 0:
                            self.logger.logger.warn(
                            "Format Element is not visiable***")
                            raise AttributeError
                    except:
                        self.logger.logger.warn(
                            "Can not find the reset camera control***")
                    else:
                        try:
                            ResetCameraElement.click()
                            sleep(1)
                        except:
                            self.logger.logger.warn(
                                "Enter reset camera interface error***")
                        else:
                            try:
                                ResetCameraDialogElement = self.InitalDevice.driver.find_element_by_accessibility_id("Are you sure you wish to reset Camera Settings?")
                            except:
                                self.logger.logger.warn(
                                    "Can not find Reset Camera dialog***")
                            else:
                                try:
                                    ResetCameraCheckOKElement =self.InitalDevice.driver.find_element_by_accessibility_id("OK")
                                except:
                                    self.logger.logger.warn(
                                        "Can not find Reset Camera OK control***")
                                else:
                                    try:
                                        ResetCameraCheckOKElement.click()
                                    except:
                                        self.logger.logger.warn(
                                            "Reset Camera error***")
                                    else:
                                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                                {"x": 200,
                                                                                 "y": 187})
                                        sleep(9)

    def CheckCameraModel(self,ModelType="XB015"):
        self.GoToCameraMainWindow()
        sleep(1.5)
        # if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                "Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    TouchAction(self.InitalDevice.driver).long_press(x=503,y=204,duration=100).move_to(x=503,
                                                                                           y=1).release().perform()
                    sleep(0.5)
                except:
                    self.logger.logger.warn(
                        "Swipe the camera setting menu error***")
                else:
                    try:
                        VideoEncodingFormatElemet = self.InitalDevice.driver.find_element_by_accessibility_id(ModelType)
                    except:
                        self.logger.logger.warn(
                            "The camera model error, current camera model is not %s***"%ModelType)
                    else:
                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 200,
                                                                             "y": 187})

    def CheckCameraVersion(self,CameraVersion="V0.2.0.8"):
        self.GoToCameraMainWindow()
        sleep(1.5)
        # if SD card is full,format SD card
        self.FormatSDCardWithPopSDFullDialog()
        try:
            CameraSettingElement = self.InitalDevice.driver.find_element_by_accessibility_id(
                "Btn console camera setting")
        except:
            self.logger.logger.warn(
                "Can not find camera setting control***")
        else:
            try:
                CameraSettingElement.click()
            except:
                self.logger.logger.warn(
                    "Enter camera setting menu error***")
            else:
                try:
                    TouchAction(self.InitalDevice.driver).long_press(x=503,y=204,duration=100).move_to(x=503,
                                                                                           y=1).release().perform()
                    sleep(0.5)
                except:
                    self.logger.logger.warn(
                        "Swipe the camera setting menu error***")
                else:
                    try:
                        VideoEncodingFormatElemet = self.InitalDevice.driver.find_element_by_accessibility_id(CameraVersion)
                    except:
                        self.logger.logger.warn(
                            "The camera version error,current version is not %s***"%CameraVersion)
                    else:
                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                            {"x": 200,
                                                                             "y": 187})
    def EnterFullScreen(self):
        self.GoToCameraMainWindow()
        sleep(1.5)
        try:
            #Swipe up FullScreenHideAllSettingBar
            TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(x=333,
                                                                                                 y=0).release().perform()
            sleep(0.1)
        except:
            self.logger.logger.warn(
                "Swipe up show full screen error***")
        else:

            try:
                isBacktoStartInterfaceElementVisible = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console back").is_displayed()
                isCameraSettingElementVisible = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console camera setting").is_displayed()
                isMapElementVisible = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console map shrink arrow").is_displayed()
            except:
                pass
            else:
                if isBacktoStartInterfaceElementVisible ==False and isCameraSettingElementVisible == False and \
                        isMapElementVisible == False:
                    pass
                else:
                    self.logger.logger.warn(
                        "Enter full screen error***")
    def ExitFullScreen(self):
        self.GoToCameraMainWindow()
        sleep(1.5)
        try:
            #Swipe up FullScreenHideAllSettingBar
            TouchAction(self.InitalDevice.driver).long_press(x=333, y=187, duration=100).move_to(x=333,
                                                                                                 y=300).release().perform()
            sleep(0.1)
        except:
            self.logger.logger.warn(
                "Swipe up show full screen error***")
        else:
            try:
                isBacktoStartInterfaceElementVisible = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console back").is_displayed()
                isCameraSettingElementVisible = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console camera setting").is_displayed()
                isMapElementVisible = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console map shrink arrow").is_displayed()
            except:
                pass
            else:
                if isBacktoStartInterfaceElementVisible and isCameraSettingElementVisible \
                        and isMapElementVisible:
                    pass
                else:
                    self.logger.logger.warn(
                        "Exit full screen error***")

    def SetPointAE(self,X=0,Y=0):
        self.EnterFullScreen()
        try:
            TouchAction(self.InitalDevice.driver).long_press(x=X, y=Y, duration=100).release().perform()
            sleep(0.1)
        except:
            self.logger.logger.warn(
                "Set Point AE error***")
        else:
            self.ExitFullScreen()

    def ControlGimbalMoveUp(self):
        self.GoToCameraMainWindow()
        sleep(1.5)
        try:
            #Swipe up FullScreenHideAllSettingBar
            TouchAction(self.InitalDevice.driver).long_press(x=333, y=187).move_to(x=333,
                                                                        y=187).wait(2000).move_to(x=333,
                                                                        y=137).wait(2000).release().perform()
            sleep(0.1)
        except:
            self.logger.logger.warn(
                "Control Gimbal Move Up error***")
        else:
            pass

    def ControlGimbalMoveDown(self):
        self.GoToCameraMainWindow()
        sleep(1.5)
        try:
            #Swipe up FullScreenHideAllSettingBar
            TouchAction(self.InitalDevice.driver).long_press(x=333, y=187).move_to(x=333,
                                                                        y=187).wait(2000).move_to(x=333,
                                                                        y=237).wait(2000).release().perform()
        except:
            self.logger.logger.warn(
                "Control Gimbal Move Down error***")
        else:
            pass

    def GetCurrentGimbalAngle(self):
        is0GimbalExist = self.InitalDevice.checkUIElementExist("0°")
        is1GimbalExist = self.InitalDevice.checkUIElementExist("1°")
        is2GimbalExist = self.InitalDevice.checkUIElementExist("2°")
        is3GimbalExist = self.InitalDevice.checkUIElementExist("3°")
        is4GimbalExist = self.InitalDevice.checkUIElementExist("4°")
        is5GimbalExist = self.InitalDevice.checkUIElementExist("5°")
        is6imbalExist = self.InitalDevice.checkUIElementExist("6°")
        is7GimbalExist = self.InitalDevice.checkUIElementExist("7°")
        is8GimbalExist = self.InitalDevice.checkUIElementExist("8°")
        is9GimbalExist = self.InitalDevice.checkUIElementExist("9°")
        is10GimbalExist = self.InitalDevice.checkUIElementExist("10°")
        is11GimbalExist = self.InitalDevice.checkUIElementExist("11°")
        is12GimbalExist = self.InitalDevice.checkUIElementExist("12°")
        is13GimbalExist = self.InitalDevice.checkUIElementExist("13°")
        is14GimbalExist = self.InitalDevice.checkUIElementExist("14°")
        is15GimbalExist = self.InitalDevice.checkUIElementExist("15°")
        is16GimbalExist = self.InitalDevice.checkUIElementExist("16°")
        is17GimbalExist = self.InitalDevice.checkUIElementExist("17°")
        is18GimbalExist = self.InitalDevice.checkUIElementExist("18°")
        is19GimbalExist = self.InitalDevice.checkUIElementExist("19°")
        is20GimbalExist = self.InitalDevice.checkUIElementExist("20°")
        is21GimbalExist = self.InitalDevice.checkUIElementExist("21°")
        is22GimbalExist = self.InitalDevice.checkUIElementExist("22°")
        is23GimbalExist = self.InitalDevice.checkUIElementExist("23°")
        is24GimbalExist = self.InitalDevice.checkUIElementExist("24°")
        is25GimbalExist = self.InitalDevice.checkUIElementExist("25°")
        is26GimbalExist = self.InitalDevice.checkUIElementExist("26°")
        is27GimbalExist = self.InitalDevice.checkUIElementExist("27°")
        is28GimbalExist = self.InitalDevice.checkUIElementExist("28°")
        is29GimbalExist = self.InitalDevice.checkUIElementExist("29°")
        is30GimbalExist = self.InitalDevice.checkUIElementExist("30°")
        is31GimbalExist = self.InitalDevice.checkUIElementExist("31°")
        is32GimbalExist = self.InitalDevice.checkUIElementExist("32°")
        is33GimbalExist = self.InitalDevice.checkUIElementExist("33°")
        is34GimbalExist = self.InitalDevice.checkUIElementExist("34°")
        is35GimbalExist = self.InitalDevice.checkUIElementExist("35°")
        is36GimbalExist = self.InitalDevice.checkUIElementExist("36°")
        is37GimbalExist = self.InitalDevice.checkUIElementExist("37°")
        is38GimbalExist = self.InitalDevice.checkUIElementExist("38°")
        is39GimbalExist = self.InitalDevice.checkUIElementExist("39°")
        is40GimbalExist = self.InitalDevice.checkUIElementExist("40°")
        is41GimbalExist = self.InitalDevice.checkUIElementExist("41°")
        is42GimbalExist = self.InitalDevice.checkUIElementExist("42°")
        is43GimbalExist = self.InitalDevice.checkUIElementExist("43°")
        is44GimbalExist = self.InitalDevice.checkUIElementExist("44°")
        is45GimbalExist = self.InitalDevice.checkUIElementExist("45°")
        is46GimbalExist = self.InitalDevice.checkUIElementExist("46°")
        is47GimbalExist = self.InitalDevice.checkUIElementExist("47°")
        is48GimbalExist = self.InitalDevice.checkUIElementExist("48°")
        is49GimbalExist = self.InitalDevice.checkUIElementExist("49°")
        is50GimbalExist = self.InitalDevice.checkUIElementExist("50°")
        is51GimbalExist = self.InitalDevice.checkUIElementExist("51°")
        is52GimbalExist = self.InitalDevice.checkUIElementExist("52°")
        is53GimbalExist = self.InitalDevice.checkUIElementExist("53°")
        is54GimbalExist = self.InitalDevice.checkUIElementExist("54°")
        is55GimbalExist = self.InitalDevice.checkUIElementExist("55°")
        is56GimbalExist = self.InitalDevice.checkUIElementExist("56°")
        is57GimbalExist = self.InitalDevice.checkUIElementExist("57°")
        is58GimbalExist = self.InitalDevice.checkUIElementExist("58°")
        is59GimbalExist = self.InitalDevice.checkUIElementExist("59°")
        is60GimbalExist = self.InitalDevice.checkUIElementExist("60°")
        is61GimbalExist = self.InitalDevice.checkUIElementExist("61°")
        is62GimbalExist = self.InitalDevice.checkUIElementExist("62°")
        is63GimbalExist = self.InitalDevice.checkUIElementExist("63°")
        is64GimbalExist = self.InitalDevice.checkUIElementExist("64°")
        is65GimbalExist = self.InitalDevice.checkUIElementExist("65°")
        is66GimbalExist = self.InitalDevice.checkUIElementExist("66°")
        is67GimbalExist = self.InitalDevice.checkUIElementExist("67°")
        is68GimbalExist = self.InitalDevice.checkUIElementExist("68°")
        is69GimbalExist = self.InitalDevice.checkUIElementExist("69°")
        is70GimbalExist = self.InitalDevice.checkUIElementExist("70°")
        is71GimbalExist = self.InitalDevice.checkUIElementExist("71°")
        is72GimbalExist = self.InitalDevice.checkUIElementExist("72°")
        is73GimbalExist = self.InitalDevice.checkUIElementExist("73°")
        is74GimbalExist = self.InitalDevice.checkUIElementExist("74°")
        is75GimbalExist = self.InitalDevice.checkUIElementExist("75°")
        is76GimbalExist = self.InitalDevice.checkUIElementExist("76°")
        is77GimbalExist = self.InitalDevice.checkUIElementExist("77°")
        is78GimbalExist = self.InitalDevice.checkUIElementExist("78°")
        is79GimbalExist = self.InitalDevice.checkUIElementExist("79°")
        is80GimbalExist = self.InitalDevice.checkUIElementExist("80°")
        is81GimbalExist = self.InitalDevice.checkUIElementExist("81°")
        is82GimbalExist = self.InitalDevice.checkUIElementExist("82°")
        is83GimbalExist = self.InitalDevice.checkUIElementExist("83°")
        is84GimbalExist = self.InitalDevice.checkUIElementExist("84°")
        is85GimbalExist = self.InitalDevice.checkUIElementExist("85°")
        is86GimbalExist = self.InitalDevice.checkUIElementExist("86°")
        is87GimbalExist = self.InitalDevice.checkUIElementExist("87°")
        is88GimbalExist = self.InitalDevice.checkUIElementExist("88°")
        is89GimbalExist = self.InitalDevice.checkUIElementExist("89°")
        is90GimbalExist = self.InitalDevice.checkUIElementExist("90°")
        if is0GimbalExist:
            return "0°"
        if is1GimbalExist:
            return "1°"
        if is2GimbalExist:
            return "2°"
        if is3GimbalExist:
            return "3°"
        if is4GimbalExist:
            return "4°"
        if is5GimbalExist:
            return "5°"
        if is6imbalExist:
            return "6°"
        if is7GimbalExist:
            return "7°"
        if is8GimbalExist:
            return "8°"
        if is9GimbalExist:
            return "9°"
        if is10GimbalExist:
            return "10°"
        if is11GimbalExist:
            return "11°"
        if is12GimbalExist:
            return "12°"
        if is13GimbalExist:
            return "13°"
        if is14GimbalExist:
            return "14°"
        if is15GimbalExist:
            return "15°"
        if is16GimbalExist:
            return "16°"
        if is17GimbalExist:
            return "17°"
        if is18GimbalExist:
            return "18°"
        if is19GimbalExist:
            return "19°"
        if is20GimbalExist:
            return "20°"
        if is21GimbalExist:
            return "21°"
        if is22GimbalExist:
            return "22°"
        if is23GimbalExist:
            return "23°"
        if is24GimbalExist:
            return "24°"
        if is25GimbalExist:
            return "25°"
        if is26GimbalExist:
            return "26°"
        if is27GimbalExist:
            return "27°"
        if is28GimbalExist:
            return "28°"
        if is29GimbalExist:
            return "29°"
        if is30GimbalExist:
            return "30°"
        if is31GimbalExist:
            return "31°"
        if is32GimbalExist:
            return "32°"
        if is33GimbalExist:
            return "33°"
        if is34GimbalExist:
            return "34°"
        if is35GimbalExist:
            return "35°"
        if is36GimbalExist:
            return "36°"
        if is37GimbalExist:
            return "37°"
        if is38GimbalExist:
            return "38°"
        if is39GimbalExist:
            return "39°"
        if is40GimbalExist:
            return "40°"
        if is41GimbalExist:
            return "41°"
        if is42GimbalExist:
            return "42°"
        if is43GimbalExist:
            return "43°"
        if is44GimbalExist:
            return "44°"
        if is45GimbalExist:
            return "45°"
        if is46GimbalExist:
            return "46°"
        if is47GimbalExist:
            return "47°"
        if is48GimbalExist:
            return "48°"
        if is49GimbalExist:
            return "49°"
        if is50GimbalExist:
            return "50°"
        if is51GimbalExist:
            return "51°"
        if is52GimbalExist:
            return "52°"
        if is53GimbalExist:
            return "53°"
        if is54GimbalExist:
            return "54°"
        if is55GimbalExist:
            return "55°"
        if is56GimbalExist:
            return "56°"
        if is57GimbalExist:
            return "57°"
        if is58GimbalExist:
            return "58°"
        if is59GimbalExist:
            return "59°"
        if is60GimbalExist:
            return "60°"
        if is61GimbalExist:
            return "61°"
        if is62GimbalExist:
            return "62°"
        if is63GimbalExist:
            return "63°"
        if is64GimbalExist:
            return "64°"
        if is65GimbalExist:
            return "65°"
        if is66GimbalExist:
            return "66°"
        if is67GimbalExist:
            return "67°"
        if is68GimbalExist:
            return "68°"
        if is69GimbalExist:
            return "69°"
        if is70GimbalExist:
            return "70°"
        if is71GimbalExist:
            return "71°"
        if is72GimbalExist:
            return "72°"
        if is73GimbalExist:
            return "73°"
        if is74GimbalExist:
            return "74°"
        if is75GimbalExist:
            return "75°"
        if is76GimbalExist:
            return "76°"
        if is77GimbalExist:
            return "77°"
        if is78GimbalExist:
            return "78°"
        if is79GimbalExist:
            return "79°"
        if is80GimbalExist:
            return "80°"
        if is81GimbalExist:
            return "81°"
        if is82GimbalExist:
            return "82°"
        if is83GimbalExist:
            return "83°"
        if is84GimbalExist:
            return "84°"
        if is85GimbalExist:
            return "85°"
        if is86GimbalExist:
            return "86°"
        if is87GimbalExist:
            return "87°"
        if is88GimbalExist:
            return "88°"
        if is89GimbalExist:
            return "89°"
        if is90GimbalExist:
            return "90°"


    def SetGimbalAngle(self,Angel="0°"):
        self.GoToCameraMainWindow()
        sleep(1.5)
        CurrentGimbalAngle = self.GetCurrentGimbalAngle()
        try:
            CurrentGimbalAngleElement = self.InitalDevice.driver.find_element_by_accessibility_id(CurrentGimbalAngle)
        except:
            self.logger.logger.warn(
                "Set Gimbal Angle Element error***")
        else:
            try:
                CurrentGimbalAngleElement.click()
            except:
                self.logger.logger.warn(
                    "Enter Gimbal Angle interface error***")
            else:
                try:
                    GimbalAngleElement = self.InitalDevice.driver.find_element_by_accessibility_id(Angel)
                except:
                    self.logger.logger.warn(
                        "Can not Gimbal Angle Item***")
                else:
                    try:
                       GimbalAngleElement.click()
                    except:
                        self.logger.logger.warn(
                            "Set Gimbal Angle %s***"%Angel)
                    else:
                        self.InitalDevice.driver.execute_script("mobile: tap",
                                                                {"x": 200,
                                                                 "y": 187})




#el1 = driver.find_element_by_accessibility_id("Album")
#el2 = driver.find_element_by_accessibility_id("Select")
#el3 = driver.find_element_by_accessibility_id("Select All")
#el4 = driver.find_element_by_accessibility_id("Btn Download Normal")
#el5 = driver.find_element_by_accessibility_id("Cancel")
#el6 = driver.find_element_by_accessibility_id("OK")
#el7 = driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"Cancel\"])[2]")






def main():
    test = CameraTest()
    sleep(0.5)
    #test.GoToCameraMainWindow()
    #sleep(0.5)
    #test.setShutterInCaptureMode("1/60")
    # test.setShutterInCaptureMode("8.0")
    #test.setISOInCaptureMode("800")
    # test.SetCaptureTypeMode("SINGLE SHOT")
    # test.SetPhotoFormat("RAW+JPG")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetPhotoFormat("RAW")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetPhotoFormat("JPG")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetCaptureTypeMode("SINGLE SHOT")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetCaptureTypeMode("TIMELAPSE","60S")
    # test.doCaptureInCaptureMode()
    # sleep(10)
    # test.StopTimelapseCaptureInCaptureMode()
    # # test.SetCaptureTypeMode("BURST", "3")
    # # test.doCaptureInCaptureMode()
    # # sleep(5)
    # # test.SetCaptureTypeMode("AEB", "5")
    # # test.doCaptureInCaptureMode()
    # # sleep(10)
    # test.SetCaptureTypeMode("TIMELAPSE", "2S")
    # test.doCaptureInCaptureMode()
    # sleep(10)
    # test.StopTimelapseCaptureInCaptureMode()
    # #test.SetCaptureTypeMode("BURST", "14")
    # #test.doCaptureInCaptureMode()
    # #sleep(60)
    # test.SetCaptureTypeMode("AEB", "3")
    # test.doCaptureInCaptureMode()
    # sleep(10)
    # test.SetCaptureTypeMode("SINGLE SHOT")
    # test.SetPictureSize("4000X3000")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetPictureSize("4000X2250")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.setShutterInCaptureMode("1/12.5")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("± 0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("-3.0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("+3.0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("-2.7")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("+2.7")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("-2.3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("+2.3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("-2.0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("+2.0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("-1.7")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("+1.7")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("-1.3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("+1.3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("-1.0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("+1.0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("-0.7")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("+0.7")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("-0.3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("+0.3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInCaptureMode("± 0")
    # test.SetWhiteBalanceInCaptureMode(WB=" AUTO")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetWhiteBalanceInCaptureMode(WB=" SUNNY")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetWhiteBalanceInCaptureMode(WB=" CLOUDY")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetWhiteBalanceInCaptureMode(WB=" INCAN")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetWhiteBalanceInCaptureMode(WB=" NEON")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetWhiteBalanceInCaptureMode("Custom"," 2000K")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetWhiteBalanceInCaptureMode("Custom", " 6000K")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetWhiteBalanceInCaptureMode("Custom", " 9900K")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetWhiteBalanceInCaptureMode(WB=" AUTO")
    # test.SetColorInCaptureMode("NONE")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("NOSTALGIC")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("LOG")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("CLASSIC")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("VIVID")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("DREAM")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("B&W")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("BEACH")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("ART")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("FILM")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetColorInCaptureMode("NONE")
    # test.SetStyleInCaptureMode(Style="STD")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="LAND")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="NEUT")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom",Sharpness="+3",Contrast="±0",Saturation="±0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="±0", Contrast="+3", Saturation="±0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="±0", Contrast="±0", Saturation="+3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="-3", Contrast="±0", Saturation="±0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="±0", Contrast="-3", Saturation="±0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="±0", Contrast="±0", Saturation="-3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="+1", Contrast="±0", Saturation="±0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="±0", Contrast="+1", Saturation="±0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="±0", Contrast="±0", Saturation="+1")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="+3", Contrast="+3", Saturation="+3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="-3", Contrast="-3", Saturation="-3")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="Custom", Sharpness="±0", Contrast="±0", Saturation="±0")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetStyleInCaptureMode(Style="STD")
    # test.SetDigitalZoomInCaptureMode("1.0×")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetDigitalZoomInCaptureMode("8.0×")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetDigitalZoomInCaptureMode("2.0×")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetDigitalZoomInCaptureMode("7.0×")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetDigitalZoomInCaptureMode("3.0×")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetDigitalZoomInCaptureMode("6.0×")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetDigitalZoomInCaptureMode("4.0×")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetDigitalZoomInCaptureMode("5.0×")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetDigitalZoomInCaptureMode("1.0×")
    # #test.setManualExposureModeInRecordMode()
    # #test.setAutoExposureModeInRecordMode()
    # test.setShutterInRecordMode("1/200")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.setShutterInRecordMode("1/60")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.setISOInRecordMode("100")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.setISOInRecordMode("3200")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.setISOInRecordMode("200")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.setISOInRecordMode("1600")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.setISOInRecordMode("400")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.setISOInRecordMode("800")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.setISOInRecordMode("100")
    # test.setISOInCaptureMode("100")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.setISOInCaptureMode("3200")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.setISOInCaptureMode("200")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.setISOInCaptureMode("1600")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.setISOInCaptureMode("400")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.setISOInCaptureMode("800")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.setISOInCaptureMode("100")
    # test.doCaptureInCaptureMode()
    # sleep(5)
    # test.SetEVInRecordMode("± 0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("-3.0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("+3.0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("-2.7")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("+2.7")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("-2.3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("+2.3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("-2.0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("+2.0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("-1.7")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("+1.7")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("-1.3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("+1.3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("-1.0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("+1.0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("-0.7")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("+0.7")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("-0.3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("+0.3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetEVInRecordMode("± 0")
    # test.SetWhiteBalanceInRecordMode(WB=" AUTO")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetWhiteBalanceInRecordMode(WB=" SUNNY")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetWhiteBalanceInRecordMode(WB=" CLOUDY")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetWhiteBalanceInRecordMode(WB=" INCAN")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetWhiteBalanceInRecordMode(WB=" NEON")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetWhiteBalanceInRecordMode("Custom"," 2000K")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetWhiteBalanceInRecordMode("Custom", " 6000K")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetWhiteBalanceInRecordMode("Custom", " 9900K")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetWhiteBalanceInRecordMode(WB=" AUTO")
    # test.SetColorInRecordMode("NONE")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("NOSTALGIC")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("LOG")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("CLASSIC")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("VIVID")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("DREAM")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("B&W")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("BEACH")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("ART")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("FILM")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetColorInRecordMode("NONE")
    # test.SetStyleInRecordMode(Style="STD")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="LAND")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="NEUT")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom",Sharpness="+3",Contrast="±0",Saturation="±0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="±0", Contrast="+3", Saturation="±0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="±0", Contrast="±0", Saturation="+3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="-3", Contrast="±0", Saturation="±0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="±0", Contrast="-3", Saturation="±0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="±0", Contrast="±0", Saturation="-3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="+1", Contrast="±0", Saturation="±0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="±0", Contrast="+1", Saturation="±0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="±0", Contrast="±0", Saturation="+1")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="+3", Contrast="+3", Saturation="+3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="-3", Contrast="-3", Saturation="-3")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="Custom", Sharpness="±0", Contrast="±0", Saturation="±0")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetStyleInRecordMode(Style="STD")
    # test.SetDigitalZoomInRecordMode("1.0×")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetDigitalZoomInRecordMode("8.0×")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetDigitalZoomInRecordMode("2.0×")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetDigitalZoomInRecordMode("7.0×")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetDigitalZoomInRecordMode("3.0×")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetDigitalZoomInRecordMode("6.0×")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetDigitalZoomInRecordMode("4.0×")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetDigitalZoomInRecordMode("5.0×")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # # test.SetPIVInRecordMode("MANUAL")
    # # test.SetPIVInRecordMode("60S")
    # # test.SetPIVInRecordMode("5S")
    # # test.SetPIVInRecordMode("30S")
    # # test.SetPIVInRecordMode("10S")
    # #
    # # test.SetvideoStandardInRecordMode("NTSC")
    # # test.SetvideoStandardInRecordMode("PAL")
    # # test.SetVideoFormatInRecordMode("MOV")
    # # test.SetVideoFormatInRecordMode("MP4")
    # # test.SetVideoResolutionInRecordMode("4K+(4096X2160)")
    # # test.SetVideoResolutionInRecordMode("720P(1280X720)")
    # # test.SetVideoResolutionInRecordMode("4K(3840X2160)")
    # # test.SetVideoResolutionInRecordMode("1080P(1920X1080)")
    # # test.SetVideoResolutionInRecordMode("2.7K(2720X1530)")
    # ##frame rate relates to standard and resolution
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("4K+(4096X2160)")
    # test.SetVideoFrameRateInRecordMode("30 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("720P(1280X720)")
    # test.SetVideoFrameRateInRecordMode("240 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("4K(3840X2160)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("1080P(1920X1080)")
    # test.SetVideoFrameRateInRecordMode("120 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("4K+(4096X2160)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("2.7K(2720X1530)")
    # test.SetVideoFrameRateInRecordMode("60 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("4K+(4096X2160)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("720P(1280X720)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("4K(3840X2160)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("1080P(1920X1080)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("2.7K(2720X1530)")
    # test.SetVideoFrameRateInRecordMode("60 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("720P(1280X720)")
    # test.SetVideoFrameRateInRecordMode("60 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("4K(3840X2160)")
    # test.SetVideoFrameRateInRecordMode("60 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("1080P(1920X1080)")
    # test.SetVideoFrameRateInRecordMode("60 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("NTSC")
    # test.SetVideoResolutionInRecordMode("2.7K(2720X1530)")
    # test.SetVideoFrameRateInRecordMode("60 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("4K+(4096X2160)")
    # test.SetVideoFrameRateInRecordMode("25 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("4K(3840X2160)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("4K+(4096X2160)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("2.7K(2720X1530)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("1080P(1920X1080)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("720P(1280X720)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("4K(3840X2160)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("1080P(1920X1080)")
    # test.SetVideoFrameRateInRecordMode("24 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("2.7K(2720X1530)")
    # test.SetVideoFrameRateInRecordMode("50 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("720P(1280X720)")
    # test.SetVideoFrameRateInRecordMode("50 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("4K(3840X2160)")
    # test.SetVideoFrameRateInRecordMode("50 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("1080P(1920X1080)")
    # test.SetVideoFrameRateInRecordMode("50 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.SetvideoStandardInRecordMode("PAL")
    # test.SetVideoResolutionInRecordMode("2.7K(2720X1530)")
    # test.SetVideoFrameRateInRecordMode("50 FPS")
    # test.startRecord()
    # sleep(15)
    # test.stopRecord()
    # test.GotoAlbumInCaptureMode()
    # test.GotoAlbumInRecordMode()
    # test.SwipeLeftInAlbum(15)
    # test.SwipeRightInAlbum(15)
    # test.EXitAlbum()
    # test.DownAllItemsInAlbum()
    # # test.FormatSDcardWithCameraSetting()
    # test.GotoAlbumInRecordMode()
    # test.DeleteCurrentItemInSingleAlbum()
    # test.DeleteAllItemInMultiAlbum()
    # test.SwitchRecordSubtitle("On")
    # test.SwitchRecordSubtitle("Off")
    # test.SetCameraGrid("Grid Lines")
    # test.SetCameraGrid("Grid Diagonals")
    # test.SetCameraGrid("None")
    # test.SetCameraCenterPoint("Circle")
    # test.SetCameraCenterPoint("Cross")
    # test.SetCameraCenterPoint("Square(Without Center Point)")
    # test.SetCameraCenterPoint("Square(With Center Point)")
    # test.SetCameraCenterPoint("Circle Cross")
    # test.SetCameraCenterPoint("None")
    # test.SwitchHistogram("On")
    # test.SwitchHistogram("Off")
    # test.SwitchOverExposureWarning("On")
    # test.SwitchOverExposureWarning("Off")
    # test.SetAntiFlicker("Auto")
    # test.SetAntiFlicker("50Hz")
    # test.SetAntiFlicker("60Hz")
    # test.SetVideoEncodingFormat("H.265")
    # test.SetVideoEncodingFormat("H.264")
    #test.ResetCamera()
    # test.CheckCameraModel("XB015")
    # test.CheckCameraVersion("V0.2.0.8")
    # test.CheckCameraModel("XB016")
    # test.CheckCameraVersion("V0.2.0.9")
    # test.EnterFullScreen()
    # test.ExitFullScreen()
    # test.SetPointAE(333,187)
    # test.SetPointAE(100, 187)
    # test.SetPointAE(500, 187)
    # test.SetPointAE(333, 50)
    # test.SetPointAE(333, 200)
    # test.SetPointAE(333, 300)
    # test.SetPointAE(333, 187)
    # test.ControlGimbalMoveDown()
    # test.ControlGimbalMoveUp()
    # test.SetGimbalAngle("0°")
    # test.SetGimbalAngle("30°")
    # test.SetGimbalAngle("45°")
    # test.SetGimbalAngle("50°")
    # test.SetGimbalAngle("60°")
    # test.SetGimbalAngle("90°")
    # test.GotoMultiAlbumInRecordMode()
    #     # test.SelectNLNCItem(1,1)
    #     # sleep(0.5)
    #     # test.SelectNLNCItem(1, 2)
    #     # sleep(0.5)
    #     # test.SelectNLNCItem(1, 3)
    #     # sleep(0.5)
    #     # test.SelectNLNCItem(1, 4)
    #     # sleep(0.5)
    #     # test.SelectNLNCItem(1, 5)
    #     # sleep(0.5)
    #     # test.SelectNLNCItem(2, 1)
    #     # sleep(0.5)
    #     # test.SelectNLNCItem(2, 2)
    #     # sleep(0.5)
    #     # test.SelectNLNCItem(2, 3)
    #     # sleep(0.5)
    #     # test.GotoMultiAlbumInSigleAlbum()
    #     # test.SelectNLNCItem(2, 5)
    #     # sleep(0.5)
    #     # test.GotoMultiAlbumInSigleAlbum()
    test.GotoAlbumInRecordMode()
    test.ZoomThePhotoPreview()


    #test.InitalDevice.closeApp()



if __name__ == '__main__':
    main()


# #start record
# el13 = driver.find_element_by_accessibility_id("Btn console video normal")
# el13.click()
# #stop record
# el14 = driver.find_element_by_accessibility_id("Btn console video recording")
# el14.click()
#
# #switch to capture mode
# el15 = driver.find_element_by_accessibility_id("Btn console switch video norma")
# el15.click()
#
# #witch to record mode
# el16 = driver.find_element_by_accessibility_id("Btn console switch photo norma")
# el16.click()
#
# #start capture
# el18 = driver.find_element_by_accessibility_id("Btn console photo normal")
# el18.click()
# #gotocaptureModeSettings
#el23 = driver.find_element_by_accessibility_id("拍照模式")
#el23 = driver.find_element_by_accessibility_id("MODE")
# el23.click()
# #select single
# el25 = driver.find_element_by_accessibility_id(u" 单拍")
#el25 = driver.find_element_by_accessibility_id("SINGLE SHOT")
# el25.click()
# #select burst
# el26 = driver.find_element_by_accessibility_id(" 连拍 ")
#el26 = driver.find_element_by_accessibility_id("BURST")
# el26.click()
# #goto burst setting
# el26 = driver.find_element_by_accessibility_id(u" 连拍 ")
# el26.click()
# #select burst 3
# el28 = driver.find_element_by_accessibility_id(" 3")
# el28.click()
# #select burst 5
# el28 = driver.find_element_by_accessibility_id(" 5")
# el28.click()
# #select burst 7
# el28 = driver.find_element_by_accessibility_id(" 7")
# el28.click()
# #select burst 10
# el28 = driver.find_element_by_accessibility_id(" 10")
# el28.click()
# #select burst 14
# el28 = driver.find_element_by_accessibility_id(" 14")
# el28.click()

#select bottom setting tool bar
#el4 = driver.find_element_by_accessibility_id("Img_console_bottom_bar_bg")
#el4.click()

#select video 120 fps
#el6 = driver.find_element_by_accessibility_id("120 FPS")
#el6.click()
#select video 60 fps
#el6 = driver.find_element_by_accessibility_id("60 FPS")
#el6.click()
#select video 48 fps
#el6 = driver.find_element_by_accessibility_id("48 FPS")
#el6.click()
#select video 30 fps
#el6 = driver.find_element_by_accessibility_id("30 FPS")
#el6.click()
#select video 24 fps
#el6 = driver.find_element_by_accessibility_id("24 FPS")
#el6.click()
##select piv setting
            #el5 = driver.find_element_by_accessibility_id("PIV")
            #el5.click()
            ##select piv mannaul
            #el1 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"手动\"])[1]")
            #el1.click()
            ##select piv 5s
            #el5 = driver.find_element_by_accessibility_id("5S")
            #el5.click()
            ##select piv 10s
            # el5 = driver.find_element_by_accessibility_id("10S")
            # el5.click()
            ##select piv 30s
            # el5 = driver.find_element_by_accessibility_id("30S")
            # el5.click()
            ##select piv 60s
            # el5 = driver.find_element_by_accessibility_id("60S")
            # el5.click()
            ##swipe piv setting bar
            #el4 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")

            ##select set video standard setting
            #el6 = driver.find_element_by_accessibility_id("视频制式")
            #el6.click()
            ##set NTSC
            #el2 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"NTSC\"])[1]")
            #el2.click()
            #el4 = driver.find_element_by_accessibility_id("NTSC")
            #el4.click()
            ##set PAL
            #el3 = driver.find_element_by_accessibility_id("PAL")
            #el3.click()





            ##select video format setting
            #el7 = driver.find_element_by_accessibility_id("视频格式")
            #el7.click()
            ##set MOV
            #el5 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"MOV\"])[1]")
            #el5.click()
            ##SET MP4
            #el6 = driver.find_element_by_accessibility_id("MP4")
            #el6.click()
            #el5 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"MP4\"])[1]")
            #el5.click()



            ##select video resolution setting
            #el8 = driver.find_element_by_accessibility_id("视频分辨率")
            #el8.click()
            ##set 4K+
            #el7 = driver.find_element_by_accessibility_id("4K+(4096X2160)")
            #el7.click()
            ## set 4k
            #el8 = driver.find_element_by_accessibility_id("4K(3840X2160)")
            #el8.click()
            ##set 2.7k
            #el9 = driver.find_element_by_accessibility_id("2.7K(2720X1530)")
            #el9.click()
            ##set 1080P
            #el10 = driver.find_element_by_accessibility_id("1080P(1920X1080)")
            #el10.click()
            ##set 720
            #el11 = driver.find_element_by_accessibility_id("720P(1280X720)")
            #el11.click()

            ##select video fps setting
            #el9 = driver.find_element_by_accessibility_id("视频帧率")
            #el9.click()
            ##set 30fps
            #el12 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"30 FPS\"])[1]")
            #el12.click()
            # el13 = driver.find_element_by_accessibility_id("30 FPS")
            # el13.click()
            ##set 24 fps
            #el13 = driver.find_element_by_accessibility_id("24 FPS")
            #el13.click()
            # el12 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"24 FPS\"])[1]")
            # el12.click()
            ##set 60 fps
            #el15 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"60 FPS\"])[1]")
            #el15.click()
            ##set 48 fps
            #el16 = driver.find_element_by_accessibility_id("48 FPS")
            #el16.click()
            ##set 120 fps
            #el17 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"120 FPS\"])[1]")
            #el17.click()
            ##set 240 fps
            #el18 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"240 FPS\"])[1]")
            #el18.click()
            ##set 25 fps
            #el19 = driver.find_element_by_accessibility_id("25 FPS")
            #el19.click()
            ##set 50 fps
            #el20 = driver.find_element_by_accessibility_id("50 FPS")
            #el20.click()





            ##select ISO setting
            #el2 = driver.find_element_by_accessibility_id("感光度")
            #driver.find_element_by_accessibility_id("ISO")
            #el2.click()
            ##el2 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
            ##set ISO 100
            #el21 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"100\"])[1]")
            #el21.click()
            ##set ISO 200
            #el22 = driver.find_element_by_accessibility_id("200")
            #el22.click()
            ##set ISO 400
            #el23 = driver.find_element_by_accessibility_id("400")
            #el23.click()
            ##set ISO 800
            #el24 = driver.find_element_by_accessibility_id("800")
            #el24.click()
            ##set ISO 1600
            #el25 = driver.find_element_by_accessibility_id("1600")
            #el25.click()
            ##SET iso 3200
            #el26 = driver.find_element_by_accessibility_id("3200")
            #el26.click()



            ##select shutter setting
            #el3 = driver.find_element_by_accessibility_id("快门速度")
            #el6 = driver.find_element_by_accessibility_id("SHUTTER")
            #el3.click()
            ##set shutter 1/8000
            #el27 = driver.find_element_by_accessibility_id("1/8000")
            #el27.click()
            ##set shutter 1/6000
            # el27 = driver.find_element_by_accessibility_id("1/6000")
            # el27.click()
            ##set shutter 1/5000
            # el27 = driver.find_element_by_accessibility_id("1/5000")
            # el27.click()
            ##set shutter 1/4000
            # el27 = driver.find_element_by_accessibility_id("1/4000")
            # el27.click()
            ##set shutter 1/3200
            # el27 = driver.find_element_by_accessibility_id("1/3200")
            # el27.click()
            ##set shutter 1/2500
            # el27 = driver.find_element_by_accessibility_id("1/2500")
            # el27.click()
            ##set shutter 1/2000
            # el27 = driver.find_element_by_accessibility_id("1/2000")
            # el27.click()
            ##set shutter 1/1600
            # el27 = driver.find_element_by_accessibility_id("1/1600")
            # el27.click()
            ##set shutter 1/1250
            # el27 = driver.find_element_by_accessibility_id("1/1250")
            # el27.click()
            ##set shutter 1/1000
            # el27 = driver.find_element_by_accessibility_id("1/1000")
            # el27.click()
            ##set shutter 1/800
            # el27 = driver.find_element_by_accessibility_id("1/800")
            # el27.click()
            ##set shutter 1/640
            # el27 = driver.find_element_by_accessibility_id("1/640")
            # el27.click()
            ##set shutter 1/500
            # el27 = driver.find_element_by_accessibility_id("1/500")
            # el27.click()
            ##set shutter 1/400
            # el27 = driver.find_element_by_accessibility_id("1/400")
            # el27.click()
            ##set shutter 1/320
            # el27 = driver.find_element_by_accessibility_id("1/320")
            # el27.click()
            ##set shutter 1/240
            # el27 = driver.find_element_by_accessibility_id("1/240")
            # el27.click()
            ##set shutter 1/200
            # el27 = driver.find_element_by_accessibility_id("1/200")
            # el27.click()
            ##set shutter 1/160
            # el27 = driver.find_element_by_accessibility_id("1/160")
            # el27.click()
            ##set shutter 1/120
            # el27 = driver.find_element_by_accessibility_id("1/120")
            # el27.click()
            ##set shutter 1/100
            # el27 = driver.find_element_by_accessibility_id("1/100")
            # el27.click()
            ##set shutter 1/80
            # el27 = driver.find_element_by_accessibility_id("1/80")
            # el27.click()
            ##set shutter 1/60
            # el27 = driver.find_element_by_accessibility_id("1/60")
            # el27.click()
            ##set shutter 1/50
            # el27 = driver.find_element_by_accessibility_id("1/50")
            # el27.click()
            ##set shutter 1/40
            # el27 = driver.find_element_by_accessibility_id("1/40")
            # el27.click()
            ##set shutter 1/30
            # el27 = driver.find_element_by_accessibility_id("1/30")
            # el27.click()
            ##set shutter 1/25
            # el27 = driver.find_element_by_accessibility_id("1/25")
            # el27.click()
            ##set shutter 1/20
            # el27 = driver.find_element_by_accessibility_id("1/20")
            # el27.click()
            ##set shutter 1/15
            # el27 = driver.find_element_by_accessibility_id("1/15")
            # el27.click()
            ##set shutter 1/12.5
            # el27 = driver.find_element_by_accessibility_id("1/12.5")
            # el27.click()
            ##set shutter 1/10
            # el27 = driver.find_element_by_accessibility_id("1/10")
            # el27.click()
            ##set shutter 1/8
            # el27 = driver.find_element_by_accessibility_id("1/8")
            # el27.click()
            ##set shutter 1/6.25
            # el27 = driver.find_element_by_accessibility_id("1/6.25")
            # el27.click()
            ##set shutter 1/5
            # el27 = driver.find_element_by_accessibility_id("1/5")
            # el27.click()
            ##set shutter 1/4
            # el27 = driver.find_element_by_accessibility_id("1/4")
            # el27.click()
            ##set shutter 1/3
            # el27 = driver.find_element_by_accessibility_id("1/3")
            # el27.click()
            ##set shutter 1/2.5
            # el27 = driver.find_element_by_accessibility_id("1/2.5")
            # el27.click()
            ##set shutter 1/2
            # el27 = driver.find_element_by_accessibility_id("1/2")
            # el27.click()
            ##set shutter 1/1.67
            # el27 = driver.find_element_by_accessibility_id("1/1.67")
            # el27.click()
            ##set shutter 1/1.25
            # el27 = driver.find_element_by_accessibility_id("1/1.25")
            # el27.click()
            ##set shutter 1s
            #el27 = self.InitalDevice.driver.find_element_by_accessibility_id("1\"")
            #el27.click()
            # ##set shutter 1.3s
            # el27 = self.InitalDevice.driver.find_element_by_accessibility_id("1.3\"")
            # el27.click()
# ##set shutter 1.6s
# el27 = self.InitalDevice.driver.find_element_by_accessibility_id("1.6\"")
# el27.click()
# ##set shutter 2.0s
# el27 = self.InitalDevice.driver.find_element_by_accessibility_id("2.0\"")
# el27.click()
# ##set shutter 2.5s
# el27 = self.InitalDevice.driver.find_element_by_accessibility_id("2.5\"")
# el27.click()
# ##set shutter 3.0s
# el27 = self.InitalDevice.driver.find_element_by_accessibility_id("3.0\"")
# el27.click()
# ##set shutter 3.2s
# el27 = self.InitalDevice.driver.find_element_by_accessibility_id("3.2\"")
# el27.click()
# ##set shutter 4.0s
# el27 = self.InitalDevice.driver.find_element_by_accessibility_id("4.0\"")
# el27.click()
# ##set shutter 5.0s
# el27 = self.InitalDevice.driver.find_element_by_accessibility_id("5.0\"")
# el27.click()
# ##set shutter 6.0s
# el27 = self.InitalDevice.driver.find_element_by_accessibility_id("6.0\"")
# el27.click()
# ##set shutter 8.0s
# el27 = self.InitalDevice.driver.find_element_by_accessibility_id("8.0\"")
# el27.click()





##select explosure mode(will change)
#el2 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"手动\"])[2]")
#el4 = driver.find_element_by_accessibility_id("MANUAL")
#el2.click()
#el3 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"自动\"])[3]")
#el5 = driver.find_element_by_accessibility_id("AUTO")
#el3.click()
##set mannual explosure mode
#el4 = driver.find_element_by_accessibility_id("手动")
#el4 = driver.find_element_by_accessibility_id("MANUAL")
#el4.click()
##set auto explosure mode
#el5 = driver.find_element_by_accessibility_id("自动")
#el3 = driver.find_element_by_accessibility_id("AUTO")
#el5.click()

##select explosure compensation setting
#el4 = driver.find_element_by_accessibility_id("曝光补偿")
#el1 = driver.find_element_by_accessibility_id("EV")

#el4.click()

##EV Setting bar
# #el1 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
# ##set Explosure compensation -3.0
#el7 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"-3.0\"])[1]")
#el7.click()
#el8 = driver.find_element_by_accessibility_id("-3.0")
#el8.click()
##set Explosure compensation -2.7
#el8 = driver.find_element_by_accessibility_id("-2.7")
#el8.click()
##set Explosure compensation -2.3
#el8 = driver.find_element_by_accessibility_id("-2.3")
#el8.click()
##set Explosure compensation -2.0
#el8 = driver.find_element_by_accessibility_id("-2.0")
#el8.click()
##set Explosure compensation -1.7
#el8 = driver.find_element_by_accessibility_id("-1.7")
#el8.click()
##set Explosure compensation -1.3
#el8 = driver.find_element_by_accessibility_id("-1.3")
#el8.click()
##set Explosure compensation -1.0
#el8 = driver.find_element_by_accessibility_id("-1.0")
#el8.click()
##set Explosure compensation -0.7
#el8 = driver.find_element_by_accessibility_id("-0.7")
#el8.click()
##set Explosure compensation -0.3
#el8 = driver.find_element_by_accessibility_id("-0.3")
#el8.click()
##set Explosure compensation -2.3
#el8 = driver.find_element_by_accessibility_id("-2.3")
#el8.click()
##set Explosure compensation ± 0
#el9 = driver.find_element_by_accessibility_id("± 0")
#el9.click()
##set Explosure compensation ± 0.3
#el11 = driver.find_element_by_accessibility_id("+0.3")
#el11.click()
##set Explosure compensation ± 0.7
#el11 = driver.find_element_by_accessibility_id("+0.7")
#el11.click()
##set Explosure compensation ± 1.0
#el11 = driver.find_element_by_accessibility_id("+1.0")
#el11.click()
##set Explosure compensation ± 1.3
#el11 = driver.find_element_by_accessibility_id("+1.3")
#el11.click()
##set Explosure compensation ± 1.7
#el11 = driver.find_element_by_accessibility_id("+1.7")
#el11.click()
##set Explosure compensation ± 2.0
#el11 = driver.find_element_by_accessibility_id("+2.0")
#el11.click()
##set Explosure compensation ± 2.3
#el11 = driver.find_element_by_accessibility_id("+2.3")
#el11.click()
##set Explosure compensation ± 2.7
#el11 = driver.find_element_by_accessibility_id("+2.7")
#el11.click()
##set Explosure compensation ± 3.0
#el11 = driver.find_element_by_accessibility_id("+3.0")
#el11.click()

##select WB setting
#el1 = driver.find_element_by_accessibility_id("WB")
#el5 = driver.find_element_by_accessibility_id("白平衡")

#wb item bar
#el1 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
#el5.click()
##set WB Auto
#el16 = driver.find_element_by_accessibility_id(" 自动")
#el3 = driver.find_element_by_accessibility_id(" AUTO")
#el16.click()
##set WB Sunny
#el15 = driver.find_element_by_accessibility_id(" 晴天")
#el2 = driver.find_element_by_accessibility_id(" SUNNY")
#el15.click()
##set WB Cloudy
#el17 = driver.find_element_by_accessibility_id(" 阴天")
#el4 = driver.find_element_by_accessibility_id(" CLOUDY")
#el17.click()
##set WB incandescent
#el18 = driver.find_element_by_accessibility_id(" 白炽灯")
#el5 = driver.find_element_by_accessibility_id(" INCAN")
#el18.click()
##set WB fluorescent
#el19 = driver.find_element_by_accessibility_id(" 荧光灯")
#el6 = driver.find_element_by_accessibility_id(" NEON")
#el19.click()
##set WB custom
#el20 = driver.find_element_by_accessibility_id(" 10000K ")
#el2 = driver.find_element_by_accessibility_id(" 6000K ")

#driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
#el20.click()
##set WB 2000K
#el26 = driver.find_element_by_accessibility_id(" 2000K")
##set WB 2100k
#el25 = driver.find_element_by_accessibility_id(" 2100K")
##set WB 2200k
#el1 = driver.find_element_by_accessibility_id("Back")
#el25 = driver.find_element_by_accessibility_id(" 2200K")
##set WB 2300k
#el25 = driver.find_element_by_accessibility_id(" 2300K")
##set WB 2400k
#el25 = driver.find_element_by_accessibility_id(" 2400K")
##set WB 2500K
#el26 = driver.find_element_by_accessibility_id(" 2500K")
##set WB 2600k
#el25 = driver.find_element_by_accessibility_id(" 2600K")
##set WB 2700k
#el25 = driver.find_element_by_accessibility_id(" 2700K")
##set WB 2800k
#el25 = driver.find_element_by_accessibility_id(" 2800K")
##set WB 2900k
#el25 = driver.find_element_by_accessibility_id(" 2900K")
##set WB 3000K
#el26 = driver.find_element_by_accessibility_id(" 3000K")
##set WB 3100k
#el25 = driver.find_element_by_accessibility_id(" 3100K")
##set WB 3200k
#el25 = driver.find_element_by_accessibility_id(" 3200K")
##set WB 3300k
#el25 = driver.find_element_by_accessibility_id(" 3300K")
##set WB 3400k
#el25 = driver.find_element_by_accessibility_id(" 3400K")
##set WB 3500K
#el26 = driver.find_element_by_accessibility_id(" 3500K")
##set WB 3600k
#el25 = driver.find_element_by_accessibility_id(" 3600K")
##set WB 3700k
#el25 = driver.find_element_by_accessibility_id(" 3700K")
##set WB 3800k
#el25 = driver.find_element_by_accessibility_id(" 3800K")
##set WB 3900k
#el25 = driver.find_element_by_accessibility_id(" 3900K")
##set WB 4000K
#el26 = driver.find_element_by_accessibility_id(" 4000K")
##set WB 4100k
#el25 = driver.find_element_by_accessibility_id(" 4100K")
##set WB 4200k
#el25 = driver.find_element_by_accessibility_id(" 4200K")
##set WB 4300k
#el25 = driver.find_element_by_accessibility_id(" 4300K")
##set WB 4400k
#el25 = driver.find_element_by_accessibility_id(" 4400K")
##set WB 4500K
#el26 = driver.find_element_by_accessibility_id(" 4500K")
##set WB 4600k
#el25 = driver.find_element_by_accessibility_id(" 4600K")
##set WB 4700k
#el25 = driver.find_element_by_accessibility_id(" 4700K")
##set WB 4800k
#el25 = driver.find_element_by_accessibility_id(" 4800K")
##set WB 4900k
#el25 = driver.find_element_by_accessibility_id(" 4900K")
##set WB 5000K
#el26 = driver.find_element_by_accessibility_id(" 5000K")
##set WB 5100k
#el25 = driver.find_element_by_accessibility_id(" 5100K")
##set WB 5200k
#el25 = driver.find_element_by_accessibility_id(" 5200K")
##set WB 5300k
#el25 = driver.find_element_by_accessibility_id(" 5300K")
##set WB 5400K
#el25 = driver.find_element_by_accessibility_id(" 5400K")
##set WB 5500K
#el26 = driver.find_element_by_accessibility_id(" 5500K")
##set WB 5600k
#el25 = driver.find_element_by_accessibility_id(" 5600K")
##set WB 5700k
#el25 = driver.find_element_by_accessibility_id(" 5700K")
##set WB 5800k
#el25 = driver.find_element_by_accessibility_id(" 5800K")
##set WB 5900k
#el25 = driver.find_element_by_accessibility_id(" 5900K")
##set WB 6000K
#el26 = driver.find_element_by_accessibility_id(" 6000K")
#el8 = driver.find_element_by_accessibility_id(" 6000K ")
##set WB 6100k
#el25 = driver.find_element_by_accessibility_id(" 6100K")
##set WB 6200k
#el25 = driver.find_element_by_accessibility_id(" 6200K")
##set WB 6300k
#el25 = driver.find_element_by_accessibility_id(" 6300K")
##set WB 6400k
#el25 = driver.find_element_by_accessibility_id(" 6400K")
##set WB 6500K
#el26 = driver.find_element_by_accessibility_id(" 6500K")
##set WB 6600k
#el25 = driver.find_element_by_accessibility_id(" 6600K")
##set WB 6700k
#el25 = driver.find_element_by_accessibility_id(" 6700K")
##set WB 6800k
#el25 = driver.find_element_by_accessibility_id(" 6800K")
##set WB 6900k
#el25 = driver.find_element_by_accessibility_id(" 6900K")
##set WB 7000K
#el26 = driver.find_element_by_accessibility_id(" 7000K")
##set WB 7100k
#el25 = driver.find_element_by_accessibility_id(" 7100K")
##set WB 7200k
#el25 = driver.find_element_by_accessibility_id(" 7200K")
##set WB 7300k
#el25 = driver.find_element_by_accessibility_id(" 7300K")
##set WB 7400k
#el25 = driver.find_element_by_accessibility_id(" 7400K")
##set WB 7500K
#el26 = driver.find_element_by_accessibility_id(" 7500K")
##set WB 7600k
#el25 = driver.find_element_by_accessibility_id(" 7600K")
##set WB 7700k
#el25 = driver.find_element_by_accessibility_id(" 7700K")
##set WB 7800k
#el25 = driver.find_element_by_accessibility_id(" 7800K")
##set WB 7900k
#el25 = driver.find_element_by_accessibility_id(" 7900K")
##set WB 8000K
#el26 = driver.find_element_by_accessibility_id(" 8000K")
##set WB 8100k
#el25 = driver.find_element_by_accessibility_id(" 8100K")
##set WB 8200k
#el25 = driver.find_element_by_accessibility_id(" 8200K")
##set WB 8300k
#el25 = driver.find_element_by_accessibility_id(" 8300K")
##set WB 8400k
#el25 = driver.find_element_by_accessibility_id(" 8400K")
##set WB 8500K
#el26 = driver.find_element_by_accessibility_id(" 8500K")
##set WB 8600k
#el25 = driver.find_element_by_accessibility_id(" 8600K")
##set WB 8700k
#el25 = driver.find_element_by_accessibility_id(" 8700K")
##set WB 8800k
#el25 = driver.find_element_by_accessibility_id(" 8800K")
##set WB 8900k
#el25 = driver.find_element_by_accessibility_id(" 8900K")
##set WB 9000K
#el26 = driver.find_element_by_accessibility_id(" 9000K")
##set WB 9100k
#el25 = driver.find_element_by_accessibility_id(" 9100K")
##set WB 9200k
#el25 = driver.find_element_by_accessibility_id(" 9200K")
##set WB 9300k
#el25 = driver.find_element_by_accessibility_id(" 9300K")
##set WB 9400k
#el25 = driver.find_element_by_accessibility_id(" 9400K")
##set WB 9500K
#el26 = driver.find_element_by_accessibility_id(" 9500K")
##set WB 9600k
#el25 = driver.find_element_by_accessibility_id(" 9600K")
##set WB 9700k
#el25 = driver.find_element_by_accessibility_id(" 9700K")
##set WB 9800k
#el25 = driver.find_element_by_accessibility_id(" 9800K")
##set WB 9900k
#el25 = driver.find_element_by_accessibility_id(" 9900K")
##set WB 10000k
#el25 = driver.find_element_by_accessibility_id(" 10000K")



##select color setting
##driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]")
#el6 = driver.find_element_by_accessibility_id("色彩")
#driver.find_element_by_accessibility_id("COLOR")
#el6.click()
##set color nature
#el29 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"自然\"])[1]")
#driver.find_element_by_accessibility_id("NONE")
##set color LOG
#el30 = driver.find_element_by_accessibility_id("LOG")
##set color vivid
#el31 = driver.find_element_by_accessibility_id("鲜艳")
#driver.find_element_by_accessibility_id("VIVID")
##set color BW
#el32 = driver.find_element_by_accessibility_id("黑白")
#driver.find_element_by_accessibility_id("B&W")
##SET color art
#el33 = driver.find_element_by_accessibility_id("艺术")
#driver.find_element_by_accessibility_id("ART")
##set color movie
#el34 = driver.find_element_by_accessibility_id("电影")
#driver.find_element_by_accessibility_id("FILM")
##set color beach
#el35 = driver.find_element_by_accessibility_id("海滩")
#driver.find_element_by_accessibility_id("BEACH")
##set color dream
#el36 = driver.find_element_by_accessibility_id("梦幻")
#driver.find_element_by_accessibility_id("DREAM")
##set color classic
#el37 = driver.find_element_by_accessibility_id("经典")
#driver.find_element_by_accessibility_id("CLASSIC")
##set color Old
#el38 = driver.find_element_by_accessibility_id("怀旧")
#driver.find_element_by_accessibility_id("NOSTALGIC")



##select style setting
#el7 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
#el7 = driver.find_element_by_accessibility_id("风格")
#el6 = driver.find_element_by_accessibility_id("STYLE")
#el7.click()
##set style standard
#el39 = driver.find_element_by_accessibility_id(" 标准 ±0 ±0 ±0")
#el3 = driver.find_element_by_accessibility_id(" STD. ±0 ±0 ±0")
##set style scene
#el40 = driver.find_element_by_accessibility_id(" 风光 +1 +1 ±0")
#el2 = driver.find_element_by_accessibility_id(" LAND. +1 +1 ±0")
##set style neutral
#el41 = driver.find_element_by_accessibility_id(" 中性 -1 ±0 ±0")
#el4 = driver.find_element_by_accessibility_id(" NEUT. -1 ±0 ±0")
##select style custom
#el42 = driver.find_element_by_accessibility_id("  ±0 ±0 ±0 ")
#el42 = driver.find_element_by_accessibility_id("  ±0 ±0 ±0 ")
##select clarity
#el44 = driver.find_element_by_accessibility_id(" 清晰度 ±0 ")
#el9 = driver.find_element_by_accessibility_id(" SHARPNESS +1 ")
#el11 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
##set clarity -3
#el45 = driver.find_element_by_accessibility_id(" -3")
##set clarity -2
#el45 = driver.find_element_by_accessibility_id(" -2")
##set clarity -1
#el45 = driver.find_element_by_accessibility_id(" -1")
##set clarity ±0
#el47 = driver.find_element_by_accessibility_id(" ±0")
##set clarity +1
#el48 = driver.find_element_by_accessibility_id(" +1")
##set clarity +2
#el48 = driver.find_element_by_accessibility_id(" +2")
 ##set clarity +3
#el48 = driver.find_element_by_accessibility_id(" +3")
##select contrast
#el49 = driver.find_element_by_accessibility_id(" 对比度 ±0 ")
##el8 = driver.find_element_by_accessibility_id(" CONTRAST ±0 ")
##set contrast -3
#el50 = driver.find_element_by_accessibility_id(" -3")
##set contrast -2
#el51 = driver.find_element_by_accessibility_id(" -2")
##set contrast -1
#el51 = driver.find_element_by_accessibility_id(" -1")
##set contrast ±0
#el53 = driver.find_element_by_accessibility_id(" ±0")
##set contrast +1
#el54 = driver.find_element_by_accessibility_id(" +1")
##set contrast +2
#el54 = driver.find_element_by_accessibility_id(" +2")
##set contrast +3
#el54 = driver.find_element_by_accessibility_id(" +3")
##select saturation
#el55 = driver.find_element_by_accessibility_id(" 饱和度 ±0 ")
#el10 = driver.find_element_by_accessibility_id(" SATURATION ±0 ")
##set saturation -3
#el50 = driver.find_element_by_accessibility_id(" -3")
##set saturation -2
#el51 = driver.find_element_by_accessibility_id(" -2")
##set saturation -1
#el51 = driver.find_element_by_accessibility_id(" -1")
##set saturation ±0
#el53 = driver.find_element_by_accessibility_id(" ±0")
##set saturation +1
#el54 = driver.find_element_by_accessibility_id(" +1")
##set saturation +2
#el54 = driver.find_element_by_accessibility_id(" +2")
##set saturation +3
#el54 = driver.find_element_by_accessibility_id(" +3")


##select digit zomm setting
#elm8 = driver.find_element_by_accessibility_id("数码变焦")
#driver.find_element_by_accessibility_id("DIGITAL ZOOM")
#el8.click()
#swip bar
#el5 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
#set digit zoom 1.0x
#el58 = driver.find_element_by_accessibility_id("1.0×")
#set digit zoom 2.0x
#el58 = driver.find_element_by_accessibility_id("2.0×")
#set digit zoom 3.0x
#el58 = driver.find_element_by_accessibility_id("3.0×")
#set digit zoom 4.0x
#el58 = driver.find_element_by_accessibility_id("4.0×")
#set digit zoom 5.0x
#el58 = driver.find_element_by_accessibility_id("5.0×")
#set digit zoom 6.0x
#el58 = driver.find_element_by_accessibility_id("6.0×")
#set digit zoom 7.0x
#el58 = driver.find_element_by_accessibility_id("7.0×")
#set digit zoom 8.0x
#el58 = driver.find_element_by_accessibility_id("8.0×")

##select photo size setting
#el59 = driver.find_element_by_accessibility_id("分辨率")
#el1 = driver.find_element_by_accessibility_id("SIZE")
##set photo size 4:3
#el60 = driver.find_element_by_accessibility_id("4000X3000(4:3)")
##set photo size 16:9
#el61 = driver.find_element_by_accessibility_id("4000X2250(16:9)")

##select photo filetype
#el62 = driver.find_element_by_accessibility_id("拍照格式")
#el2 = driver.find_element_by_accessibility_id("FORMAT")
##set photo filetype JPG
#el63 = driver.find_element_by_accessibility_id("JPG")
##set Photo filetype RAW
#el63 = driver.find_element_by_accessibility_id("RAW")
##set photo filetype RAW + JPG
#el64 = driver.find_element_by_accessibility_id("RAW + JPG")

#Bottom set bar
#el9 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView")
##selet capture type
#el65 = driver.find_element_by_accessibility_id("拍照模式")
#el3 = driver.find_element_by_accessibility_id("MODE")
#capture type swipe
##el2 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
##set single type
#el67 = driver.find_element_by_accessibility_id(" 单拍")
#el4 = driver.find_element_by_accessibility_id(" SINGLE SHOT")
##select burst capture
#el66 = driver.find_element_by_accessibility_id(" 连拍 ")
#el5 = driver.find_element_by_accessibility_id(" BURST ")

#BURST Set Bar
#el8 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
##set 3 burst
#el70 = driver.find_element_by_accessibility_id(" 3")
##set 5 burst
#el70 = driver.find_element_by_accessibility_id(" 5")
##set 7 burst
#el70 = driver.find_element_by_accessibility_id(" 7")
##set 10 burst
#el70 = driver.find_element_by_accessibility_id(" 10")
##set 14 burst
#el70 = driver.find_element_by_accessibility_id(" 14")
##select timelapse
#el72 = driver.find_element_by_accessibility_id(" 定时拍 ")
#el6 = driver.find_element_by_accessibility_id(" TIMELAPSE ")
#set bar
#el9 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
#set 2s timelapse
#el73 = driver.find_element_by_accessibility_id(" 2S")
#set 5s timelapse
#el73 = driver.find_element_by_accessibility_id(" 5S")
#set 7s timelapse
#el73 = driver.find_element_by_accessibility_id(" 7S")
#set 10s timelapse
#el73 = driver.find_element_by_accessibility_id(" 10S")
#set 20s timelapse
#el73 = driver.find_element_by_accessibility_id(" 20S")
#set 30s timelapse
#el73 = driver.find_element_by_accessibility_id(" 30S")
#set 60s timelapse
#el73 = driver.find_element_by_accessibility_id(" 60S")
#el7 = driver.find_element_by_accessibility_id(" AEB ")
#el6 = driver.find_element_by_accessibility_id(" 3")
#el5 = driver.find_element_by_accessibility_id(" 5")



##camera setting
#el3 = driver.find_element_by_accessibility_id("相机设置")
#el1 = driver.find_element_by_accessibility_id("Btn console camera setting")
##net grid
#el11 = driver.find_element_by_accessibility_id("网格")
## no net grid
#el9 = driver.find_element_by_accessibility_id("无")
## net grid
#el8 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"网格\"])[3]")
##net grid and Hline
#el10 = driver.find_element_by_accessibility_id("网格＋横线")
##
##centre point
#el12 = driver.find_element_by_accessibility_id("中心点")
##no centre point
#el13 = driver.find_element_by_accessibility_id("无")
## circle
#el14 = driver.find_element_by_accessibility_id("圆形（有中心点)")
##closs lines
#el15 = driver.find_element_by_accessibility_id("十字交叉")
##square no centre point
#el16 = driver.find_element_by_accessibility_id("正方形（无中心点）")
##square with centre point
#el17 = driver.find_element_by_accessibility_id("正方形（有中心点）")
##circle and closs lines
#el18 = driver.find_element_by_accessibility_id("圆形（十字交叉）")
##
##zhifangtukaiguan
#el19 = driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name=\"直方图\"]")
##guobaogaojingkaiguan
#el21 = driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name=\"过曝警告\"]")
##shipinzimukaiguan
#el22 = driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name=\"视频字幕\"]")

##select anti-flick
#el23 = driver.find_element_by_accessibility_id("抗闪烁")
##set auto anti-flick
#el24 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"自动\"])[4]")
##set 50HZ anti-flick
#el25 = driver.find_element_by_accessibility_id("50Hz")
##set 60HZ anti-flick
##el25 = driver.find_element_by_accessibility_id("60Hz")

##select video code format
#el27 = driver.find_element_by_accessibility_id("视频编码格式")
##set H264
#el28 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"H.264\"])[2]")
#el29 = driver.find_element_by_accessibility_id("H.264")
##set H265
#el29 = driver.find_element_by_accessibility_id("H.265")

##select format SD card
#el30 = driver.find_element_by_accessibility_id("格式化SD卡")
##format SD card
#el31 = driver.find_element_by_accessibility_id("格式化")
##cancel format SD card
#el33 = driver.find_element_by_accessibility_id("取消")

##select reset camera
#el34 = driver.find_element_by_accessibility_id("重置相机")
##cancal reset camera
#el35 = driver.find_element_by_accessibility_id("取消")
##reset camera
#el37 = driver.find_element_by_accessibility_id("确定")


##realtime video interface
#el1 = driver.find_element_by_accessibility_id("Img_console_media_bg")
# def setVideoStandardwithBottomBar(self):
    #     try:
    #         BottomBarelement = self.InitalDevice.driver.find_element_by_accessibility_id("Img_console_bottom_bar_bg")
    #     except Exception as e:
    #         self.logger.logger.warn(e)
    #         print e
    #     else:
    #         params = {'direction': 'right',"element":BottomBarelement}
    #         self.InitalDevice.driver.execute_script("mobile: swipe",params)
    #         #gimbal
    #         #self.InitalDevice.driver.execute_script("mobile: tap",{"x":25,"y":337})
    #         #piv
    #         self.InitalDevice.driver.execute_script("mobile: tap", {"x": 125, "y": 337})
    #         sleep(0.5)
    #         helpelement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn console help normal")
    #         sleep(0.5)
    #         helpelement.click()
    #         sleep(0.5)
    #         PIVHelpContextElement = self.InitalDevice.driver.find_element_by_accessibility_id(
    #         "PIV功能可实现在录像的同时拍摄静止照片。EVO可在录像的同时捕捉截图并保存为JPEG格式的照片，但不支持RAW格式。所保存照片的分辨率将和录像分辨率保持一致。")
    #         sleep(0.5)
    #         # swip help left
    #         self.InitalDevice.driver.execute_script("mobile: swipe", {'direction': 'left',"element":PIVHelpContextElement})
    #         sleep(0.5)
    #         VideostandardContextElement= self.InitalDevice.driver.find_element_by_accessibility_id("此选项要根据具体的国家地区来区分。NTSC为美国地区的标准播放格式，PAL为欧洲、澳洲和部分亚洲地区的标准播放格式。")
    #         sleep(0.5)
    #         # swip help right
    #         self.InitalDevice.driver.execute_script("mobile: swipe", {'direction': 'right',"element":VideostandardContextElement})
    #         sleep(0.5)
    #         # close help
    #         SettingHelpElement = self.InitalDevice.driver.find_element_by_accessibility_id("Btn settings aircraftStatus cl")
    #         SettingHelpElement.click()
    #         sleep(0.5)
    #         ##swipe piv setting bar left
    #         PIVSettingBarElement = self.InitalDevice.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Autel Explorer\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView")
    #         self.InitalDevice.driver.execute_script("mobile: swipe",
    #                                                 {'direction': 'left', "element": PIVSettingBarElement})
    #         sleep(0.5)
    #         #piv help
    #         #el2 = driver.find_element_by_accessibility_id("Btn console help normal")
    #         #el2.click()
    #         #clos help
    #         #el1 = driver.find_element_by_accessibility_id("Btn settings aircraftStatus cl")
    #         #el1.click()
    #         ##previus help
    #         #el2 = driver.find_element_by_accessibility_id("Btn console help previou n")
    #         #el2.click()
    #         ##next help
    #         #el4 = driver.find_element_by_accessibility_id("Btn console help next n")
    #         #el4.click()
    #
    #
    #         ##find gimbal help element
    #         #el3 = driver.find_element_by_accessibility_id("云台角度")
    #         ##find gimbal angel help context element
    #         #el47 = driver.find_element_by_accessibility_id("飞机云台的转动角度。")
    #         #swip help left
    #         # self.InitalDevice.driver.execute_script("mobile: swipe", {'direction': 'left',"element":el47})
    #         ##find PIV help element
    #         #el5 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"PIV\"])[3]")
    #         ##finde PIV help context element
    #         # el46 = driver.find_element_by_accessibility_id("PIV功能可实现在录像的同时拍摄静止照片。EVO可在录像的同时捕捉截图并保存为JPEG格式的照片，但不支持RAW格式。所保存照片的分辨率将和录像分辨率保持一致。")
    #         # swip help left
    #         # self.InitalDevice.driver.execute_script("mobile: swipe", {'direction': 'left',"element":el46})
    #         # swip help right
    #         # self.InitalDevice.driver.execute_script("mobile: swipe", {'direction': 'right',"element":el46})
    #         ##find PIV help element
    #         ##find video standard help element
    #         #el7 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"视频制式\"])[2]")
    #         ##find video standard help context element
    #         #el45 = driver.find_element_by_accessibility_id("此选项要根据具体的国家地区来区分。NTSC为美国地区的标准播放格式，PAL为欧洲、澳洲和部分亚洲地区的标准播放格式。")
    #         ##find video format help element
    #         #el9 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"视频格式\"])[2]")
    #         ##find video format help context element
    #         #el44 = driver.find_element_by_accessibility_id("MP4是大多数媒体播放器和编辑工具所识别的标准格式，较常用于电脑。MOV则是苹果公司的标准格式，默认与苹果播放器和编辑工具一同使用。")
    #         ##find video resolution help element
    #         #el11 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"视频分辨率\"])[2]")
    #         ##finde video resolution help context element
    #         #el43 = driver.find_element_by_accessibility_id("高分辨率可拍摄出尺寸较大的高质量照片。")
    #         ##find video fps help element
    #         #el13 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"视频帧率\"])[2]")
    #         ##find video fps help context element
    #         #el42 = driver.find_element_by_accessibility_id("每秒帧数会随着分辨率设定的变化而变化。当每秒帧数较高时，录像可以捕捉慢镜头。")
    #         ##find exposure mode help element
    #         #el15 = driver.find_element_by_accessibility_id("曝光模式")
    #         ##find exposure mode help context element
    #         #el41 = driver.find_element_by_accessibility_id("曝光模式选择手动，可自行调节感光度和快门速度；曝光模式选择自动，相机将会自动调节。手动挡情况下，曝光补偿设定不可调节；自动挡情况下，感光度和快门速度不可调节。")
    #         ##find iso help element
    #         #el17 = driver.find_element_by_accessibility_id("感光度")
    #         ##find iso help context element
    #         #el40 = driver.find_element_by_accessibility_id("此设置将图像传感器调整为对光敏感。低感光度适用于阳光明媚的天气；高感光度适用于光照不足的场景，但是会因此增加图像噪点。")
    #         ##find shutter help element
    #         #el19 = driver.find_element_by_accessibility_id("快门速度")
    #         ##find shutter help context element
    #         #el39 = driver.find_element_by_accessibility_id("快门速度决定了传感器曝光时间的长短。快门速度快时，运动物体就会在底片呈现更清晰的影像；快门速度慢时，更多光会进入传感器，适用于光照不足的场景。")
    #         ##find exposure compensation help element
    #         #el21 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"曝光补偿\"])[2]")
    #         ##find exposure compensation help context element
    #         #el38 = driver.find_element_by_accessibility_id("曝光补偿为感光度和快门速度的结合，此设置在选择相机自动挡时使用。增大曝光补偿会使光线变亮，减小曝光补偿会使光线变暗。")
    #         ##find WB help element
    #         #el23 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"白平衡\"])[2]")
    #         ##find WB help context element
    #         #el37 = driver.find_element_by_accessibility_id("白平衡用来设置照片和视频的色温。")
    #         ##find color help element
    #         #el25 = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name=\"色彩\"])[2]")
    #         ##find color help context element
    #         #el36 = driver.find_element_by_accessibility_id("色彩选项可以自定义相机内照片和视频的外观，从而不再需要进行后期处理。")
    #         ##find style help element
    #         #el27 = driver.find_element_by_accessibility_id("风格")
    #         ##find style help context element
    #         #el32 = driver.find_element_by_accessibility_id("风格选项可以为相机提供更多控制功能，可以通过调节对比度、饱和度和清晰度来为照片和视频定义独特的外观。")
    #         ##find digit zoom help element
    #         #el29 = driver.find_element_by_accessibility_id("数码")
    #         ##find digit zoom help context element
    #         #el30 = driver.find_element_by_accessibility_id("数码变焦通过放大拍摄对象来使用相机传感器进行剪裁，但此方法会降低图片的分辨率。")





