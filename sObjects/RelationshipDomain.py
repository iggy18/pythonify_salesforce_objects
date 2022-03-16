class RelationshipDomain:

    def __init__(self, Id=None, DurableId=None, ParentSobjectId=None, ChildSobjectId=None, FieldId=None, RelationshipInfoId=None, RelationshipName=None, IsCascadeDelete=None, IsDeprecatedAndHidden=None, IsRestrictedDelete=None, JunctionIdListNames=None):
        self.Id = Id
        self.DurableId = DurableId
        self.ParentSobjectId = ParentSobjectId
        self.ChildSobjectId = ChildSobjectId
        self.FieldId = FieldId
        self.RelationshipInfoId = RelationshipInfoId
        self.RelationshipName = RelationshipName
        self.IsCascadeDelete = IsCascadeDelete
        self.IsDeprecatedAndHidden = IsDeprecatedAndHidden
        self.IsRestrictedDelete = IsRestrictedDelete
        self.JunctionIdListNames = JunctionIdListNames


