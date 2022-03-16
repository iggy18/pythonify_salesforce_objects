class PermissionSetEventStore:

    def __init__(self, Id=None, CreatedDate=None, EventIdentifier=None, UserId=None, Username=None, EventDate=None, RelatedEventIdentifier=None, PolicyId=None, PolicyOutcome=None, EvaluationTime=None, SessionKey=None, LoginKey=None, SessionLevel=None, SourceIp=None, LoginHistoryId=None, EventSource=None, Operation=None, ParentIdList=None, ParentNameList=None, PermissionType=None, PermissionList=None, ImpactedUserIds=None, UserCount=None):
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
        self.EventSource = EventSource
        self.Operation = Operation
        self.ParentIdList = ParentIdList
        self.ParentNameList = ParentNameList
        self.PermissionType = PermissionType
        self.PermissionList = PermissionList
        self.ImpactedUserIds = ImpactedUserIds
        self.UserCount = UserCount


