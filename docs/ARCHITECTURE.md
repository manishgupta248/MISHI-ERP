# MISHI-ERP — Architecture

## High-Level Structure

Mishika
    |
    +-- core
    |
    +-- Future Django Applications
    |
    +-- Shared Templates
    |
    +-- Shared Static
    |
    +-- Database
    |
    +-- AI / Agent Layer
    |
    +-- Events / Scheduler
    |
    +-- Telegram Integration

## Principles

1. Modular Django applications
2. Shared common services through `core`
3. Clear separation of responsibilities
4. Environment configuration outside source code
5. Incremental development
6. Automated smoke testing where practical
7. Avoid unnecessary dependencies
8. Keep AI/LLM components loosely coupled to ERP modules