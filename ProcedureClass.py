class Proceudre: 

    def __init__(self, procedure, date, name_prac, charges, ID):
        self.__procedure = procedure
        self.__date = date
        self.__name_prac = name_prac
        self.__charges = charges
        self.__PatientID  = ID

    def set_procedure(self, procedure):
        self.__procedure = procedure

    def set_date(self, date):
        self.__date = date

    def set_name_prac(self, name_prac):
        self.__name_prac = name_prac

    def set_charges(self, charges):
        self.__charges = charges
    
    def set_PatientID(self, ID):
        self.__PatientID = ID

    def get_procedure(self):
        return self.__procedure

    def get_date(self):
        return self.__date

    def get_name_prac(self):
        return self.__name_prac

    def get_charges(self):
        return self.__charges
    
    def get_PatientID(self):
        return self.__PatientID


