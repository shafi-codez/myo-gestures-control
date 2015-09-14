from __future__ import print_function

import myo as libmyo;

libmyo.init()
import time
import sys, os


class Listener(libmyo.DeviceListener):
    """
    Listener implementation. Return False from any function to
    stop the Hub.
    """

    interval = 0.05  # Output only 0.05 seconds

    def __init__(self):
        super(Listener, self).__init__()
        self.orientation = None
        self.pose = libmyo.Pose.rest
        self.emg_enabled = False
        self.locked = False
        self.rssi = None
        self.emg = None
        self.last_time = 0

    @staticmethod
    def open_google_on_fingers_spread():
        import subprocess

        subprocess.call(
            [r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe', '-new-tab', 'http://www.monkeybars.io/'])

    @staticmethod
    def post_data_on_double_tap():
        import requests
        r = requests.get('http://jsonplaceholder.typicode.com/posts?userId=1')
        print(r.content)

    @staticmethod
    def create_file_on_wave_in():
        fileName = "C:\Users\sulla\Documents\myo\processing-3.0b6-windows64\processing-3.0b6\modes\java\examples\Topics\File IO\LoadFile1\data\positions.txt"
        if os.path.isfile(fileName) is True:
            file_var = open(fileName, "w+")
            file_var.write("1")
            print("\nFile Name:", file_var.name)
            print("\nClosed :", file_var.closed)

    @staticmethod
    def create_file_on_wave_out():
        fileName = "C:\Users\sulla\Documents\myo\processing-3.0b6-windows64\processing-3.0b6\modes\java\examples\Topics\File IO\LoadFile1\data\positions.txt"
        if os.path.isfile(fileName) is True:
            file_var = open(fileName, "w+")
            file_var.write("0")
            print("\nFile Name:", file_var.name)
            print("\nClosed :", file_var.closed)


    @staticmethod
    def open_media_file_on_fist():
        import os

        os.startfile('C:\Users\sulla\Videos\Spartan Race Super - Chicago 2014.mp4')

    def output(self):
        ctime = time.time()
        if (ctime - self.last_time) < self.interval:
            return
        self.last_time = ctime

        parts = []
        if self.orientation:
            for comp in self.orientation:
                parts.append(str(comp).ljust(15))
        parts.append(str(self.pose).ljust(10))
        parts.append('E' if self.emg_enabled else ' ')
        parts.append('L' if self.locked else ' ')
        parts.append(self.rssi or 'NORSSI')
        if self.emg:
            for comp in self.emg:
                parts.append(str(comp).ljust(5))
        print('\r' + ''.join('[ {0} ]'.format(p) for p in parts), end='')
        sys.stdout.flush()

    def on_connect(self, myo, timestamp, firmware_version):
        print("on_connect......")
        myo.vibrate('short')
        myo.vibrate('short')
        myo.request_rssi()
        myo.request_battery_level()

    def on_rssi(self, myo, timestamp, rssi):
        self.rssi = rssi
        self.output()

    def on_pose(self, myo, timestamp, pose):
        if pose == libmyo.Pose.fingers_spread:
            print("\nAction Captured >> FINGER SPREAD\n")
            self.open_google_on_fingers_spread()
            myo.set_stream_emg(libmyo.StreamEmg.disabled)
            self.emg_enabled = False
            self.emg = None
        elif pose == libmyo.Pose.double_tap:
            print("\nAction Captured >> DOUBLE TAP\n")
            self.post_data_on_double_tap()
            myo.set_stream_emg(libmyo.StreamEmg.enabled)
            self.post_data_on_double_tap()
            self.emg_enabled = True
        elif pose == libmyo.Pose.wave_in:
            print("\nAction Captured >> WAVE IN\n")
            self.create_file_on_wave_in()
            self.emg_enabled = False
            self.emg = None
        elif pose == libmyo.Pose.wave_out:
            print("\nAction Captured >> WAVE OUT\n")
            self.create_file_on_wave_out()
            self.emg_enabled = False
            self.emg = None
        elif pose == libmyo.Pose.fist:
            print("\nAction Captured >> HOLD FIST\n")
            self.open_media_file_on_fist()
            self.emg_enabled = False
            self.emg = None
        self.pose = pose
        self.output()

    def on_orientation_data(self, myo, timestamp, orientation):
        self.orientation = orientation
        self.output()

    def on_accelerometor_data(self, myo, timestamp, acceleration):
        pass

    def on_gyroscope_data(self, myo, timestamp, gyroscope):
        pass

    def on_emg_data(self, myo, timestamp, emg):
        self.emg = emg
        self.output()

    def on_unlock(self, myo, timestamp):
        self.locked = False
        self.output()

    def on_lock(self, myo, timestamp):
        self.locked = True
        self.output()

    def on_event(self, kind, event):
        """
        Called before any of the event callbacks.
        """

    def on_event_finished(self, kind, event):
        """
        Called after the respective event callbacks have been
        invoked. This method is *always* triggered, even if one of
        the callbacks requested the stop of the Hub.
        """

    def on_pair(self, myo, timestamp, firmware_version):
        """
        Called when a Myo armband is paired.
        """

    def on_unpair(self, myo, timestamp):
        """
        Called when a Myo armband is unpaired.
        """

    def on_disconnect(self, myo, timestamp):
        """
        Called when a Myo is disconnected.
        """

    def on_arm_sync(self, myo, timestamp, arm, x_direction, rotation,
                    warmup_state):
        """
        Called when a Myo armband and an arm is synced.
        """

    def on_arm_unsync(self, myo, timestamp):
        """
        Called when a Myo armband and an arm is unsynced.
        """

    def on_battery_level_received(self, myo, timestamp, level):
        """
        Called when the requested battery level received.
        """

    def on_warmup_completed(self, myo, timestamp, warmup_result):
        """
        Called when the warmup completed.
        """

def main():
    print("Connecting to Myo ... Use CTRL^C to exit.")
    print("If nothing happens, make sure the Bluetooth adapter is plugged in,")
    print("Myo Connect is running and your Myo is put on.")
    hub = libmyo.Hub()
    hub.set_locking_policy(libmyo.LockingPolicy.none)
    hub.run(1000, Listener())

    # Listen to keyboard interrupts and stop the hub in that case.
    try:
        while hub.running:
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\nQuitting ...")
    finally:
        print("Shutting down hub...")
        hub.shutdown()


if __name__ == '__main__':
    main()

