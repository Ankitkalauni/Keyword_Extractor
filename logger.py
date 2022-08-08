from datetime import datetime

class Logger:
    """
    Logger class to log files as a activity history.
    """
    def __init__(self) -> None:
        pass
        
    def log(self, file_obj: "FileObject", mssg: str) -> None:
        """
        file_obj -> Takes FileObject as argument.
        mssg     -> String Message to log.
        """
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_obj.write(str(self.date) + "/" + str(self.current_time) + "\t\t" + mssg +"\n")
