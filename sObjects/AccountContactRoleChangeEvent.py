class AccountContactRoleChangeEvent:

    def __init__(self, Id=None, ReplayId=None, ChangeEventHeader=None, CreatedDate=None, CreatedById=None, LastModifiedDate=None, LastModifiedById=None, AccountId=None, ContactId=None, Role=None, IsPrimary=None):
        self.Id = Id
        self.ReplayId = ReplayId
        self.ChangeEventHeader = ChangeEventHeader
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.LastModifiedDate = LastModifiedDate
        self.LastModifiedById = LastModifiedById
        self.AccountId = AccountId
        self.ContactId = ContactId
        self.Role = Role
        self.IsPrimary = IsPrimary


