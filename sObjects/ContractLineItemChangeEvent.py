class ContractLineItemChangeEvent:

    def __init__(self, Id=None, ReplayId=None, ChangeEventHeader=None, LineItemNumber=None, CreatedDate=None, CreatedById=None, LastModifiedDate=None, LastModifiedById=None, ServiceContractId=None, AssetId=None, StartDate=None, EndDate=None, Description=None, PricebookEntryId=None, Quantity=None, UnitPrice=None, Discount=None, ParentContractLineItemId=None, RootContractLineItemId=None, LocationId=None):
        self.Id = Id
        self.ReplayId = ReplayId
        self.ChangeEventHeader = ChangeEventHeader
        self.LineItemNumber = LineItemNumber
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.LastModifiedDate = LastModifiedDate
        self.LastModifiedById = LastModifiedById
        self.ServiceContractId = ServiceContractId
        self.AssetId = AssetId
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Description = Description
        self.PricebookEntryId = PricebookEntryId
        self.Quantity = Quantity
        self.UnitPrice = UnitPrice
        self.Discount = Discount
        self.ParentContractLineItemId = ParentContractLineItemId
        self.RootContractLineItemId = RootContractLineItemId
        self.LocationId = LocationId


