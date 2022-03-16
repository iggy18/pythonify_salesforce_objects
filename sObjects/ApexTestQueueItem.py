class ApexTestQueueItem:

    def __init__(self, Id=None, CreatedDate=None, CreatedById=None, SystemModstamp=None, ApexClassId=None, Status=None, ExtendedStatus=None, ParentJobId=None, TestRunResultId=None, ShouldSkipCodeCoverage=None):
        self.Id = Id
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.SystemModstamp = SystemModstamp
        self.ApexClassId = ApexClassId
        self.Status = Status
        self.ExtendedStatus = ExtendedStatus
        self.ParentJobId = ParentJobId
        self.TestRunResultId = TestRunResultId
        self.ShouldSkipCodeCoverage = ShouldSkipCodeCoverage


