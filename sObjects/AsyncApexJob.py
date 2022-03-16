class AsyncApexJob:

    def __init__(self, Id=None, CreatedDate=None, CreatedById=None, JobType=None, ApexClassId=None, Status=None, JobItemsProcessed=None, TotalJobItems=None, NumberOfErrors=None, CompletedDate=None, MethodName=None, ExtendedStatus=None, ParentJobId=None, LastProcessed=None, LastProcessedOffset=None):
        self.Id = Id
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.JobType = JobType
        self.ApexClassId = ApexClassId
        self.Status = Status
        self.JobItemsProcessed = JobItemsProcessed
        self.TotalJobItems = TotalJobItems
        self.NumberOfErrors = NumberOfErrors
        self.CompletedDate = CompletedDate
        self.MethodName = MethodName
        self.ExtendedStatus = ExtendedStatus
        self.ParentJobId = ParentJobId
        self.LastProcessed = LastProcessed
        self.LastProcessedOffset = LastProcessedOffset


