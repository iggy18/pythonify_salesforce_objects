class ProcessExceptionEvent:

    def __init__(self, ReplayId=None, CreatedDate=None, CreatedById=None, EventUuid=None, AttachedToId=None, Message=None, Description=None, ExceptionType=None, Severity=None, BackgroundOperationId=None, ExternalReference=None):
        self.ReplayId = ReplayId
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.EventUuid = EventUuid
        self.AttachedToId = AttachedToId
        self.Message = Message
        self.Description = Description
        self.ExceptionType = ExceptionType
        self.Severity = Severity
        self.BackgroundOperationId = BackgroundOperationId
        self.ExternalReference = ExternalReference


