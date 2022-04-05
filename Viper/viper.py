from viper.scan.scan import scan_aps, scan_ap

class Viper:
    def __init__(self):
        self.interface = self.init_interface()

    def init_interface(self):
        """
        Initiate wireless network interface for monitor mode.
        """
        pass
    
    def scan(self):
        """
        Scan all available access points and return all available information.
        """
        aps = scan_aps(self.interface)
        for ap in aps:
            result_ap = scan_ap(interface, ap)
            print(result_ap.asdict())
        