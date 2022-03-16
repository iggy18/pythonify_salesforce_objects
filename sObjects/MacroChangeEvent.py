class MacroChangeEvent:

    def __init__(self, Id=None, ReplayId=None, ChangeEventHeader=None, OwnerId=None, Name=None, CreatedDate=None, CreatedById=None, LastModifiedDate=None, LastModifiedById=None, Description=None, IsAlohaSupported=None, IsLightningSupported=None, StartingContext=None):
        self.Id = Id
        self.ReplayId = ReplayId
        self.ChangeEventHeader = ChangeEventHeader
        self.OwnerId = OwnerId
        self.Name = Name
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.LastModifiedDate = LastModifiedDate
        self.LastModifiedById = LastModifiedById
        self.Description = Description
        self.IsAlohaSupported = IsAlohaSupported
        self.IsLightningSupported = IsLightningSupported
        self.StartingContext = StartingContext


