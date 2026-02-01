# Model P3: Algorithmic Compression Signatures (ACS) Toolkit

[![Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18444596-blue)](https://zenodo.org/records/18444596)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![Status: Production](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/Kirby6567/model-p3-acs-toolkit)

## 🔬 Scientific Abstract

Model P3 is a novel methodology for **passive cryptographic auditing** designed for Red Team operations. By analyzing the compression ratio (R) of RSA public keys against their file size (S), this toolkit identifies key strength (2048/4096-bit) and detects low-entropy artifacts (Honeypots) **without requiring metadata parsing or active probing**.

### The Universal Scaling Law

```
R = 1 + O/S
```

Where:
- **R** = Compression Ratio (compressed_size / original_size)
- **O** = Algorithmic Overhead constant (specific to compression algorithm)
- **S** = Original File Size

### Key Insight
- **Ratio > 0.85** → High entropy → **PRODUCTION KEY** ✅
- **Ratio < 0.85** → Low entropy → **HONEYPOT** ⚠️

---

## ⚔️ Operational Utility (Red Team)

### Stealth Reconnaissance
Classify target encryption standards **without triggering IDS signatures**. Unlike active scanning tools, Model P3 performs purely passive analysis:
- ✅ No network traffic
- ✅ No metadata parsing
- ✅ No IDS/IPS alerts
- ✅ 100% offline operation

### Honeypot Detection
Instantly identify decoy keys generated with low entropy, preventing **resource exhaustion during engagement**:
- ✅ Detects weak RNG implementations
- ✅ Identifies test/fake keys
- ✅ Validates key authenticity
- ✅ Optimizes target prioritization

---

## 🚀 Installation & Usage

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Kirby6567/model-p3-acs-toolkit.git
cd model-p3-acs-toolkit

# Install dependencies
pip install -r requirements.txt

# Run the analyzer
python src/analyzer.py --target ./keys --algo zlib
```

### Command-Line Options

```bash
python src/analyzer.py --help
```

**Parameters:**
- `--target TARGET` (required): Directory containing files to analyze
- `--algo {zlib,zstd,brotli}` (optional): Compression algorithm (default: zlib)

### Examples

#### Analyze current directory
```bash
python src/analyzer.py --target .
```

#### Analyze with Zstandard compression
```bash
python src/analyzer.py --target ./rsa_keys --algo zstd
```

#### Analyze with Brotli compression
```bash
python src/analyzer.py --target ./collected_keys --algo brotli
```

---

## 📊 Output Example

```
======================================================================
  MODEL P3: ALGORITHMIC COMPRESSION SIGNATURE TOOLKIT v1.0
  Research by: Cristhian Lucinger
  Target: RSA Key Auditing & Honeypot Detection
======================================================================

[*] Starting Passive Recon on: ./keys
[*] Applying Algorithmic Compression Signatures (ACS)...
[*] Algorithm: ZLIB
----------------------------------------------------------------------------------------------------
FILENAME                       | SIZE (B)     | RATIO (R)  | STATUS        
----------------------------------------------------------------------------------------------------
rsa_key_prod1.pem             | 1704         | 0.8545     | PRODUCTION    
rsa_key_prod2.pem             | 1704         | 0.8612     | PRODUCTION    
fake_key_honeypot.pem         | 1704         | 0.7234     | HONEYPOT DETECTED
rsa_key_prod3.pem             | 2048         | 0.8703     | PRODUCTION    
----------------------------------------------------------------------------------------------------

[+] SUMMARY:
    Production Keys: 3
    Honeypots Detected: 1
    Total Files Analyzed: 4
```

---

## 🧪 Validation & Testing

### Test Results

| Test Case | Algorithm | Files | Production | Honeypots | Accuracy |
|---|---|---|---|---|---|
| Project Files | ZLIB | 2 | 1 | 1 | ✅ 100% |
| Test Suite (repetitive) | ZLIB | 3 | 2 | 1 | ✅ 100% |
| Test Suite (repetitive) | ZSTD | 3 | 2 | 1 | ✅ 100% |
| Test Suite (repetitive) | BROTLI | 3 | 2 | 1 | ✅ 100% |

**Conclusion:** Achieved **100% accuracy** in honeypot detection across all tested compression algorithms.

---

## 🛠️ Compression Algorithms

### ZLIB (Default)
- **Speed:** ⚡⚡⚡ Fastest
- **Compression:** ⭐⭐ Standard
- **Use Case:** Quick reconnaissance

### Zstandard (ZSTD)
- **Speed:** ⚡⚡ Medium
- **Compression:** ⭐⭐⭐ Better
- **Use Case:** Detailed analysis

### Brotli
- **Speed:** ⚡ Slower
- **Compression:** ⭐⭐⭐⭐ Best
- **Use Case:** Text-heavy analysis

---

## 📋 Requirements

### System Requirements
- **OS:** Windows, Linux, macOS
- **Python:** 3.8 or higher
- **RAM:** 512 MB minimum
- **Disk Space:** 50 MB

### Python Dependencies

```
numpy==1.26.0
matplotlib==3.8.0
zstandard==0.22.0
brotli==1.1.0
scipy==1.11.0
```

Install:
```bash
pip install -r requirements.txt
```

---

## 🎯 Use Cases

### Red Team Operations
- **Passive Key Classification** - Discover SSH keys without IDS alert
- **Honeypot Avoidance** - Validate collected keys before exploitation
- **Target Prioritization** - Identify high-value production keys

### Security Research
- Cryptographic key analysis
- Entropy measurement
- RNG quality assessment

---

## 📞 Support & Contact

### Contact
- 🔗 [LinkedIn](https://www.linkedin.com/in/cristhian-lucinger/)
- 🐙 [GitHub](https://github.com/Kirby6567)
- 📚 [Research](https://zenodo.org/records/18444596)

---

## 👨‍🔬 Author

**Cristhian Edilson Lucinger**

Cybersecurity Researcher specializing in Offensive Security, Applied Cryptography, and Purple Team Strategy.

Developed as part of Undergraduate Research in Applied Cryptography at Anhanguera University, Brazil.

---

## 📜 License

MIT License - See LICENSE file for details

---

<div align="center">

Made with ❤️ by **Cristhian Lucinger**  
[Report Bug](https://github.com/Kirby6567/model-p3-acs-toolkit/issues) • [Request Feature](https://github.com/Kirby6567/model-p3-acs-toolkit/issues)

**Version 1.0.0 | Production Ready ✅**

</div>
