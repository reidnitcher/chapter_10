class Patient:
    def __init__(self, ID, name, address, phone, v_status):
        self.__PatientID = ID
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__v_status = v_status

    def set_PatientID(self, ID):
        self.__PatientID = ID

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_v_status(self, v_status):
        self.__v_status = v_status

    def get_PatientID(self):
        return self.__PatientID

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
    
    def get_v_status(self):
        return self.__v_status