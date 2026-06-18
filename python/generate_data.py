#!/usr/bin/env python3
"""
Healthcare Commercial Analytics Platform - Synthetic Data Generator
Generates realistic healthcare commercial data files including:
- Prescribers (NPI registry)
- Prescriptions (TRx/NRx transaction details)
- Medical Claims (diagnoses, procedures, costs)
- CRM Interactions (Sales Rep detailing calls to physicians)
"""

import os
import csv
import random
from datetime import datetime, timedelta

# Configuration
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw')
RANDOM_SEED = 42

# Sample Data Elements
SPECIALTIES = [
    'Cardiology', 'Endocrinology', 'Oncology', 'Primary Care', 
    'Rheumatology', 'Neurology', 'Gastroenterology', 'Dermatology'
]

STATES = ['NY', 'CA', 'TX', 'FL', 'PA', 'IL', 'OH', 'GA', 'NC', 'MI']

DRUGS = [
    # {'brand': 'BrandName', 'generic': 'GenericName', 'therapeutic_class': 'Class', 'wac_per_unit': Price}
    {'brand': 'Januvia', 'generic': 'sitagliptin', 'class': 'Diabetes', 'wac_per_unit': 16.50},
    {'brand': 'Lipitor', 'generic': 'atorvastatin', 'class': 'Cardiology', 'wac_per_unit': 1.80},
    {'brand': 'Humira', 'generic': 'adalimumab', 'class': 'Immunology', 'wac_per_unit': 2750.00},
    {'brand': 'Keytruda', 'generic': 'pembrolizumab', 'class': 'Oncology', 'wac_per_unit': 9800.00},
    {'brand': 'Eliquis', 'generic': 'apixaban', 'class': 'Cardiology', 'wac_per_unit': 14.20},
    {'brand': 'Synthroid', 'generic': 'levothyroxine', 'class': 'Endocrinology', 'wac_per_unit': 1.10},
    {'brand': 'Jardiance', 'generic': 'empagliflozin', 'class': 'Diabetes', 'wac_per_unit': 19.80},
    {'brand': 'Stelara', 'generic': 'ustekinumab', 'class': 'Immunology', 'wac_per_unit': 8200.00}
]

ICD10_CODES = [
    {'code': 'I10', 'desc': 'Essential (primary) hypertension'},
    {'code': 'E11.9', 'desc': 'Type 2 diabetes mellitus without complications'},
    {'code': 'E78.5', 'desc': 'Hyperlipidemia, unspecified'},
    {'code': 'M81.0', 'desc': 'Senile osteoporosis without current pathological fracture'},
    {'code': 'M06.9', 'desc': 'Rheumatoid arthritis, unspecified'},
    {'code': 'C50.919', 'desc': 'Malignant neoplasm of unspecified site of unspecified female breast'},
    {'code': 'G30.9', 'desc': 'Alzheimers disease, unspecified'},
    {'code': 'K50.90', 'desc': 'Crohns disease, unspecified, without complications'}
]

CPT_CODES = [
    {'code': '99213', 'desc': 'Outpatient office visit, 15 minutes'},
    {'code': '99214', 'desc': 'Outpatient office visit, 25 minutes'},
    {'code': '99204', 'desc': 'New patient office visit, 45 minutes'},
    {'code': '93000', 'desc': 'Electrocardiogram (ECG) report'},
    {'code': '36415', 'desc': 'Collection of venous blood (venipuncture)'},
    {'code': '96413', 'desc': 'Chemotherapy administration, intravenous infusion; up to 1 hour'}
]

FIRST_NAMES = ['John', 'Mary', 'Robert', 'Patricia', 'James', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica']
LAST_NAMES = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas']

REPS = [
    {'rep_id': 'REP001', 'name': 'Alice Carter', 'region': 'East'},
    {'rep_id': 'REP002', 'name': 'Bob Mendez', 'region': 'West'},
    {'rep_id': 'REP003', 'name': 'Charlie Vance', 'region': 'South'},
    {'rep_id': 'REP004', 'name': 'Diana Prince', 'region': 'Midwest'},
    {'rep_id': 'REP005', 'name': 'Ethan Hunt', 'region': 'Northeast'}
]

def generate_prescribers(count=200):
    """Generates synthetic prescribers with NPI numbers."""
    prescribers = []
    # Seed for NPI generation (10-digit standard starting with 18)
    npi_start = 1800000001
    
    for i in range(count):
        npi = str(npi_start + i)
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        specialty = random.choice(SPECIALTIES)
        state = random.choice(STATES)
        zip_code = f"{random.randint(10000, 99999)}"
        
        prescribers.append({
            'npi': npi,
            'first_name': first_name,
            'last_name': last_name,
            'specialty': specialty,
            'state': state,
            'zip_code': zip_code
        })
    return prescribers

def generate_prescriptions(prescribers, count=5000):
    """Generates synthetic prescription records linked to prescribers."""
    prescriptions = []
    start_date = datetime(2025, 1, 1)
    
    for i in range(count):
        rx_id = f"RX{1000000 + i}"
        prescriber = random.choice(prescribers)
        patient_id = f"PAT{random.randint(10000, 25000)}"
        drug = random.choice(DRUGS)
        
        # Prescription dates staggered over 1 year
        days_offset = random.randint(0, 364)
        rx_date = (start_date + timedelta(days=days_offset)).strftime('%Y-%m-%d')
        
        # Determine quantity and refills based on drug type
        if drug['class'] in ['Oncology', 'Immunology']:
            quantity = random.randint(1, 4)
            refills = random.randint(0, 2)
        else:
            quantity = random.choice([30, 90])
            refills = random.randint(0, 5)
            
        unit_wac = drug['wac_per_unit']
        total_wac = round(quantity * unit_wac, 2)
        
        # Copay and insurance variables
        copay = round(random.choice([0.00, 5.00, 10.00, 20.00, 50.00, 150.00]), 2)
        payer_type = random.choice(['Commercial', 'Medicare', 'Medicaid', 'Cash'])
        
        prescriptions.append({
            'prescription_id': rx_id,
            'npi': prescriber['npi'],
            'patient_id': patient_id,
            'rx_date': rx_date,
            'drug_brand': drug['brand'],
            'drug_generic': drug['generic'],
            'therapeutic_class': drug['class'],
            'quantity': quantity,
            'refills': refills,
            'total_wac': total_wac,
            'copay': copay,
            'payer_type': payer_type
        })
    return prescriptions

def generate_claims(count=3000):
    """Generates synthetic medical claims."""
    claims = []
    start_date = datetime(2025, 1, 1)
    
    for i in range(count):
        claim_id = f"CLM{2000000 + i}"
        patient_id = f"PAT{random.randint(10000, 25000)}"
        provider_npi = f"{random.randint(1900000000, 1999999999)}"
        
        days_offset = random.randint(0, 364)
        service_date = (start_date + timedelta(days=days_offset)).strftime('%Y-%m-%d')
        
        diag = random.choice(ICD10_CODES)
        proc = random.choice(CPT_CODES)
        
        # Costs
        allowed_amount = round(random.uniform(50.00, 1500.00), 2)
        # Paid is always <= allowed
        paid_amount = round(allowed_amount * random.uniform(0.6, 1.0), 2)
        
        claims.append({
            'claim_id': claim_id,
            'patient_id': patient_id,
            'provider_npi': provider_npi,
            'service_date': service_date,
            'diagnosis_code': diag['code'],
            'diagnosis_desc': diag['desc'],
            'procedure_code': proc['code'],
            'procedure_desc': proc['desc'],
            'allowed_amount': allowed_amount,
            'paid_amount': paid_amount
        })
    return claims

def generate_crm_calls(prescribers, count=1000):
    """Generates CRM activity logs representing Sales Representative interactions."""
    calls = []
    start_date = datetime(2025, 1, 1)
    topics = ['Efficacy Profile', 'Safety & Tolerability', 'Co-pay Assistance Program', 'Clinical Trials Data', 'Market Access & Formulary Update']
    call_methods = ['In-Person', 'Virtual Video', 'Phone Call', 'Email Follow-up']
    
    for i in range(count):
        call_id = f"CALL{3000000 + i}"
        rep = random.choice(REPS)
        prescriber = random.choice(prescribers)
        
        days_offset = random.randint(0, 364)
        call_date = (start_date + timedelta(days=days_offset)).strftime('%Y-%m-%d')
        
        call_type = random.choice(call_methods)
        detailing_topic = random.choice(topics)
        
        # Sample interaction outcome/rating
        outcome = random.choice(['High Interest', 'Favorable', 'Neutral', 'Busy - Left Materials', 'Unfavorable'])
        
        calls.append({
            'call_id': call_id,
            'rep_id': rep['rep_id'],
            'rep_name': rep['name'],
            'rep_region': rep['region'],
            'npi': prescriber['npi'],
            'call_date': call_date,
            'call_type': call_type,
            'detailing_topic': detailing_topic,
            'outcome': outcome
        })
    return calls

def save_to_csv(data, filename, fieldnames):
    """Utility function to save generated dictionary data into CSV formats."""
    filepath = os.path.join(RAW_DATA_DIR, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Successfully generated: {filepath} ({len(data)} records)")

def main():
    print("Initialising Synthetic Data Generation...")
    random.seed(RANDOM_SEED)
    
    # 1. Generate Prescribers (NPI Directory)
    prescribers = generate_prescribers(250)
    save_to_csv(
        prescribers, 
        'raw_prescribers.csv', 
        ['npi', 'first_name', 'last_name', 'specialty', 'state', 'zip_code']
    )
    
    # 2. Generate Prescriptions
    prescriptions = generate_prescriptions(prescribers, 6000)
    save_to_csv(
        prescriptions,
        'raw_prescriptions.csv',
        ['prescription_id', 'npi', 'patient_id', 'rx_date', 'drug_brand', 'drug_generic', 
         'therapeutic_class', 'quantity', 'refills', 'total_wac', 'copay', 'payer_type']
    )
    
    # 3. Generate Claims
    claims = generate_claims(4000)
    save_to_csv(
        claims,
        'raw_claims.csv',
        ['claim_id', 'patient_id', 'provider_npi', 'service_date', 'diagnosis_code', 
         'diagnosis_desc', 'procedure_code', 'procedure_desc', 'allowed_amount', 'paid_amount']
    )
    
    # 4. Generate CRM Calls
    crm_calls = generate_crm_calls(prescribers, 1500)
    save_to_csv(
        crm_calls,
        'raw_crm_calls.csv',
        ['call_id', 'rep_id', 'rep_name', 'rep_region', 'npi', 'call_date', 'call_type', 'detailing_topic', 'outcome']
    )
    
    print("\nData generation complete! All files saved in 'data/raw/'.")

if __name__ == '__main__':
    main()
