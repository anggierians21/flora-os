# Flora Runtime Engine

Runtime Engine adalah lapisan yang menghubungkan Knowledge Base Flora OS dengan Hermes Agent.

## Tujuan

- Membaca seluruh knowledge
- Menggabungkan knowledge menjadi runtime context
- Menyediakan context kepada seluruh AI Agent
- Menjadikan GitHub sebagai Single Source of Truth

## Alur

GitHub Knowledge

↓

Loader

↓

Builder

↓

Runtime Context

↓

Hermes Agent

↓

Research
Writer
Designer
Publisher
Analytics

## Komponen

loader.py

Membaca seluruh markdown.

builder.py

Menyusun runtime context.

context.py

Memberikan context kepada AI Agent.
