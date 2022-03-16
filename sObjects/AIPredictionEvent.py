class AIPredictionEvent:

    def __init__(self, ReplayId=None, CreatedDate=None, CreatedById=None, EventUuid=None, PredictionEntityId=None, InsightId=None, TargetId=None, Confidence=None, FieldName=None, HasError=None):
        self.ReplayId = ReplayId
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.EventUuid = EventUuid
        self.PredictionEntityId = PredictionEntityId
        self.InsightId = InsightId
        self.TargetId = TargetId
        self.Confidence = Confidence
        self.FieldName = FieldName
        self.HasError = HasError


