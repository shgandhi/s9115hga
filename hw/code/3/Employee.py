class Employee():
    """Represents an employee.
    
    Attributes:
      emp_name: Name of the employee
      emp_age: Age of the employee
    """
    
    def __init__(self, emp_name, emp_age):
        self.emp_name = emp_name
        self.emp_age = emp_age
        
    def __repr__(self):
        """Returns machine readable string representation"""
        return "\nEmployee %s has age %d" % (self.emp_name, self.emp_age)
        
    def __lt__(self, other):
        """Sorts the employees in ascending order of their age"""
        return other.emp_age > self.emp_age
        
if __name__ == '__main__':
    employee = [ Employee('George Costanza', 54),\
    Employee('Jerry Seinfeld', 52),\
    Employee('Elaine Banes', 50),\
    Employee('Cosmo Kramer', 60)]
    print sorted(employee)