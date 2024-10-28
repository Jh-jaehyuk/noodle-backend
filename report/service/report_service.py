from abc import abstractmethod, ABC


class ResultReportService(ABC):
    @abstractmethod
    def createResultReport(self, username, **kwargs):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def read(self, resultReportId):
        pass