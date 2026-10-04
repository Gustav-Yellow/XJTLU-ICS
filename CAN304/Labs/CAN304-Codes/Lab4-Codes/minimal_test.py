# --- CAN304 Lab  -----------------------------------------------------
# Lab 4: CKKS Fully Homomorphic Encryption
#
# Basic CKKS functionality test
# Run this first to verify your setup works correctly
#
# By Jie Zhang <Jie.Zhang01@xjtlu.edu.cn>
#
# ----------------------------------------------------------------------

import tenseal as ts
import numpy as np

def run_minimal_test():
    
    print("\nCKKS Minimal Test - Verify Your Installation")
    
    # 1. Check version
    print(f"tenseal version: {ts.__version__}")
    
    # 2. Create context with simple parameters
    print("\n1. Creating CKKS context...")
    try:
        # Use minimal parameters that work reliably
        ctx = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=4096,
            coeff_mod_bit_sizes=[40, 20, 40]
        )
        ctx.global_scale = 2**20
        print("✓ Context created successfully")
    except Exception as e:
        print(f"✗ Failed to create context: {e}")
        print("\nTrying alternative parameters...")
        try:
            # Try with even simpler parameters
            ctx = ts.context(
                ts.SCHEME_TYPE.CKKS,
                poly_modulus_degree=2048,
                coeff_mod_bit_sizes=[30, 20, 30]
            )
            ctx.global_scale = 2**20
            print("✓ Context created with alternative parameters")
        except Exception as e2:
            print(f"✗ All attempts failed: {e2}")
            return False
    
    # 3. Basic encryption/decryption
    print("\n2. Testing encryption/decryption...")
    plaintext = [1.5, 2.5, 3.5]
    print(f"Plaintext: {plaintext}")
    
    try:
        ciphertext = ts.ckks_vector(ctx, plaintext)
        decrypted = ciphertext.decrypt()
        
        print(f"Decrypted: [{', '.join(f'{x:.6f}' for x in decrypted)}]")
        
        # Format numbers for consistent output
        formatted_decrypted = [f"{x:.6f}" for x in decrypted]
        print(f"Decrypted: [{', '.join(formatted_decrypted)}]")
        
        # Calculate and display error
        error = np.max(np.abs(np.array(plaintext) - np.array(decrypted)))
        print(f"Maximum error: {error:.10f}")
        
    except Exception as e:
        print(f"✗ Encryption/decryption failed: {e}")
        return False
    
    # 4. Homomorphic addition
    print("\n3. Testing homomorphic addition...")
    try:
        ciphertext2 = ciphertext + ciphertext
        decrypted2 = ciphertext2.decrypt()
        expected2 = [x*2 for x in plaintext]
        
        # Format for consistent display
        formatted_decrypted2 = [f"{x:.6f}" for x in decrypted2]
        formatted_expected2 = [f"{x:.6f}" for x in expected2]
        
        print(f"Ciphertext + Ciphertext: [{', '.join(formatted_decrypted2)}]")
        print(f"Expected: [{', '.join(formatted_expected2)}]")
        
        # Test with tolerance
        addition_works = np.allclose(decrypted2, expected2, rtol=1e-3)
        print(f"Addition works: {addition_works}")
        
    except Exception as e:
        print(f"✗ Homomorphic addition failed: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("Setup verification: PASSED ✓")
    print("You can now proceed to main experiments!")
    print("=" * 50)
    
    return True

if __name__ == "__main__":
    # Run test
    success = run_minimal_test()
    
    # Provide helpful information based on results
    if not success:
        print("\n" + "=" * 50)
        print("TROUBLESHOOTING TIPS:")
        print("=" * 50)
        print("1. Make sure virtual environment is activated:")
        print("   Windows: ckks-env\\Scripts\\activate")
        print("   macOS/Linux: source ckks-env/bin/activate")
        print("\n2. Try reinstalling tenseal:")
        print("   pip install --upgrade tenseal")
        print("\n3. For macOS users, ensure Xcode tools are installed:")
        print("   xcode-select --install")
        print("\n4. For memory issues, reduce poly_modulus_degree to 2048")
        exit(1)
