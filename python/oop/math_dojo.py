class Mathdojo(object):
    def __init__(self):
        self.sum=0
    def adding(self, *args):
        running=list(args)
        for x in running:
            if isinstance(x, list):
                for thingy in x:
                    running.append(thingy)                    
            else:
                self.sum+=x
        print self.sum
        return self
    def subtracting(self, *args):
        running=list(args)
        for y in running:
            if isinstance(y, list or tuple):
                for thingy in y:
                    running.append(thingy)                    
            else:
                self.sum-=y
        print self.sum
        return self
thingy = Mathdojo()
thingy.adding(1,6,7, 2, [2,3], [1.1,2.3]).subtracting(4,2,2, [2,3], [1.1,2.3,(2,5)])