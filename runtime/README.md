# Flora Runtime Engine

Runtime Engine adalah lapisan yang menghubungkan Flora Knowledge Base dengan Hermes Agent.

Runtime bertanggung jawab membaca seluruh knowledge, menyusunnya menjadi Runtime Context, menyimpan cache, dan menyediakan context kepada seluruh AI Agent.

---

# Tujuan

- Membaca seluruh Knowledge Base
- Memuat Brain Flora
- Menyusun Runtime Context
- Mengurangi waktu loading melalui cache
- Menyediakan context yang konsisten kepada seluruh AI Agent
- Menjadikan GitHub sebagai Single Source of Truth

---

# Runtime Flow

GitHub Repository

↓

Knowledge Loader

↓

Registry

↓

Brain Loader

↓

Runtime Builder

↓

Runtime Cache

↓

Context Provider

↓

Hermes Agent

---

# Components

## loader.py

Membaca seluruh file markdown dari repository.

---

## registry.py

Menentukan folder dan file yang menjadi bagian Runtime.

---

## builder.py

Menggabungkan seluruh knowledge menjadi Runtime Context.

---

## cache.py

Menyimpan hasil Runtime Build agar proses berikutnya lebih cepat.

---

## context.py

Menyediakan Runtime Context kepada seluruh AI Agent.

---

## bootstrap.py

Menjalankan seluruh proses Runtime dari awal hingga siap digunakan.

---

# Build Order

1. Brain
2. Organization
3. Programs
4. Operations
5. Agents
6. Islamic Knowledge
7. Learning

---

# Filosofi

Knowledge adalah sumber kebenaran.

Brain menentukan cara berpikir.

Runtime adalah hasil kompilasi seluruh pengetahuan.

Hermes hanya menggunakan Runtime.

---

# Future

- Incremental Build

---

# Runtime API

Seluruh AI Agent **wajib** mengakses Runtime melalui `RuntimeManager`.

Agent **tidak boleh** mengakses `loader.py`, `builder.py`, `registry.py`, `cache.py`, atau `context.py` secara langsung.

Contoh penggunaan:

```python
from runtime.manager import RuntimeManager

context = RuntimeManager.load()
```

RuntimeManager merupakan **single entrypoint** Runtime Engine.

Keuntungan pendekatan ini:

- Menyembunyikan implementasi internal Runtime.
- Memudahkan perubahan arsitektur tanpa mengubah seluruh Agent.
- Menjaga konsistensi cara seluruh Agent memperoleh Runtime Context.
- Runtime Versioning
- Plugin System
- Memory Engine
- Multi-Agent Runtime
- Runtime Analytics
