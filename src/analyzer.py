import os
import sys
import zlib
import argparse
import time


def banner():
    print("\n" + "="*70)
    print("  MODEL P3: ALGORITHMIC COMPRESSION SIGNATURE TOOLKIT v1.0")
    print("  Research by: Cristhian Lucinger")
    print("  Target: RSA Key Auditing & Honeypot Detection")
    print("="*70 + "\n")


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
        elif algo == 'brotli':
            try:
                import brotli
                compressed_data = brotli.compress(data)
            except ImportError:
                print("[!] Brotli not installed. Using zlib instead.")
                compressed_data = zlib.compress(data, level=9)
        elif algo == 'zstd':
            try:
                import zstandard as zstd
                cctx = zstd.ZstdCompressor()
                compressed_data = cctx.compress(data)
            except ImportError:
                print("[!] Zstandard not installed. Using zlib instead.")
                compressed_data = zlib.compress(data, level=9)
        else:
            compressed_data = zlib.compress(data, level=9)

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


def analyze_directory(target_dir, algo='zlib'):
    print(f"[*] Starting Passive Recon on: {target_dir}")
    print(f"[*] Applying Algorithmic Compression Signatures (ACS)...")
    print(f"[*] Algorithm: {algo.upper()}")
    print("-" * 100)
    print(f"{'FILENAME':<30} | {'SIZE (B)':<12} | {'RATIO (R)':<10} | {'STATUS':<20}")
    print("-" * 100)

    try:
        files = [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]
    except PermissionError:
        print(f"[X] Permission denied to access {target_dir}")
        return

    if not files:
        print(f"[!] No files found in {target_dir}")
        return

    count_production = 0
    count_honeypot = 0

    for file in files:
        path = os.path.join(target_dir, file)
        metrics = calculate_p3_metrics(path, algo)

        if metrics:
            status = "PRODUCTION"
            # Low Entropy (Honeypot) usually compresses way too well (Ratio < 0.85)
            if metrics['ratio'] < 0.85:
                status = "HONEYPOT DETECTED"
                count_honeypot += 1
            else:
                count_production += 1

            print(f"{metrics['file']:<30} | {metrics['size']:<12} | {metrics['ratio']:.4f}     | {status:<20}")

    print("-" * 100)
    print(f"\n[+] SUMMARY:")
    print(f"    Production Keys: {count_production}")
    print(f"    Honeypots Detected: {count_honeypot}")
    print(f"    Total Files Analyzed: {count_production + count_honeypot}\n")


def main():
    banner()
    parser = argparse.ArgumentParser(
        description='Model P3: Passive RSA Key Auditing Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXAMPLES:

  Analyze keys in current directory (using zlib):
    python analyzer.py --target .

  Analyze RSA keys folder with Zstandard compression:
    python analyzer.py --target ./keys --algo zstd

  Analyze with Brotli algorithm:
    python analyzer.py --target ./rsa_keys --algo brotli

ALGORITHMS:
  - zlib (default, fastest)
  - zstd (Zstandard, better compression)
  - brotli (Brotli, best for text)

INTERPRETATION:
  - Ratio < 0.85: LIKELY HONEYPOT (low entropy, compresses too well)
  - Ratio > 0.85: LIKELY PRODUCTION KEY (high entropy, resists compression)
        """
    )
    
    parser.add_argument('--target', 
                       type=str, 
                       help='Directory containing keys to analyze', 
                       required=True)
    parser.add_argument('--algo', 
                       type=str, 
                       default='zlib', 
                       choices=['zlib', 'zstd', 'brotli'],
                       help='Compression Algorithm (default: zlib)')
    
    args = parser.parse_args()

    if not os.path.exists(args.target):
        print(f"[X] Target directory '{args.target}' not found.")
        sys.exit(1)

    if not os.path.isdir(args.target):
        print(f"[X] '{args.target}' is not a directory.")
        sys.exit(1)

    analyze_directory(args.target, args.algo)


if __name__ == "__main__":
    main()