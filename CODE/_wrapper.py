from Custom_Libraries.Log import *
from Custom_Libraries.Actions import *
import ctypes


class Checks:
    def __init__(self):
        self.Actions = Actions()

    @staticmethod
    def is_admin() -> bool:
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except AttributeError:
            return False

    def using_uac(self) -> bool:
        value = self.Actions.run_command("powershell (Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System).EnableLUA")
        return int(value.strip("\n")) == 1

if __name__ == "__main__":
    WEBHOOK, DEBUG, VERSION, FILES, API_KEY = Actions.read_config()
    os.makedirs("../ACCESS/LOGS/", exist_ok=True)
    log = Log(debug=DEBUG)
    action, sub_action = Actions().flags()
    print(action, sub_action)