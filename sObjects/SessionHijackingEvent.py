class SessionHijackingEvent:

    def __init__(self, ReplayId=None, CreatedDate=None, EventUuid=None, EventIdentifier=None, UserId=None, Username=None, EventDate=None, SessionKey=None, LoginKey=None, SourceIp=None, PolicyId=None, PolicyOutcome=None, EvaluationTime=None, Score=None, Summary=None, CurrentIp=None, PreviousIp=None, CurrentPlatform=None, PreviousPlatform=None, CurrentScreen=None, PreviousScreen=None, CurrentUserAgent=None, PreviousUserAgent=None, CurrentWindow=None, PreviousWindow=None, SecurityEventData=None):
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
        self.Score = Score
        self.Summary = Summary
        self.CurrentIp = CurrentIp
        self.PreviousIp = PreviousIp
        self.CurrentPlatform = CurrentPlatform
        self.PreviousPlatform = PreviousPlatform
        self.CurrentScreen = CurrentScreen
        self.PreviousScreen = PreviousScreen
        self.CurrentUserAgent = CurrentUserAgent
        self.PreviousUserAgent = PreviousUserAgent
        self.CurrentWindow = CurrentWindow
        self.PreviousWindow = PreviousWindow
        self.SecurityEventData = SecurityEventData


