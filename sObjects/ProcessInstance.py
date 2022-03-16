class ProcessInstance:

    def __init__(self, Id=None, ProcessDefinitionId=None, TargetObjectId=None, Status=None, CompletedDate=None, LastActorId=None, ElapsedTimeInDays=None, ElapsedTimeInHours=None, ElapsedTimeInMinutes=None, SubmittedById=None, IsDeleted=None, CreatedDate=None, CreatedById=None, LastModifiedDate=None, LastModifiedById=None, SystemModstamp=None):
        self.Id = Id
        self.ProcessDefinitionId = ProcessDefinitionId
        self.TargetObjectId = TargetObjectId
        self.Status = Status
        self.CompletedDate = CompletedDate
        self.LastActorId = LastActorId
        self.ElapsedTimeInDays = ElapsedTimeInDays
        self.ElapsedTimeInHours = ElapsedTimeInHours
        self.ElapsedTimeInMinutes = ElapsedTimeInMinutes
        self.SubmittedById = SubmittedById
        self.IsDeleted = IsDeleted
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.LastModifiedDate = LastModifiedDate
        self.LastModifiedById = LastModifiedById
        self.SystemModstamp = SystemModstamp


