import abc


class TaskManageRepository(abc.ABC):
    @abc.abstractmethod
    def createTask(self, target, args):
        pass

    @abc.abstractmethod
    def endTask(self):
        pass