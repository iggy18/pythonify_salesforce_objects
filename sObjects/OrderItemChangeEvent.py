class OrderItemChangeEvent:

    def __init__(self, Id=None, ReplayId=None, ChangeEventHeader=None, OrderId=None, PricebookEntryId=None, OriginalOrderItemId=None, AvailableQuantity=None, Quantity=None, UnitPrice=None, ListPrice=None, ServiceDate=None, EndDate=None, Description=None, CreatedDate=None, CreatedById=None, LastModifiedDate=None, LastModifiedById=None, OrderItemNumber=None):
        self.Id = Id
        self.ReplayId = ReplayId
        self.ChangeEventHeader = ChangeEventHeader
        self.OrderId = OrderId
        self.PricebookEntryId = PricebookEntryId
        self.OriginalOrderItemId = OriginalOrderItemId
        self.AvailableQuantity = AvailableQuantity
        self.Quantity = Quantity
        self.UnitPrice = UnitPrice
        self.ListPrice = ListPrice
        self.ServiceDate = ServiceDate
        self.EndDate = EndDate
        self.Description = Description
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.LastModifiedDate = LastModifiedDate
        self.LastModifiedById = LastModifiedById
        self.OrderItemNumber = OrderItemNumber


