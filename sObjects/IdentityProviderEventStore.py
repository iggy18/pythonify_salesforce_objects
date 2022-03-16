class IdentityProviderEventStore:

    def __init__(self, Id=None, CreatedDate=None, EventIdentifier=None, UserId=None, EventDate=None, IdentityUsed=None, SamlEntityUrl=None, InitiatedBy=None, ErrorCode=None, SsoType=None, AuthSessionId=None, AppId=None, HasLogoutUrl=None):
        self.Id = Id
        self.CreatedDate = CreatedDate
        self.EventIdentifier = EventIdentifier
        self.UserId = UserId
        self.EventDate = EventDate
        self.IdentityUsed = IdentityUsed
        self.SamlEntityUrl = SamlEntityUrl
        self.InitiatedBy = InitiatedBy
        self.ErrorCode = ErrorCode
        self.SsoType = SsoType
        self.AuthSessionId = AuthSessionId
        self.AppId = AppId
        self.HasLogoutUrl = HasLogoutUrl


