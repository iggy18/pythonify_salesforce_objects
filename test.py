from sObjects.Todo__c import Todo__c

def test_contact():
    todo = Todo__c()
    todo.message = 'test'
    todo.status = "In Progress"