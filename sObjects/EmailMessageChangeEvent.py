class EmailMessageChangeEvent:

    def __init__(self, Id=None, ReplayId=None, ChangeEventHeader=None, ParentId=None, ActivityId=None, CreatedById=None, CreatedDate=None, LastModifiedDate=None, LastModifiedById=None, TextBody=None, HtmlBody=None, Headers=None, Subject=None, FromName=None, FromAddress=None, ToAddress=None, CcAddress=None, BccAddress=None, Incoming=None, HasAttachment=None, Status=None, MessageDate=None, ReplyToEmailMessageId=None, IsExternallyVisible=None, MessageIdentifier=None, ThreadIdentifier=None, IsClientManaged=None, RelatedToId=None, IsTracked=None, FirstOpenedDate=None, LastOpenedDate=None, IsBounced=None, EmailTemplateId=None):
        self.Id = Id
        self.ReplayId = ReplayId
        self.ChangeEventHeader = ChangeEventHeader
        self.ParentId = ParentId
        self.ActivityId = ActivityId
        self.CreatedById = CreatedById
        self.CreatedDate = CreatedDate
        self.LastModifiedDate = LastModifiedDate
        self.LastModifiedById = LastModifiedById
        self.TextBody = TextBody
        self.HtmlBody = HtmlBody
        self.Headers = Headers
        self.Subject = Subject
        self.FromName = FromName
        self.FromAddress = FromAddress
        self.ToAddress = ToAddress
        self.CcAddress = CcAddress
        self.BccAddress = BccAddress
        self.Incoming = Incoming
        self.HasAttachment = HasAttachment
        self.Status = Status
        self.MessageDate = MessageDate
        self.ReplyToEmailMessageId = ReplyToEmailMessageId
        self.IsExternallyVisible = IsExternallyVisible
        self.MessageIdentifier = MessageIdentifier
        self.ThreadIdentifier = ThreadIdentifier
        self.IsClientManaged = IsClientManaged
        self.RelatedToId = RelatedToId
        self.IsTracked = IsTracked
        self.FirstOpenedDate = FirstOpenedDate
        self.LastOpenedDate = LastOpenedDate
        self.IsBounced = IsBounced
        self.EmailTemplateId = EmailTemplateId


