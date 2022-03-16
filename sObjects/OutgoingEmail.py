class OutgoingEmail:

    def __init__(self, Id=None, ExternalId=None, ValidatedFromAddress=None, ToAddress=None, CcAddress=None, BccAddress=None, Subject=None, TextBody=None, HtmlBody=None, RelatedToId=None, WhoId=None, EmailTemplateId=None, InReplyTo=None, References=None, MessageId=None):
        self.Id = Id
        self.ExternalId = ExternalId
        self.ValidatedFromAddress = ValidatedFromAddress
        self.ToAddress = ToAddress
        self.CcAddress = CcAddress
        self.BccAddress = BccAddress
        self.Subject = Subject
        self.TextBody = TextBody
        self.HtmlBody = HtmlBody
        self.RelatedToId = RelatedToId
        self.WhoId = WhoId
        self.EmailTemplateId = EmailTemplateId
        self.InReplyTo = InReplyTo
        self.References = References
        self.MessageId = MessageId


