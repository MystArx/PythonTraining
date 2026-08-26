patients = [
    {
        "PatientId": 101,
        "PatientName": "Aman Verma",
        "Age": 35,
        "City": "Noida",
        "Visits": [
            {
                "VisitId": 1,
                "DoctorName": "Dr. Mehta",
                "Department": "Cardiology",
                "ConsultationFee": 1200,
                "MedicinesCost": 800,
                "Status": "Completed"
            },
            {
                "VisitId": 2,
                "DoctorName": "Dr. Sharma",
                "Department": "General Medicine",
                "ConsultationFee": 700,
                "MedicinesCost": 500,
                "Status": "Pending"
            }
        ]
    },
    {
        "PatientId": 102,
        "PatientName": "Riya Singh",
        "Age": 28,
        "City": "Delhi",
        "Visits": [
            {
                "VisitId": 1,
                "DoctorName": "Dr. Kapoor",
                "Department": "Orthopaedics",
                "ConsultationFee": 1000,
                "MedicinesCost": 650,
                "Status": "Completed"
            }
        ]
    }
]

SearchPatientByID = lambda pid, p_list: next((p for p in p_list if p["PatientId"] == pid), None)
SearchVisitByID = lambda vid, v_list: next((v for v in v_list if v["VisitId"] == vid), None)

def addPatient():
    pid = int(input("Enter Patient ID : "))
    if SearchPatientByID(pid, patients) != None:
        print("Patient ID already exists.")
        return
    name = input("Enter Patient Name : ")
    age = int(input("Enter Age : "))
    if age <= 0:
        print("Age must be greater than zero.")
        return
    city = input("Enter City : ")
    
    new_patient = {
        "PatientId": pid,
        "PatientName": name,
        "Age": age,
        "City": city,
        "Visits": []
    }
    patients.append(new_patient)
    print("Patient added successfully.")

def addVisit():
    pid = int(input("Enter Patient ID : "))
    p = SearchPatientByID(pid, patients)
    if p == None:
        print("Patient not found.")
        return
    
    vid = int(input("Enter Visit ID : "))
    if SearchVisitByID(vid, p["Visits"]) != None:
        print("Visit ID already exists for this patient.")
        return
    
    doc = input("Enter Doctor Name : ")
    dept = input("Enter Department : ")
    fee = float(input("Enter Consultation Fee : "))
    if fee < 0:
        print("Consultation fee cannot be negative.")
        return
    med_cost = float(input("Enter Medicines Cost : "))
    if med_cost < 0:
        print("Medicines cost cannot be negative.")
        return
    status = input("Enter Visit Status (Scheduled/Pending/Completed/Cancelled) : ")
    
    visit = {
        "VisitId": vid,
        "DoctorName": doc,
        "Department": dept,
        "ConsultationFee": fee,
        "MedicinesCost": med_cost,
        "Status": status
    }
    p["Visits"].append(visit)
    print("Medical visit added successfully.")

def displayPatientDetails(p):
    print(f"Patient ID   : {p['PatientId']}")
    print(f"Patient Name : {p['PatientName']}")
    print(f"Age          : {p['Age']}")
    print(f"City         : {p['City']}")
    if len(p["Visits"]) == 0:
        print("Visits       : No medical visits.")
    else:
        print("Visits:")
        for v in p["Visits"]:
            print(f"  Visit ID          : {v['VisitId']}")
            print(f"  Doctor Name       : {v['DoctorName']}")
            print(f"  Department        : {v['Department']}")
            print(f"  Consultation Fee  : {v['ConsultationFee']}")
            print(f"  Medicines Cost    : {v['MedicinesCost']}")
            print(f"  Status            : {v['Status']}")

def viewAllPatients():
    if len(patients) == 0:
        print("No patient records found.")
    else:
        for p in patients:
            displayPatientDetails(p)
            print("----------------------------------------")

def searchPatient():
    pid = int(input("Enter Patient ID : "))
    p = SearchPatientByID(pid, patients)
    if p != None:
        print(f"Patient details found.")
        print(f"Total number of visits : {len(p['Visits'])}")
        displayPatientDetails(p)
    else:
        print("Patient not found.")

def updateVisitStatus():
    pid = int(input("Enter Patient ID : "))
    p = SearchPatientByID(pid, patients)
    if p == None:
        print("Patient not found.")
        return
    vid = int(input("Enter Visit ID : "))
    v = SearchVisitByID(vid, p["Visits"])
    if v != None:
        new_status = input("Enter New Status (Scheduled/Pending/Completed/Cancelled) : ")
        v["Status"] = new_status
        print("Visit status updated successfully.")
    else:
        print("Visit not found.")

def calculateMedicalBill():
    pid = int(input("Enter Patient ID : "))
    p = SearchPatientByID(pid, patients)
    if p == None:
        print("Patient not found.")
        return
    if len(p["Visits"]) == 0:
        print("No visits found for this patient.")
        return
    
    total_bill = 0
    for idx, v in enumerate(p["Visits"], start=1):
        v_bill = v["ConsultationFee"] + v["MedicinesCost"]
        total_bill += v_bill
        print(f"Visit {idx} Bill : ₹{v_bill:.2f}")
    print("-----------------------")
    print(f"Total Bill   : ₹{total_bill:.2f}")

def displayMultipleVisitsPatients():
    print("\nPatients with more than 2 visits:")
    count = 0
    for p in patients:
        if len(p["Visits"]) > 2:
            print(f"Patient ID       : {p['PatientId']}")
            print(f"Patient Name     : {p['PatientName']}")
            print(f"Number of Visits : {len(p['Visits'])}")
            count += 1
    if count == 0:
        print("No patients found with more than 2 visits.")

def displayDepartmentVisitCount():
    dept_counts = {}
    for p in patients:
        for v in p["Visits"]:
            dept = v["Department"]
            dept_counts[dept] = dept_counts.get(dept, 0) + 1
            
    if len(dept_counts) == 0:
        print("No visit records found.")
    else:
        print("\nDepartment-wise Visit Count:")
        for dept, count in dept_counts.items():
            print(f"{dept:<18} : {count}")

def findHighestBillPatient():
    if len(patients) == 0:
        print("No patients available.")
        return
    
    highest_p = None
    max_bill = -1
    for p in patients:
        p_total = sum(v["ConsultationFee"] + v["MedicinesCost"] for v in p["Visits"])
        if p_total > max_bill:
            max_bill = p_total
            highest_p = p
            
    if highest_p != None:
        print("\nPatient with Highest Medical Bill:")
        print(f"Patient ID   : {highest_p['PatientId']}")
        print(f"Patient Name : {highest_p['PatientName']}")
        print(f"Total Bill   : {max_bill:.2f}")

def removeVisit():
    pid = int(input("Enter Patient ID : "))
    p = SearchPatientByID(pid, patients)
    if p == None:
        print("Patient not found.")
        return
    vid = int(input("Enter Visit ID : "))
    v = SearchVisitByID(vid, p["Visits"])
    if v != None:
        p["Visits"].remove(v)
        print("Visit record removed successfully.")
    else:
        print("Visit not found.")

def main():
    while True:
        print("\n========== Hospital Patient Management System ==========")
        print("1. Add a New Patient")
        print("2. Add a Medical Visit")
        print("3. View All Patients")
        print("4. Search Patient by ID")
        print("5. Update Visit Status")
        print("6. Calculate Total Medical Bill")
        print("7. Display Patients with Multiple Visits")
        print("8. Display Department-wise Visit Count")
        print("9. Find the Patient with the Highest Medical Bill")
        print("10. Remove a Visit Record")
        print("11. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            addPatient()
        elif ch == 2:
            addVisit()
        elif ch == 3:
            viewAllPatients()
        elif ch == 4:
            searchPatient()
        elif ch == 5:
            updateVisitStatus()
        elif ch == 6:
            calculateMedicalBill()
        elif ch == 7:
            displayMultipleVisitsPatients()
        elif ch == 8:
            displayDepartmentVisitCount()
        elif ch == 9:
            findHighestBillPatient()
        elif ch == 10:
            removeVisit()
        elif ch == 11:
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()