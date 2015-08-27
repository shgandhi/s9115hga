def ok(*lst):
    print "###", lst[0].__name__
    for one in lst: unittest(one)
    return one

class unittest:
    tries = fails = 0 #track the record
    @staticmethod
    def score():
        t = unittest.tries
        f = unittest.fails
        return "# TRIES= %s FAIL= %s %%PASS=%s%%" % (
            t, f, int(round(t*100/(t+f+0.001))))
            
    def __init__(self, test): #pass the test when the unittest class is created
        unittest.tries += 1   #tries is inc by 1
        try:                    
            test()             #run test
        except Exception,e:
            unittest.fails += 1 #if failed inc fails
            self.report(test)
            
    def report(self, test):
        import traceback
        print traceback.format_exc()
        print unittest.score(), ':',test.__name__