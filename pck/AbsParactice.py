from abc import ABC, abstractmethod

class Father(ABC):
      @abstractmethod
      def pradeep_tiwari(self):
          pass

      def __init__(self):
          print("I am Constructer")

      def tiwari(self):
          print("Concrete method")


class Self(Father):
    # def __init__(self):
    #     print("I am child constructor")

    def pradeep_tiwari(self):
        print("child")


obj = Self()
obj.tiwari()
obj.pradeep_tiwari()
