class ReportAnomalyEvent:

    def __init__(self, ReplayId=None, CreatedDate=None, EventUuid=None, EventIdentifier=None, UserId=None, Username=None, EventDate=None, SessionKey=None, LoginKey=None, SourceIp=None, PolicyId=None, PolicyOutcome=None, EvaluationTime=None, Report=None, SecurityEventData=None, Summary=None, Score=None):
        self.ReplayId = ReplayId
        self.CreatedDate = CreatedDate
        self.EventUuid = EventUuid
        self.EventIdentifier = EventIdentifier
        self.UserId = UserId
        self.Username = Username
        self.EventDate = EventDate
        self.SessionKey = SessionKey
        self.LoginKey = LoginKey
        self.SourceIp = SourceIp
        self.PolicyId = PolicyId
        self.PolicyOutcome = PolicyOutcome
        self.EvaluationTime = EvaluationTime
        self.Report = Report
        self.SecurityEventData = SecurityEventData
        self.Summary = Summary
        self.Score = Score


