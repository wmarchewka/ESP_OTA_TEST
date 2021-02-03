from ulogging import Logger


class Tester(object):
    def __init__(self):
        pass

    def connectToWifiAndUpdate():
        import time, machine, network, gc, app.secrets as secrets
        time.sleep(1)
        print('Memory free', gc.mem_free())

        from app.ota_updater import OTAUpdater

        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
            while not sta_if.isconnected():
                pass
        print('network config:', sta_if.ifconfig())
        otaUpdater = OTAUpdater('https://github.com/rdehuyss/micropython-ota-updater', main_dir='app', secrets_file="secrets.py")
        hasUpdated = otaUpdater.install_update_if_available()
        if hasUpdated:
            machine.reset()
        else:
            del(otaUpdater)
            gc.collect()

    def startApp():
        import app.start


    def run(self):
        self.log = Logger("debug")
        self.log.setLevel(10)
        self.log.debug("Walt")

#connectToWifiAndUpdate()
#startApp()

tst = Tester()
tst.run()