class BulkApiResultEventStore:

    def __init__(self, Id=None, CreatedDate=None, EventIdentifier=None, UserId=None, Username=None, EventDate=None, RelatedEventIdentifier=None, PolicyId=None, PolicyOutcome=None, EvaluationTime=None, SessionKey=None, LoginKey=None, SessionLevel=None, SourceIp=None, LoginHistoryId=None, Query=None):
        self.Id = Id
        self.CreatedDate = CreatedDate
        self.EventIdentifier = EventIdentifier
        self.UserId = UserId
        self.Username = Username
        self.EventDate = EventDate
        self.RelatedEventIdentifier = RelatedEventIdentifier
        self.PolicyId = PolicyId
        self.PolicyOutcome = PolicyOutcome
        self.EvaluationTime = EvaluationTime
        self.SessionKey = SessionKey
        self.LoginKey = LoginKey
        self.SessionLevel = SessionLevel
        self.SourceIp = SourceIp
        self.LoginHistoryId = LoginHistoryId
        self.Query = Query


