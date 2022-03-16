class AuthSession:

    def __init__(self, Id=None, UsersId=None, CreatedDate=None, LastModifiedDate=None, NumSecondsValid=None, UserType=None, SourceIp=None, LoginType=None, SessionType=None, SessionSecurityLevel=None, LogoutUrl=None, ParentId=None, LoginHistoryId=None, LoginGeoId=None, IsCurrent=None):
        self.Id = Id
        self.UsersId = UsersId
        self.CreatedDate = CreatedDate
        self.LastModifiedDate = LastModifiedDate
        self.NumSecondsValid = NumSecondsValid
        self.UserType = UserType
        self.SourceIp = SourceIp
        self.LoginType = LoginType
        self.SessionType = SessionType
        self.SessionSecurityLevel = SessionSecurityLevel
        self.LogoutUrl = LogoutUrl
        self.ParentId = ParentId
        self.LoginHistoryId = LoginHistoryId
        self.LoginGeoId = LoginGeoId
        self.IsCurrent = IsCurrent


