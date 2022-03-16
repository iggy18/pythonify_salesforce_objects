class ApexTestResult:

    def __init__(self, Id=None, SystemModstamp=None, TestTimestamp=None, Outcome=None, ApexClassId=None, MethodName=None, Message=None, StackTrace=None, AsyncApexJobId=None, QueueItemId=None, ApexLogId=None, ApexTestRunResultId=None, RunTime=None):
        self.Id = Id
        self.SystemModstamp = SystemModstamp
        self.TestTimestamp = TestTimestamp
        self.Outcome = Outcome
        self.ApexClassId = ApexClassId
        self.MethodName = MethodName
        self.Message = Message
        self.StackTrace = StackTrace
        self.AsyncApexJobId = AsyncApexJobId
        self.QueueItemId = QueueItemId
        self.ApexLogId = ApexLogId
        self.ApexTestRunResultId = ApexTestRunResultId
        self.RunTime = RunTime


