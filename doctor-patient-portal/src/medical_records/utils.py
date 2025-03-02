from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm, mm
import os

def generate_prescription_pdf(health_record):
    """
    Generate a PDF prescription based on the PatientHealthDetails record.
    
    Args:
        health_record: A PatientHealthDetails instance
    
    Returns:
        BytesIO: A buffer containing the generated PDF
    """
    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()
    
    # Set up the PDF with A4 page size
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4  # Width and height of A4 page
    
    # Set up colors
    light_purple = colors.Color(0.85, 0.75, 0.95)
    dark_purple = colors.Color(0.5, 0.1, 0.5)
    
    p.setFillColor(light_purple)
    p.rect(0, height - 175, width, 175, fill=True)
    # Add clinic header with logo
    logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images', 'health-hero.png')
    p.drawImage(logo_path, 20, height - 75, width=50, height=50)
    p.setFillColorRGB(0.9, 0.3, 0.4)  # Pink color for clinic name
    p.setFont("Helvetica-Bold", 18)
    p.drawString(80, height - 55, "HEALTH AND")
    p.drawString(80, height - 75, "WELLNESS CLINIC")
    
    # Add doctor information
    p.setFillColorRGB(0.3, 0.3, 0.3)  # Dark gray for doctor name
    p.setFont("Helvetica-Bold", 16)
    p.drawString(350, height - 55, "Dr. Durgesh Makwana")
    p.setFont("Helvetica", 10)
    p.drawString(350, height - 70, "MBBS, DNB, FNB (Critical Care Medicine)")
    p.drawString(350, height - 85, "IDCCM, CCEBDM (Diabetes)")
    p.setFont("Helvetica-Bold", 12)
    p.drawString(350, height - 105, "Critical Care Physician and Diabetologist")
    p.setFont("Helvetica", 10)
    p.drawString(350, height - 120, "Reg. no: MMC 2009/03/0904")
    p.drawString(350, height - 135, "Senior ICU Consultant, Ruby Hall Clinic, Pune")
    
    # Add clinic address and contact
    p.setFont("Helvetica", 9)
    p.drawString(40, height - 104, "1st floor, Vandana Plaza, Opp Park Royale Society,")
    p.drawString(40, height - 120, "Rahatni, Pune. 411017")
    p.drawString(40, height - 135, "7387180485 / 7058071089   www.drdurgeshmakwana.com")
    p.drawString(40, height - 150, "Timing: Mon to Sat - 6pm to 9:30 pm (Sunday on appointment)")
    
    # Draw line to separate header from content
    p.setStrokeColorRGB(0.8, 0.8, 0.8)
    p.line(40, height - 175, width - 40, height - 175)
    
    # Add date and time - use appointment date if available
    appointment_date = ""
    if hasattr(health_record, 'appointment') and health_record.appointment:
        if hasattr(health_record.appointment, 'appointment_date'):
            appointment_date = health_record.appointment.appointment_date.strftime('%d-%m-%Y %I:%M %p')
    
    p.drawString(350, height - 190, "Date and Time:" + appointment_date)
    
    # Get patient data
    patient = health_record.patient
    
    # Add patient details
    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, height - 210, "Name: ")
    p.setFont("Helvetica", 10)
    patient_name = f"{patient.first_name} {patient.last_name}" if hasattr(patient, 'first_name') else "Patient Name"
    p.drawString(80, height - 210, patient_name)
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(350, height - 210, "Age: ")
    p.setFont("Helvetica", 10)
    p.drawString(380, height - 210, f"{getattr(patient, 'age', '')} years")
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(425, height - 210, "Sex: ")
    p.setFont("Helvetica", 10)
    gender = getattr(patient, 'gender', 'M/F/O')
    p.drawString(450, height - 210, gender)
    
    # Add patient measurements
    y_position = height - 235
    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, y_position, "Address: ")
    p.setFont("Helvetica", 10)
    
    # Wrap address into multiple lines
    address = getattr(patient, 'address', '')
    address_lines = wrap_text(address, 40)  # Wrap address with 40 chars per line
    for i, line in enumerate(address_lines):
        p.drawString(100, y_position - (i * 15), line)
    
    y_position = height - 235
    
    # Continue with measurements on the right side
    p.setFont("Helvetica-Bold", 10)
    p.drawString(350, y_position, "Wt: ")
    p.setFont("Helvetica", 10)
    weight = str(health_record.weight) if health_record.weight else ""
    p.drawString(370, y_position, f"{weight} Kg")
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(425, y_position, "Ht: ")
    p.setFont("Helvetica", 10)
    height_cm = str(health_record.height) if health_record.height else ""
    p.drawString(440, y_position, f"{height_cm} cm")

    p.setFont("Helvetica-Bold", 10)
    p.drawString(500, y_position, "BMI: ")
    p.setFont("Helvetica", 10)
    bmi = str(health_record.bmi) if health_record.bmi else ""
    p.drawString(530, y_position, f"{bmi} Kg/m2")

    # Add allergy, addiction, diet, sleep info
    
    y_position -= len(address_lines) * 15

    y_position -= 10

    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, y_position, "Allergy: ")
    p.setFont("Helvetica", 10)

    allergies = health_record.allergies or ""

    allergies_lines = wrap_text(allergies, 40)  # Wrap address with 40 chars per line
    for i, line in enumerate(allergies_lines):
        p.drawString(100, y_position - (i * 15), line)
    
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(260, y_position, "Addiction: ")
    p.setFont("Helvetica", 10)
    addictions = health_record.addictions or ""

    addictions_lines = wrap_text(addictions, 30)  # Wrap address with 40 chars per line
    for i, line in enumerate(addictions_lines):
        p.drawString(315, y_position - (i * 15), line)
    
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(420, y_position, "Diet: ")
    p.setFont("Helvetica", 10)
    diet_map = {'VEG': 'Veg', 'NON_VEG': 'Non-veg', 'VEGAN': 'Vegan', 'OTHER': 'Other'}
    diet = diet_map.get(health_record.diet, "") if health_record.diet else ""
    p.drawString(450, y_position, diet)
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(500, y_position, "Sleep: ")
    p.setFont("Helvetica", 10)
    sleep = str(health_record.sleep_hours) if health_record.sleep_hours else ""
    p.drawString(535, y_position, f"{sleep} hrs")
    
    # Add comorbidities
    y_position = height - 295
    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, y_position, "Comorbidity: ")
    p.setFont("Helvetica", 10)
    p.drawString(120, y_position, health_record.comorbidities or "")
    
    # Add vitals on the right side
    p.line(width - 150, y_position - 15, width - 150, y_position - 200)  # Vertical line for vitals section
    
    vitals_y = y_position - 15
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 130, vitals_y, "O/e,")
    vitals_y -= 20
    
    p.drawString(width - 130, vitals_y, "Temp: ")
    p.setFont("Helvetica", 10)
    temp = str(health_record.temperature) if health_record.temperature else ""
    p.drawString(width - 90, vitals_y, temp)
    vitals_y -= 20
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 130, vitals_y, "HR: ")
    p.setFont("Helvetica", 10)
    hr = str(health_record.heart_rate) if health_record.heart_rate else ""
    p.drawString(width - 105, vitals_y, f"{hr} /min")
    vitals_y -= 20
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 130, vitals_y, "BP: ")
    p.setFont("Helvetica", 10)
    bp = health_record.blood_pressure or ""
    p.drawString(width - 105, vitals_y, f"{bp} mmHg")
    vitals_y -= 20
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 130, vitals_y, "RR: ")
    p.setFont("Helvetica", 10)
    rr = str(health_record.rr) if health_record.rr else ""
    p.drawString(width - 105, vitals_y, f"{rr} /min")
    vitals_y -= 20
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 130, vitals_y, "SpO2: ")
    p.setFont("Helvetica", 10)
    spo2 = str(health_record.spo2) if health_record.spo2 else ""
    p.drawString(width - 95, vitals_y, f"{spo2} %")
    vitals_y -= 20
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 130, vitals_y, "RS: ")
    p.setFont("Helvetica", 10)
    p.drawString(width - 105, vitals_y, health_record.rs or "")
    vitals_y -= 20
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 130, vitals_y, "CVS: ")
    p.setFont("Helvetica", 10)
    p.drawString(width - 100, vitals_y, health_record.cvs or "")
    vitals_y -= 20
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 130, vitals_y, "P/A: ")
    p.setFont("Helvetica", 10)
    p.drawString(width - 105, vitals_y, health_record.p_a or "")
    vitals_y -= 20
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 130, vitals_y, "CNS: ")
    p.setFont("Helvetica", 10)
    p.drawString(width - 100, vitals_y, health_record.cns or "")
    
    # Add presenting complaints
    y_position -= 30
    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, y_position, "Presenting complaints:")
    y_position -= 15
    
    p.setFont("Helvetica", 10)
    complaints = health_record.presenting_complaints or ""
    # Wrap text if needed
    lines = wrap_text(complaints, 60)
    for line in lines:
        p.drawString(40, y_position, line)
        y_position -= 15
    
    # Add provisional diagnosis
    y_position -= 10
    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, y_position, "Provisional diagnosis:")
    y_position -= 15
    
    p.setFont("Helvetica", 10)
    diagnosis = health_record.provisional_diagnosis or ""
    lines = wrap_text(diagnosis, 60)
    for line in lines:
        p.drawString(40, y_position, line)
        y_position -= 15
    
    # Add prescription symbol
    y_position = vitals_y - 10
    p.setFont("Helvetica-Bold", 15)
    p.drawString(40, y_position, "Rx")
    y_position -= 20
    
    # Add medicine table
    medicine_details = health_record.medicine_details.all()
    
    # Table headers
    headers = ['Name of medicine', 'Dose', 'Morning', '', 'Afternoon', '', 'Night', '', 'Days']
    subheaders = ['', '', 'Before food', 'After food', 'Before food', 'After food', 'Before food', 'After food', '']
    
    # Table data
    data = [headers, subheaders]
    
    for med in medicine_details:
        medicine_name = med.medicine.name if hasattr(med.medicine, 'name') else ""
        row = [
            medicine_name,
            med.dosage,
            '✓' if med.morning_before_meal else '',
            '✓' if med.morning_after_meal else '',
            '✓' if med.afternoon_before_meal else '',
            '✓' if med.afternoon_after_meal else '',
            '✓' if med.night_before_meal else '',
            '✓' if med.night_after_meal else '',
            str(med.days)
        ]
        data.append(row)
    
    # Add empty rows if needed
    while len(data) < 9:  # Ensure at least 7 rows for medicines
        data.append(['', '', '', '', '', '', '', '', ''])
    
    # Create table
    col_widths = [110, 50, 55, 55, 55, 55, 55, 55, 40]
    table = Table(data, colWidths=col_widths)
    
    # Add table style
    table_style = TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey),
        ('BACKGROUND', (0, 0), (-1, 1), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('SPAN', (2, 0), (3, 0)),  # Merge "Morning" cells
        ('SPAN', (4, 0), (5, 0)),  # Merge "Afternoon" cells
        ('SPAN', (6, 0), (7, 0)),  # Merge "Night" cells
    ])
    table.setStyle(table_style)
    
    # Draw the table
    table.wrapOn(p, width, height)
    table.drawOn(p, 40, y_position - 150)
    
    # Set position for investigation advice
    y_position = y_position - 170
    
    # Add investigation advice
    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, y_position, "Investigation advised:")
    y_position -= 15
    
    p.setFont("Helvetica", 10)
    investigation = health_record.investigation_advice or ""
    lines = wrap_text(investigation, 80)
    for line in lines:
        p.drawString(40, y_position, line)
        y_position -= 15
    
    # Add diet advice
    y_position -= 10
    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, y_position, "Diet advise:")
    y_position -= 15
    
    p.setFont("Helvetica", 10)
    diet_advice = health_record.diet_advice or ""
    lines = wrap_text(diet_advice, 80)
    for line in lines:
        p.drawString(40, y_position, line)
        y_position -= 15
    
    # Add follow-up date
    y_position -= 10
    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, y_position, "Follow up date:")
    
    p.setFont("Helvetica", 10)
    follow_up = health_record.follow_up_date.strftime('%d-%m-%Y') if health_record.follow_up_date else ""
    p.drawString(130, y_position, follow_up)
    
    # Add doctor signature
    p.setFont("Helvetica-Bold", 10)
    p.drawString(450, y_position, "Doctor Signature:")
    
    # Add footer notes
    y_position -= 15
    p.setFont("Helvetica", 8)
    p.drawString(40, y_position, "Contact immediately if symptoms persists or worsens and visit nearest hospital.")
    y_position -= 10
    p.drawString(40, y_position, "Check for drug allergy and complications before consumption!")
    
    # Add clinic contact at the bottom
    y_position = 30
    p.setFont("Helvetica", 10)
    p.drawString(40, y_position, "drmakwanaclinic@gmail.com")
    p.drawString(350, y_position, "@dr_makwana_healthclinic")
    
    # Save the PDF
    p.showPage()
    p.save()
    
    # Get the value of the buffer
    pdf = buffer.getvalue()
    buffer.close()
    
    return pdf

def wrap_text(text, max_chars_per_line):
    """Wrap text to fit within specified character limit per line"""
    if not text:
        return []
        
    words = text.split()
    lines = []
    current_line = []
    current_chars = 0
    
    for word in words:
        if current_chars + len(word) + len(current_line) <= max_chars_per_line:
            current_line.append(word)
            current_chars += len(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_chars = len(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines