
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{'id': 1, 'first_name': 'John', 'last_name': self.last_name ,'age': 33, 'lucky_number': [7, 13, 22]},
                         {'id': self._generateId(), 'first_name': 'Jane', 'last_name': self.last_name,  'age': 35, 'lucky_number': [10, 14, 32]},
                         {'id': self._generateId(), 'first_name': 'Jimmy', 'last_name': self.last_name,  'age': 5, 'lucky_number': [1]}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member['id'] = self._generateId()
        member['last_name'] = self.last_name
        self._members.append(member)
        return

    def delete_member(self, id):
        self._members = [item for item in self._members if item['id'] != id]
        # fill this method and update the return
        return self._members

    def get_member(self, id):
        member = [row for row in self._members if row['id'] == id]
        # fill this method and update the return
        pass
    
    def get_last_name(self):
        return self.last_name

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
