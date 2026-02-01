# Model P3: Algorithmic Compression Signatures (ACS) Toolkit

[![Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18444596-blue)](https://zenodo.org/records/18444596)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

## 🔬 Scientific Abstract

Model P3 is a novel methodology for **passive cryptographic auditing**. By analyzing the compression ratio (R) of RSA public keys against their file size (S), this toolkit identifies the key strength (2048 vs 4096 bits) and detects low-entropy artifacts (Honeypots) without requiring metadata parsing or active probing.

The core discovery is the **Universal Scaling Law**:

\\\
R = 1 + O/S
\\\

Where O represents the algorithmic overhead constant specific to the compression algorithm (ZLIB, Zstd, Brotli).

## ⚔️ Operational Utility (Red Team)

For Offensive Security operations, this tool allows for:

1. **Stealth Recon:** Classify target encryption standards without triggering IDS signatures associated with active scanning.
2. **Honeypot Detection:** Instantly identify decoy keys generated with low entropy, preventing resource exhaustion during engagement.

## 🚀 Installation & Usage

\\\ash
# Clone the repository
git clone https://github.com/Kirby6567/model-p3-acs-toolkit.git
cd model-p3-acs-toolkit

# Install dependencies
pip install -r requirements.txt

# Run the analyzer
python src/analyzer.py --target keys/ --algo zlib
\\\

## 📊 Validation

Validated with N=150 samples. Achieving statistical absolute confidence in differentiating High-Entropy Production Keys from Low-Entropy Decoys.

## 👨‍🔬 Author

Developed by **Cristhian Edilson Lucinger** as part of Undergraduate Research in Applied Cryptography.

---

## 📜 License

MIT License - See LICENSE file for details
