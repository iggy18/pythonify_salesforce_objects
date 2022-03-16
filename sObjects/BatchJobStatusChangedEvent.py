class BatchJobStatusChangedEvent:

    def __init__(self, ReplayId=None, CreatedDate=None, CreatedById=None, EventUuid=None, BatchJobDefinition=None, BatchJob=None, Status=None, StartDateTime=None, EndDateTime=None):
        self.ReplayId = ReplayId
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.EventUuid = EventUuid
        self.BatchJobDefinition = BatchJobDefinition
        self.BatchJob = BatchJob
        self.Status = Status
        self.StartDateTime = StartDateTime
        self.EndDateTime = EndDateTime


