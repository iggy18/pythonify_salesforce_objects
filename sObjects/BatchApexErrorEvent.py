class BatchApexErrorEvent:

    def __init__(self, ReplayId=None, CreatedDate=None, CreatedById=None, EventUuid=None, ExceptionType=None, Message=None, StackTrace=None, RequestId=None, AsyncApexJobId=None, JobScope=None, DoesExceedJobScopeMaxLength=None, Phase=None):
        self.ReplayId = ReplayId
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.EventUuid = EventUuid
        self.ExceptionType = ExceptionType
        self.Message = Message
        self.StackTrace = StackTrace
        self.RequestId = RequestId
        self.AsyncApexJobId = AsyncApexJobId
        self.JobScope = JobScope
        self.DoesExceedJobScopeMaxLength = DoesExceedJobScopeMaxLength
        self.Phase = Phase


