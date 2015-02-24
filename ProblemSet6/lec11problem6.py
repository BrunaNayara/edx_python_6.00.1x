class Queue(object):

    def __init__(self);
        """Initialize empty queue  """
        self.vals = []

    def insert(self, e):
        """ Insert one element at the end of the Queue"""
        self.vals.append(e)

    def remove(self):
        """ Remove one element of the Queue (the fisrt) and return it"""
        try:
            pop = self.vals[0]
            self.vals = self.vals[1:]
            return pop
        except:
            raise ValueError()
