# --- CAN304 Lab  -----------------------------------------------------
#
# Lab 3: Cryptographic Hash Functions and Message Authentication
#
# Compare different cryptographic hash functions
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------


from Crypto.Hash import MD5, SHA1, SHA256, SHA512, SHA3_256, SHA3_512
import time
import os
import json

class HashFunctionAnalyzer:
    def __init__(self):
        self.results = {}
    
    def compute_hashes(self, data: bytes) -> dict:
        """Compute hashes using different algorithms"""
        hashes = {}
        
        algorithms = [
            ('MD5', MD5),
            ('SHA-1', SHA1),
            ('SHA-256', SHA256),
            ('SHA-512', SHA512),
            ('SHA3-256', SHA3_256),
            ('SHA3-512', SHA3_512)
        ]
        
        for algo_name, algo_class in algorithms:
            start_time = time.perf_counter()
            hash_obj = algo_class.new(data)
            digest = hash_obj.hexdigest()
            elapsed = (time.perf_counter() - start_time) * 1000
            
            hashes[algo_name] = {
                'digest': digest,
                'length': len(digest) * 4,  # Convert hex chars to bits
                'time_ms': round(elapsed, 4)
            }
        
        return hashes
    
    def avalanche_effect_test(self):
        """Test avalanche effect: small input change = big output change"""
        
        # Create two messages differing by one bit
        message1 = b"A" * 100
        message2 = b"B" + b"A" * 99  # Only first character differs
        
        print(f"Message 1: {message1[:20].decode()}... (100 'A's)")
        print(f"Message 2: {message2[:20].decode()}... ('B' + 99 'A's)")
        
        algorithms = [SHA256, SHA512, SHA3_256]
        
        for algo_class in algorithms:
            algo_name = algo_class.__name__.replace('Hash', '')
            
            # Compute hashes
            hash1 = algo_class.new(message1).hexdigest()
            hash2 = algo_class.new(message2).hexdigest()
            
            # Convert to binary for bit comparison
            bin1 = bin(int(hash1, 16))[2:].zfill(len(hash1) * 4)
            bin2 = bin(int(hash2, 16))[2:].zfill(len(hash2) * 4)
            
            # Count differing bits
            diff_bits = sum(1 for b1, b2 in zip(bin1, bin2) if b1 != b2)
            diff_percentage = (diff_bits / len(bin1)) * 100
            
            print(f"\n{algo_name}:")
            print(f"  Hash 1: {hash1[:32]}...")
            print(f"  Hash 2: {hash2[:32]}...")
            print(f"  Differing bits: {diff_bits}/{len(bin1)} ({diff_percentage:.2f}%)")
            
           
    
    def run_experiment(self):
        """Execute all parts of Experiment 1"""
        
        # Part 1: Basic hash computation
        test_message = b"Cryptography is essential for modern security"
        print(f"\n1: Basic Hash Computation")
        print(f"Message: {test_message.decode()}")
        
        hashes = self.compute_hashes(test_message)
        for algo, data in hashes.items():
            print(f"{algo:12} | {data['digest'][:32]}... | "
                  f"{data['length']:4} bits | {data['time_ms']:7.4f} ms")
        
        # Part 2: Avalanche effect
        print(f"\n2: Avalanche Effect")
        self.avalanche_effect_test()
        

if __name__ == "__main__":
    analyzer = HashFunctionAnalyzer()
    analyzer.run_experiment()
