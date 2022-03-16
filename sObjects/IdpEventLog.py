class IdpEventLog:

    def __init__(self, Id=None, InitiatedBy=None, Timestamp=None, ErrorCode=None, SamlEntityUrl=None, UserId=None, AuthSessionId=None, SsoType=None, AppId=None, IdentityUsed=None, OptionsHasLogoutUrl=None):
        self.Id = Id
        self.InitiatedBy = InitiatedBy
        self.Timestamp = Timestamp
        self.ErrorCode = ErrorCode
        self.SamlEntityUrl = SamlEntityUrl
        self.UserId = UserId
        self.AuthSessionId = AuthSessionId
        self.SsoType = SsoType
        self.AppId = AppId
        self.IdentityUsed = IdentityUsed
        self.OptionsHasLogoutUrl = OptionsHasLogoutUrl


