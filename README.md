# Package Sorter

This repository contains the implementation of a package sorter for Thoughtful's robotic automation factory. The sorter dispatches packages into stacks based on their volume, dimensions, and mass.

## Sorting Criteria

1. **Bulky**: A package is bulky if:
   - Volume (Width x Height x Length) ≥ 1,000,000 cm³, or
   - Any dimension ≥ 150 cm.
2. **Heavy**: A package is heavy if its mass ≥ 20 kg.

### Stacks

- **STANDARD**: Not bulky or heavy.
- **SPECIAL**: Either bulky or heavy.
- **REJECTED**: Both bulky and heavy.

## Function Details

The main function `sort(width, height, length, mass)` returns the stack name for the package.

### Usage

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd package_sorter
