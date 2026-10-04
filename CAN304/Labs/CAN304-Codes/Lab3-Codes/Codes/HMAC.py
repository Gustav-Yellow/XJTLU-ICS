# --- CAN304 Lab  -----------------------------------------------------
#
# Lab 3: Cryptographic Hash Functions and Message Authentication
#
# HMAC implementation: Hash-based Message Authentication Code
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------

from Crypto.Hash import HMAC, SHA256, SHA512
import secrets
import base64
import json
import time

class HMACExperiment:
    def __init__(self):
        self.secret_keys = {}
    
    def generate_secure_key(self, key_size=32):
        """Generate cryptographically secure random key"""
        return secrets.token_bytes(key_size)
    
    def compute_hmac(self, message: str, key: bytes, algorithm='SHA256'):
        """Compute HMAC for given message and key"""
        if algorithm.upper() == 'SHA256':
            hmac_obj = HMAC.new(key, digestmod=SHA256)
        elif algorithm.upper() == 'SHA512':
            hmac_obj = HMAC.new(key, digestmod=SHA512)
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        hmac_obj.update(message.encode('utf-8'))
        return hmac_obj.hexdigest()
    
    def message_authentication_demo(self):
        """Demonstrate message authentication with HMAC"""
        
        # Generate secret key (shared between sender and receiver)
        secret_key = self.generate_secure_key(32)
        self.secret_keys['shared_key'] = secret_key
        
        # Original message
        original_message = "Transfer $1000 to account 987654321"
        print(f"\nOriginal Message: {original_message}")
        print(f"Secret Key (base64): {base64.b64encode(secret_key).decode()}")
        
        # Sender computes HMAC
        hmac_sender = self.compute_hmac(original_message, secret_key, 'SHA256')
        print(f"\n[SENDER] Computed HMAC-SHA256: {hmac_sender}")
        
        # Receiver verifies
        print("\n[RECEIVER] Verification Process:")
        hmac_receiver = self.compute_hmac(original_message, secret_key, 'SHA256')
        
        # Secure comparison (timing-attack resistant)
        if secrets.compare_digest(hmac_sender, hmac_receiver):
            print("Message authentication successful")
        else:
            print("Message authentication failed")
        
        return {
            'message': original_message,
            'key': base64.b64encode(secret_key).decode(),
            'hmac': hmac_sender
        }
    
    def message_tampering_test(self):
        """Test detection of message tampering"""

        
        # Setup
        secret_key = self.generate_secure_key(32)
        original_message = "Critical command: SHUTDOWN system at 0300"
        
        # Compute original HMAC
        original_hmac = self.compute_hmac(original_message, secret_key, 'SHA256')
        
        print(f"Original Message: {original_message}")
        print(f"Original HMAC: {original_hmac}")
        
        # Simulate tampering during transmission
        tampered_message = "Critical command: SHUTDOWN system at 1300"  # Changed time
        
        print(f"\n[TAMPERING DETECTED]")
        print(f"Intercepted Message: {tampered_message}")
        
        # Compute HMAC for tampered message
        tampered_hmac = self.compute_hmac(tampered_message, secret_key, 'SHA256')
        
        # Verify
        print(f"Computed HMAC for received message: {tampered_hmac}")
        print(f"Stored HMAC for original message:  {original_hmac}")
        
        if secrets.compare_digest(original_hmac, tampered_hmac):
            print("\nSECURITY BREACH: Tampering not detected!")
        else:
            print("\nSECURITY MAINTAINED: Tampering detected and rejected")
    
   
    
    def run_experiment(self):

        results = {}
        
        # Part 1: Basic message authentication
        print("\n1: Basic Message Authentication")
        auth_result = self.message_authentication_demo()
        results['authentication'] = auth_result
        
        # Part 2: Tampering detection
        print("\n2: Message Tampering Detection")
        self.message_tampering_test()
        
        


if __name__ == "__main__":
    hmac_exp = HMACExperiment()
    hmac_exp.run_experiment()
