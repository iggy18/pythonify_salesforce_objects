class BatchDataSource:

    def __init__(self, Id=None, IsDeleted=None, CreatedDate=None, CreatedById=None, LastModifiedDate=None, LastModifiedById=None, SystemModstamp=None, BatchJobDefinitionId=None, SourceTableName=None, CriteriaJoinCondition=None, CriteriaJoinType=None):
        self.Id = Id
        self.IsDeleted = IsDeleted
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.LastModifiedDate = LastModifiedDate
        self.LastModifiedById = LastModifiedById
        self.SystemModstamp = SystemModstamp
        self.BatchJobDefinitionId = BatchJobDefinitionId
        self.SourceTableName = SourceTableName
        self.CriteriaJoinCondition = CriteriaJoinCondition
        self.CriteriaJoinType = CriteriaJoinType


