class UserRecordAccess:

    def __init__(self, Id=None, UserId=None, RecordId=None, HasReadAccess=None, HasEditAccess=None, HasDeleteAccess=None, HasTransferAccess=None, HasAllAccess=None, MaxAccessLevel=None):
        self.Id = Id
        self.UserId = UserId
        self.RecordId = RecordId
        self.HasReadAccess = HasReadAccess
        self.HasEditAccess = HasEditAccess
        self.HasDeleteAccess = HasDeleteAccess
        self.HasTransferAccess = HasTransferAccess
        self.HasAllAccess = HasAllAccess
        self.MaxAccessLevel = MaxAccessLevel


