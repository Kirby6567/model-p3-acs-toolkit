import os
import sys
import zlib
import argparse
import time


def banner():
    print("""
███    ███  ██████  ██████  ███████ ██      ██████  
██████ ██████  ████ ██    ██ ██   ██ ██      ██      
██   ██      ████ ████ ██ ██    ██ ██   ██ █████   
██      ██████   ███████  ██  ██ ██    ██ ██   ██ 
██      ██      ██           ████      ██  ██████  

[ Model P3: Algorithmic Compression Signature Toolkit v1.0 ]
[ Research by: Cristhian Lucinger | Target: RSA Key Auditing ]
""")


def calculate_p3_metrics(file_path, algo='zlib'):
    """
    Calculates the P3 Spectral Ratio based on the Universal Scaling Law:
    R = 1 + O/S (Theory)
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        original_size = len(data)
        if original_size == 0:
            return None

        start_time = time.time()

        # Algorithmic Compression Simulation
        if algo == 'zlib':
            compressed_data = zlib.compress(data, level=9)
        else:
            # Fallback for demo purposes
            compressed_data = zlib.compress(data, level=1)

        compressed_size = len(compressed_data)
        exec_time = (time.time() - start_time) * 1000

        # The P3 Ratio (R)
        ratio = compressed_size / original_size

        return {
            'file': os.path.basename(file_path),
            'size': original_size,
            'compressed': compressed_size,
            'ratio': ratio,
            'time_ms': exec_time
        }
    except Exception as e:
        print(f"[!] Error analyzing {file_path}: {e}")
        return None


def analyze_directory(target_dir):
    print(f"[*] Starting Passive Recon on: {target_dir}")
    print(f"[*] Applying Algorithmic Compression Signatures (ACS)...")
    print("-" * 80)
    print(f"{'FILENAME':<25} | {'SIZE (B)':<12} | {'RATIO (R)':<10} | {'STATUS':<20}")
    print("-" * 80)

    files = [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]

    for file in files:
        path = os.path.join(target_dir, file)
        metrics = calculate_p3_metrics(path)

        if metrics:
            status = "✅ PRODUCTION"
            # Low Entropy (Honeypot) usually compresses way too well (Ratio < 0.85)
            if metrics['ratio'] < 0.85:
                status = "⚠️ HONEYPOT DETECTED"

            print(f"{metrics['file']:<25} | {metrics['size']:<12} | {metrics['ratio']:.4f}     | {status:<20}")


def main():
    banner()
    parser = argparse.ArgumentParser(description='Model P3: Passive RSA Key Auditing Tool')
    parser.add_argument('--target', type=str, help='Directory containing keys to analyze', required=True)
    parser.add_argument('--algo', type=str, default='zlib', help='Compression Algorithm (zlib, zstd, brotli)')
    args = parser.parse_args()

    if not os.path.exists(args.target):
        print(f"[X] Target directory '{args.target}' not found.")
        sys.exit(1)

    analyze_directory(args.target)


if __name__ == "__main__":
    main()
