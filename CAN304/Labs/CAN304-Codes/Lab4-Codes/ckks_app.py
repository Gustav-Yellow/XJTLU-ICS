# --- CAN304 Lab  -----------------------------------------------------
# Lab 4: CKKS Fully Homomorphic Encryption
#
# CKKS Application
# Secure Average Age Computation
#
# By Jie Zhang <Jie.Zhang01@xjtlu.edu.cn>
#
# ----------------------------------------------------------------------



import tenseal as ts
import numpy as np
import random

def secure_healthcare_demo():
    print("\nCKKS Application: Secure Average Age Computation")

    
    # 1. Setup CKKS context with required keys
    print("\n1. Setting up encryption system...")
    ctx = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60]
    )
    ctx.global_scale = 2**40
    
    # Generate necessary keys
    ctx.generate_galois_keys()  # Required for .sum() operation
    print("✓ Encryption system ready (Galois keys generated)")
    
    # 2. Simulate hospitals with DIFFERENT patient counts
    print("\n2. Simulating hospital data (realistic scenario):")
    hospital_sizes = [26, 21, 30]  # Different sizes for each hospital
    hospital_data = []
    
    for i, size in enumerate(hospital_sizes):
        # Generate random patient ages (20-80 years)
        ages = [random.randint(20, 80) for _ in range(size)]
        hospital_data.append(ages)
        
        # Display hospital statistics
        total = sum(ages)
        avg = total / size
        print(f"   Hospital {i+1}: {size} patients")
        print(f"     • Total age: {total}")
        print(f"     • Average age: {avg:.1f}")
    
    # 3. Each hospital processes data locally
    print("\n3. Local processing at each hospital:")
    encrypted_sums = []
    
    for i, (ages, size) in enumerate(zip(hospital_data, hospital_sizes)):
        # Step 1: Hospital encrypts patient data
        encrypted_ages = ts.ckks_vector(ctx, ages)
        print(f"   Hospital {i+1}: ✓ Encrypted {size} patient records")
        
        # Step 2: Hospital computes sum on encrypted data
        encrypted_sum = encrypted_ages.sum()
        encrypted_sums.append(encrypted_sum)
        print(f"          → Computed encrypted sum")
    
    # 4. Secure aggregation (researcher's perspective)
    print("\n4. Secure aggregation of hospital sums:")
    print("   Researcher receives only encrypted sums")
    
    # Add all encrypted sums together
    total_encrypted_sum = encrypted_sums[0].copy()
    for i, enc_sum in enumerate(encrypted_sums[1:], 1):
        total_encrypted_sum = total_encrypted_sum + enc_sum
        print(f"   Added Hospital {i+1}'s encrypted sum")
    
    # Decrypt ONLY the final total
    final_total = total_encrypted_sum.decrypt()[0]
    total_patients = sum(hospital_sizes)
    average_age = final_total / total_patients
    
    print(f"\n   Final results after decryption:")
    print(f"   • Total patients: {total_patients}")
    print(f"   • Total age sum: {final_total:.1f}")
    print(f"   • Average age: {average_age:.1f}")
    
    # 5. Verification with plaintext computation
    print("\n5. Verification (plaintext comparison):")
    
    # Compute plaintext results
    all_ages = []
    for ages in hospital_data:
        all_ages.extend(ages)
    
    plaintext_total = sum(all_ages)
    plaintext_avg = plaintext_total / len(all_ages)
    
    print(f"   Plaintext calculation:")
    print(f"   • Total patients: {len(all_ages)}")
    print(f"   • Total age sum: {plaintext_total}")
    print(f"   • Average age: {plaintext_avg:.1f}")
    
    # Calculate accuracy
    total_error = abs(final_total - plaintext_total)
    avg_error = abs(average_age - plaintext_avg)
    
    print(f"\n   Accuracy check:")
    print(f"   • Total sum error: {total_error:.3f} years")
    print(f"   • Average age error: {avg_error:.3f} years")
    print(f"   • Error percentage: {(avg_error/plaintext_avg)*100:.2f}%")
    


if __name__ == "__main__":
    secure_healthcare_demo()
