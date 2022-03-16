class Note:

    def __init__(self, Id=None, IsDeleted=None, ParentId=None, Title=None, IsPrivate=None, Body=None, OwnerId=None, CreatedDate=None, CreatedById=None, LastModifiedDate=None, LastModifiedById=None, SystemModstamp=None):
        self.Id = Id
        self.IsDeleted = IsDeleted
        self.ParentId = ParentId
        self.Title = Title
        self.IsPrivate = IsPrivate
        self.Body = Body
        self.OwnerId = OwnerId
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.LastModifiedDate = LastModifiedDate
        self.LastModifiedById = LastModifiedById
        self.SystemModstamp = SystemModstamp


