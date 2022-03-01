import PatientClass as pc
import ProcedureClass as pcd

veteran_rate = 0.4
patient1 = pc.Patient(1, 'Matt Jones', '123 Main st, Waco TX 76706', '254-555-7415', True)
visit1 = pcd.Proceudre('Physical Exam', '2/15/2022', 'Dr.Irvine', 250, 1)
visit2 = pcd.Proceudre('MRI', '2/15/2022', 'Dr. Hamilton', 1500, 1)
visit3 = pcd.Proceudre('CT Scan', '2/17/2022', 'Dr.Drey', 1200, 2)
procedure_list = [visit1, visit2, visit3]

total_charges = visit1.get_charges() + visit2.get_charges()

print('***Patient Bill***')
print('Name: ', patient1.get_name())
print('Address: ', patient1.get_name())
print('Phone: ', patient1.get_phone())

n = 0
total = 0

for n in procedure_list:
    if procedure_list[n].get_PatientID == patient1.get_PatientID():
        print('Procedure: ', procedure_list[n].get_procedure())
        print('Date: ',  procedure_list[n].get_date())
        print('Practitioner: ', procedure_list[n].get_name_prac())
        print('Charge: ' + '$' + format(float(procedure_list[n].get_charges()), ',.2f'))
        total += procedure_list[n].get_charges()
        n += 1

    
if patient1.get_v_status() == True:
    total *= (1-veteran_rate)

print('\nTotal Charges: ' + '$' + format(total, ',.2f'))





