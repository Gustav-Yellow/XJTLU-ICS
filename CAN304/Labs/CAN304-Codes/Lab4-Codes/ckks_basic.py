# --- CAN304 Lab  -----------------------------------------------------
# Lab 4: CKKS Fully Homomorphic Encryption
#
# Additive and Multiplicative Homomorphism
# Run this to observe additive and multiplicative homomorphism
#
# By Jie Zhang <Jie.Zhang01@xjtlu.edu.cn>
#
# ----------------------------------------------------------------------


import tenseal as ts
import numpy as np

def demo_homomorphism():
    print("\nCKKS Homomorphism Observation\n")
    
    # Create context with better precision
    ctx = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,  # Increased for better precision
        coeff_mod_bit_sizes=[60, 40, 40, 60]  # More levels for multiplication
    )
    ctx.global_scale = 2**40  # Large scale for better accuracy
    
    # Test vectors
    a = [1.0, 2.0, 3.0]
    b = [4.0, 5.0, 6.0]
    scalar = 2.5
    
    print(f"Test vectors: A={a}, B={b}")
    print(f"Test scalar: {scalar}\n")
    
    # Encrypt
    enc_a = ts.ckks_vector(ctx, a)
    enc_b = ts.ckks_vector(ctx, b)
    
    # 1. Additive homomorphism
    print("1. Additive Homomorphism:")
    print(f"   Enc({a}) + Enc({b})")
    
    enc_sum = enc_a + enc_b
    dec_sum = enc_sum.decrypt()
    expected_sum = [x+y for x,y in zip(a,b)]
    
    print(f"   Result: {[f'{x:.4f}' for x in dec_sum]}")
    print(f"   Expected: {expected_sum}")
    
    # Check with reasonable tolerance
    add_ok = np.allclose(dec_sum, expected_sum, rtol=0.01, atol=0.01)
    print(f"   ✓ Works: {add_ok}\n")
    
    # 2. Scalar multiplication - FIXED VERSION
    print("2. Scalar Multiplication:")
    print(f"   Enc({a}) * {scalar}")
    
    # Method 1: Direct multiplication
    enc_scaled = enc_a * scalar
    dec_scaled = enc_scaled.decrypt()
    expected_scaled = [x*scalar for x in a]
    
    print(f"   Result: {[f'{x:.4f}' for x in dec_scaled]}")
    print(f"   Expected: {expected_scaled}")
    
    # Check with CKKS-appropriate tolerance (CKKS is approximate!)
    # For multiplication, allow 2% relative error
    mul_ok = np.allclose(dec_scaled, expected_scaled, rtol=0.02, atol=0.02)
    print(f"   ✓ Works: {mul_ok}")
    
    # Show actual differences
    errors = [abs(d - e) for d, e in zip(dec_scaled, expected_scaled)]
    print(f"   Errors: {[f'{e:.4f}' for e in errors]}")
    print(f"   Relative errors: {[f'{e/abs(es):.1%}' for e,es in zip(errors, expected_scaled)]}\n")
    
    # 3. Alternative: Test with integer scalar first
    print("3. Integer Scalar Test (for comparison):")
    int_scalar = 2
    enc_scaled_int = enc_a * int_scalar
    dec_scaled_int = enc_scaled_int.decrypt()
    expected_scaled_int = [x*int_scalar for x in a]
    
    print(f"   Enc({a}) * {int_scalar}")
    print(f"   Result: {[f'{x:.4f}' for x in dec_scaled_int]}")
    print(f"   Expected: {expected_scaled_int}")
    
    int_mul_ok = np.allclose(dec_scaled_int, expected_scaled_int, rtol=0.01)
    print(f"   ✓ Works: {int_mul_ok}\n")
    

if __name__ == "__main__":
    demo_homomorphism()
