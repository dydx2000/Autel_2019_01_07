import time


def CamModeLaps_2s(driver): #2S
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(0.5)
    driver.swipe(0.16, 0.82, 0.856, 0.82, 300)  # 左滑到右
    time.sleep(0.5)
    # driver.swipe(0.16, 0.82, 0.856, 0.82, 300)  # 左滑到右
    # time.sleep(0.5)
    # driver.swipe(0.16, 0.82, 0.856, 0.82, 300)  # 左滑到右

def CamModeLaps_5s(driver): #5S
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(0.5)
    driver.swipe(0.16, 0.82, 0.856, 0.82, 300)  # 左滑到右
    time.sleep(0.5)
    driver.swipe(0.5,0.82,0.25,0.82)

def CamModeLaps_7s(driver): #7S
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(0.5)
    driver.swipe(0.16, 0.82, 0.856, 0.82, 300)  # 左滑到右
    time.sleep(0.5)
    driver.swipe(0.5,0.82,0.25,0.82)
    time.sleep(0.5)
    driver.swipe(0.5,0.82,0.25,0.82)

def CamModeLaps_10s(driver): #10S
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(0.5)
    driver.swipe(0.856, 0.82,0.16, 0.82,300)  # 右滑到左
    time.sleep(0.5)
    driver.swipe(0.25,0.82,0.5,0.82)
    time.sleep(0.5)
    driver.swipe(0.25,0.82,0.5,0.82)
    time.sleep(0.5)
    driver.swipe(0.25, 0.82, 0.5, 0.82)

def CamModeLaps_20s(driver): #20S
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(0.5)
    driver.swipe(0.856, 0.82,0.16, 0.82,300)  # 右滑到左
    time.sleep(0.5)
    driver.swipe(0.25,0.82,0.5,0.82)
    time.sleep(0.5)
    driver.swipe(0.25,0.82,0.5,0.82)


    # time.sleep(0.5)
    # driver.swipe(0.5,0.82,0.25,0.82)

def CamModeLaps_30s(driver): #30S
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(0.5)
    driver.swipe(0.856, 0.82,0.16, 0.82,300)  # 右滑到左
    time.sleep(0.5)
    driver.swipe(0.25,0.82,0.5,0.82)
    # time.sleep(0.5)
    # driver.swipe(0.5,0.82,0.25,0.82)

def CamModeLaps_60s(driver): #60S
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(0.5)
    driver.swipe(0.856, 0.82,0.16, 0.82,300)  # 右滑到左
    # time.sleep(0.5)
    # driver.swipe(0.5,0.82,0.25,0.82)
    # time.sleep(0.5)
    # driver.swipe(0.5,0.82,0.25,0.82)

